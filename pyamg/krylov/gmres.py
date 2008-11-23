from numpy import array, zeros, ones, sqrt, ravel, abs, max, dot, arange, conjugate
from scipy.sparse import csr_matrix
from scipy.sparse.linalg.isolve.utils import make_system
from scipy.sparse.sputils import upcast
from scipy import hstack, ceil, isnan, isinf
from scipy.linalg import lu_solve
from warnings import warn
from pyamg.util.linalg import norm
from pyamg import multigridtools
import scipy.sparse

__docformat__ = "restructuredtext en"

__all__ = ['gmres']

def mysign(x):
    if x == 0.0:
        return 1.0
    else:
        # return the complex "sign"
        return x/abs(x)

def gmres(A, b, x0=None, tol=1e-5, restrt=None, maxiter=None, xtype=None, M=None, callback=None, residuals=None):
    '''
    Generalized Minimum Residual Method (GMRES)
        GMRES iteratively refines the initial solution guess to the system Ax = b
    For robustness, Householder reflections are used to orthonormalize the Krylov Space
    Givens Rotations are used to provide the residual norm each iteration

    Parameters
    ----------
    A : array, matrix or sparse matrix
        n x n, linear system to solve
    b : array
        n x 1, right hand side
    x0 : array
        n x 1, initial guess
        default is a vector of zeros
    tol : float
        convergence tolerance
    restrt : int
        number of restarts
        total iterations = restrt*maxiter
    maxiter : int
        maximum number of allowed inner iterations
    M : matrix-like
        n x n, inverted preconditioner, i.e. solve M A x = b.
        For preconditioning with a mat-vec routine, set
        A.psolve = func, where func := M y
    callback : function
        callback( ||resid||_2 ) is called each iteration, 
    residuals : {None, empty-list}
        If empty-list, residuals holds the residual norm history,
        including the initial residual, upon completion
     
    Returns
    -------    
    (xNew, info)
    xNew -- an updated guess to the solution of Ax = b
    info -- halting status of gmres
            0  : successful exit
            >0 : convergence to tolerance not achieved,
                 return iteration count instead.  This value
                 is precisely the order of the Krylov space.
            <0 : numerical breakdown, or illegal input


    Notes
    -----
    
    Examples
    --------
    >>>from pyamg.krylov import *
    >>>from scipy import rand
    >>>import pyamg
    >>>A = pyamg.poisson((50,50))
    >>>b = rand(A.shape[0],)
    >>>(x,flag) = gmres(A,b)
    >>>print pyamg.util.linalg.norm(b - A*x)

    References
    ----------
    Yousef Saad, "Iterative Methods for Sparse Linear Systems, 
    Second Edition", SIAM, pp. 151-172, pp. 272-275, 2003

    '''
    # Convert inputs to linear system, with error checking  
    A,M,x,b,postprocess = make_system(A,M,x0,b,xtype)
    dimen = A.shape[0]

    # Choose type
    xtype = upcast(A.dtype, x.dtype, b.dtype, M.dtype)

    # Should norm(r) be kept
    if residuals == []:
        keep_r = True
    else:
        keep_r = False

    # check number of iterations
    if restrt == None:
        restrt = 1
    elif restrt < 1:
        raise ValueError('Number of restarts must be positive')

    if maxiter == None:
        maxiter = int(min(ceil(dimen/restrt), 40.0))
    elif maxiter < 1:
        raise ValueError('Number of iterations must be positive')
    elif maxiter > dimen:
        warn('maximimum allowed inner iterations (maxiter) are the number of degress of freedom')
        maxiter = dimen

    # Scale tol by normb
    normb = norm(b) 
    if normb == 0:
        pass
    #    if callback != None:
    #        callback(0.0)
    #
    #    return (postprocess(zeros((dimen,)), dtype=xtype),0)
    else:
        tol = tol*normb

    # Is this a one dimensional matrix?
    if dimen == 1:
        entry = ravel(A*array([1.0], dtype=xtype))
        return (postprocess(b/entry), 0)

    # Prep for method
    r = b - ravel(A*x)
    normr = norm(r)
    if keep_r:
        residuals.append(normr)
    
    # Is initial guess sufficient?
    if normr <= tol:
        if callback != None:    
            callback(norm(r))
        
        return (postprocess(x), 0)

    #Apply preconditioner
    r = ravel(M*r)
    normr = norm(r)
    ## Check for nan, inf    
    #if isnan(r).any() or isinf(r).any():
    #    warn('inf or nan after application of preconditioner')
    #    return(postprocess(x), -1)
    
    # Use separate variable to track iterations.  If convergence fails, we cannot 
    # simply report niter = (outer-1)*maxiter + inner.  Numerical error could cause 
    # the inner loop to halt before reaching maxiter while the actual ||r|| > tol.
    niter = 0

    # Begin GMRES
    for outer in range(restrt):
        
        # Calculate vector w, which defines the Householder reflector
        #    Take shortcut in calculating, 
        #    w = r + sign(r[1])*||r||_2*e_1
        w = r 
        beta = mysign(w[0])*normr
        w[0] += beta
        w /= norm(w)
    
        # Preallocate for Krylov vectors, Householder reflectors and Hessenberg matrix
        # Space required is O(dimen*maxiter)
        Q = zeros( (4*maxiter,), dtype=xtype)               # Given's Rotations
        H = zeros( (maxiter, maxiter), dtype=xtype)         # upper Hessenberg matrix (actually made upper tri with Given's Rotations) 
        W = zeros( (maxiter, dimen), dtype=xtype)           # Householder reflectors
        W[0,:] = w
    
        # Multiply r with (I - 2*w*w.T), i.e. apply the Householder reflector
        # This is the RHS vector for the problem in the Krylov Space
        g = zeros((dimen,), dtype=xtype) 
        g[0] = -beta

        for inner in range(maxiter):
            # Calcute Krylov vector in two steps
            # (1) Calculate v = P_j = (I - 2*w*w.T)v, where k = inner
            v = -2.0*conjugate(w[inner])*w
            v[inner] += 1.0
            # (2) Calculate the rest, v = P_1*P_2*P_3...P_{j-1}*ej.
            #for j in range(inner-1,-1,-1):
            #    v -= 2.0*dot(conjugate(W[j,:]), v)*W[j,:]
            multigridtools.apply_householders(v, ravel(W), dimen, inner-1, -1, -1)

            # Calculate new search direction
            v = ravel(A*v)

            #Apply preconditioner
            v = ravel(M*v)
            ## Check for nan, inf    
            #if isnan(v).any() or isinf(v).any():
            #    warn('inf or nan after application of preconditioner')
            #    return(postprocess(x), -1)

            # Factor in all Householder orthogonal reflections on new search direction
            #for j in range(inner+1):
            #    v -= 2.0*dot(conjugate(W[j,:]), v)*W[j,:]
            multigridtools.apply_householders(v, ravel(W), dimen, 0, inner+1, 1)
                  
            # Calculate next Householder reflector, w
            #  w = v[inner+1:] + sign(v[inner+1])*||v[inner+1:]||_2*e_{inner+1)
            #  Note that if maxiter = dimen, then this is unnecessary for the last inner 
            #     iteration, when inner = dimen-1.  Here we do not need to calculate a
            #     Householder reflector or Given's rotation because nnz(v) is already the
            #     desired length, i.e. we do not need to zero anything out.
            if inner != dimen-1:
                if inner < (maxiter-1):
                    w = W[inner+1,:]
                vslice = v[inner+1:]
                alpha = norm(vslice)
                if alpha != 0:
                    alpha = mysign(vslice[0])*alpha
                    # We do not need the final reflector for future calculations
                    if inner < (maxiter-1):
                        w[inner+1:] = vslice
                        w[inner+1] += alpha
                        w /= norm(w)
      
                    # Apply new reflector to v
                    #  v = v - 2.0*w*(w.T*v)
                    v[inner+1] = -alpha
                    v[inner+2:] = 0.0
            

            if inner > 0:
                # Apply all previous Given's Rotations to v
                multigridtools.apply_givens(Q, v, dimen, inner)

            # Calculate the next Given's rotation, where j = inner
            #  Note that if maxiter = dimen, then this is unnecessary for the last inner 
            #     iteration, when inner = dimen-1.  Here we do not need to calculate a
            #     Householder reflector or Given's rotation because nnz(v) is already the
            #     desired length, i.e. we do not need to zero anything out.
            if inner != dimen-1:
                if v[inner+1] != 0:
                    # Calculate terms for complex 2x2 Given's Rotation
                    # Note that abs(x) takes the complex modulus
                    h1 = v[inner]; h2 = v[inner+1];
                    h1_mag = abs(h1); h2_mag = abs(h2);
                    if h1_mag < h2_mag:
                        mu = h1/h2
                        tau = conjugate(mu)/abs(mu)
                    else:    
                        mu = h2/h1
                        tau = mu/abs(mu)

                    denom = sqrt( h1_mag**2 + h2_mag**2 )               
                    c = h1_mag/denom; s = h2_mag*tau/denom; 
                    Qblock = array([[c, conjugate(s)], [-s, c]], dtype=xtype) 
                    Q[(inner*4) : ((inner+1)*4)] = ravel(Qblock).copy()
                    
                    # Apply Given's Rotation to g, 
                    #   the RHS for the linear system in the Krylov Subspace.
                    #   Note that this dot does a matrix multiply, not an actual
                    #   dot product where a conjugate transpose is taken
                    g[inner:inner+2] = dot(Qblock, g[inner:inner+2])
                    
                    # Apply effect of Given's Rotation to v
                    v[inner] = dot(Qblock[0,:], v[inner:inner+2]) 
                    v[inner+1] = 0.0
            
            # Write to upper Hessenberg Matrix,
            #   the LHS for the linear system in the Krylov Subspace
            H[:,inner] = v[0:maxiter]

            # Don't update normr if last inner iteration, because 
            # normr is calculated directly after this loop ends.
            if inner < maxiter-1:
                normr = abs(g[inner+1])
                if normr < tol:
                    break
                
                # Allow user access to residual
                if callback != None:
                    callback( normr )
                if keep_r:
                    residuals.append(normr)
            
            niter += 1
            
        # end inner loop, back to outer loop

        # Find best update to x in Krylov Space, V.  Solve inner+1 x inner+1 system.
        #   Apparently this is the best way to solve a triangular
        #   system in the magical world of scipy
        piv = arange(inner+1)
        y = lu_solve((H[0:(inner+1),0:(inner+1)], piv), g[0:(inner+1)], trans=0)
        
        # Use Horner like Scheme to map solution, y, back to original space.
        # Note that we do not use the last reflector.
        update = zeros(x.shape, dtype=xtype)
        #for j in range(inner,-1,-1):
        #    update[j] += y[j]
        #    # Apply j-th reflector, (I - 2.0*w_j*w_j.T)*upadate
        #    update -= 2.0*dot(conjugate(W[j,:]), update)*W[j,:]
        multigridtools.householder_hornerscheme(update, ravel(W), ravel(y), dimen, inner, -1, -1)

        x += update
        r = b - ravel(A*x)

        #Apply preconditioner
        r = ravel(M*r)
        normr = norm(r)
        ## Check for nan, inf    
        #if isnan(r).any() or isinf(r).any():
        #    warn('inf or nan after application of preconditioner')
        #    return(postprocess(x), -1)
        
        # Allow user access to residual
        if callback != None:
            callback( normr )
        if keep_r:
            residuals.append(normr)
        
        # Has GMRES stagnated?
        indices = (x != 0)
        if indices.any():
            change = max(abs( update[indices] / x[indices] ))
            if change < 1e-12:
                # No change, halt
                return (postprocess(x), -1)

    
        # test for convergence
        if normr < tol:
            return (postprocess(x),0)
            
    # end outer loop
    
    return (postprocess(x), niter)



if __name__ == '__main__':
    # from numpy import diag
    # A = random((4,4))
    # A = A*A.transpose() + diag([10,10,10,10])
    # b = random((4,1))
    # x0 = random((4,1))
    #%timeit -n 15 (x,flag) = gmres(A,b,x0,tol=1e-8,maxiter=100)

    from pyamg.gallery import stencil_grid
    from numpy.random import random
    A = stencil_grid([[0,-1,0],[-1,4,-1],[0,-1,0]],(75,75),dtype=float,format='csr')
    b = random((A.shape[0],))
    x0 = random((A.shape[0],))

    import time
    from scipy.sparse.linalg.isolve import gmres as igmres

    print '\n\nTesting GMRES with %d x %d 2D Laplace Matrix'%(A.shape[0],A.shape[0])
    t1=time.time()
    (x,flag) = gmres(A,b,x0,tol=1e-8,maxiter=240)
    t2=time.time()
    print '%s took %0.3f ms' % ('gmres', (t2-t1)*1000.0)
    print 'norm = %g'%(norm(b - A*x))
    print 'info flag = %d'%(flag)

    t1=time.time()
    # DON"T Enforce a maxiter as scipy gmres can't handle it correctly
    (y,flag) = igmres(A,b,x0,tol=1e-8)
    t2=time.time()
    print '\n%s took %0.3f ms' % ('linalg gmres', (t2-t1)*1000.0)
    print 'norm = %g'%(norm(b - A*y))
    print 'info flag = %d'%(flag)

    