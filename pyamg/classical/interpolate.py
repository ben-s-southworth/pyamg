"""Classical AMG Interpolation methods"""


__docformat__ = "restructuredtext en"

import numpy as np
from scipy.sparse import csr_matrix, isspmatrix_csr
from pyamg import amg_core
from pyamg.relaxation.relaxation import boundary_relaxation

__all__ = ['direct_interpolation', 'standard_interpolation', 'trivial_interpolation', 'approximate_ideal_restriction']

def direct_interpolation(A, C, splitting, cost=[0]):
    """Create prolongator using direct interpolation

    Parameters
    ----------
    A : {csr_matrix}
        NxN matrix in CSR format
    C : {csr_matrix}
        Strength-of-Connection matrix
        Must have zero diagonal
    splitting : array
        C/F splitting stored in an array of length N

    Returns
    -------
    P : {csr_matrix}
        Prolongator using direct interpolation

    Examples
    --------
    >>> from pyamg.gallery import poisson
    >>> from pyamg.classical import direct_interpolation
    >>> import numpy as np
    >>> A = poisson((5,),format='csr')
    >>> splitting = np.array([1,0,1,0,1], dtype='intc')
    >>> P = direct_interpolation(A, A, splitting)
    >>> print P.todense()
    [[ 1.   0.   0. ]
     [ 0.5  0.5  0. ]
     [ 0.   1.   0. ]
     [ 0.   0.5  0.5]
     [ 0.   0.   1. ]]

    """
    if not isspmatrix_csr(A):
        raise TypeError('expected csr_matrix for A')

    if not isspmatrix_csr(C):
        raise TypeError('expected csr_matrix for C')

    # Interpolation weights are computed based on entries in A, but subject to
    # the sparsity pattern of C.  So, copy the entries of A into the
    # sparsity pattern of C.
    C = C.copy()
    C.data[:] = 1.0
    C = C.multiply(A)

    Pp = np.empty_like(A.indptr)

    amg_core.rs_direct_interpolation_pass1(A.shape[0],
                                           C.indptr, C.indices, splitting, Pp)

    nnz = Pp[-1]
    Pj = np.empty(nnz, dtype=Pp.dtype)
    Px = np.empty(nnz, dtype=A.dtype)

    amg_core.rs_direct_interpolation_pass2(A.shape[0],
                                           A.indptr, A.indices, A.data,
                                           C.indptr, C.indices, C.data,
                                           splitting,
                                           Pp, Pj, Px)

    return csr_matrix((Px, Pj, Pp))


def standard_interpolation(A, C, splitting, cost=[0]):
    """Create prolongator using standard interpolation

    Parameters
    ----------
    A : {csr_matrix}
        NxN matrix in CSR format
    C : {csr_matrix}
        Strength-of-Connection matrix
        Must have zero diagonal
    splitting : array
        C/F splitting stored in an array of length N

    Returns
    -------
    P : {csr_matrix}
        Prolongator using standard interpolation

    Examples
    --------
    >>> from pyamg.gallery import poisson
    >>> from pyamg.classical import standard_interpolation
    >>> import numpy as np
    >>> A = poisson((5,),format='csr')
    >>> splitting = np.array([1,0,1,0,1], dtype='intc')
    >>> P = standard_interpolation(A, A, splitting)
    >>> print P.todense()
    [[ 1.   0.   0. ]
     [ 0.5  0.5  0. ]
     [ 0.   1.   0. ]
     [ 0.   0.5  0.5]
     [ 0.   0.   1. ]]

    """
    if not isspmatrix_csr(A):
        raise TypeError('expected csr_matrix for A')

    if not isspmatrix_csr(C):
        raise TypeError('expected csr_matrix for C')

    # Interpolation weights are computed based on entries in A, but subject to
    # the sparsity pattern of C.  So, copy the entries of A into the
    # sparsity pattern of C.
    C = C.copy()
    C.data[:] = 1.0
    C = C.multiply(A)

    Pp = np.empty_like(A.indptr)
    amg_core.rs_standard_interpolation_pass1(A.shape[0], C.indptr,
    										 C.indices, splitting, Pp)

    nnz = Pp[-1]
    Pj = np.empty(nnz, dtype=Pp.dtype)
    Px = np.empty(nnz, dtype=A.dtype)

    amg_core.rs_standard_interpolation_pass2(A.shape[0],
                                             A.indptr, A.indices, A.data,
                                             C.indptr, C.indices, C.data,
                                             splitting,
                                             Pp, Pj, Px)
    return  csr_matrix((Px, Pj, Pp))


def trivial_interpolation(A, splitting):

    Cpts = np.where(splitting == 1)[0]
    Nc = Cpts.shape[0]
    R_rowptr = np.ones((Nc,),dtype='int32')
    return csr_matrix((np.ones((Nc,)),Cpts,R_rowptr),dtype=A.dtype).T


# TODO : add interpolation by injection, i.e. interpolate F-points from strongest connected C-point





def approximate_ideal_restriction(A, C, splitting, max_row=None, cost=[0]):

    if not isspmatrix_csr(A):
        raise TypeError('expected csr_matrix for A')

    if not isspmatrix_csr(C):
        raise TypeError('expected csr_matrix for C')

    Cpts = np.array(np.where(splitting == 1)[0], dtype='int32')
    nc = Cpts.shape[0]
    n = A.shape[0]

    # Form row pointer for R
    R_rowptr = np.empty(nc+1, dtype='int32')
    if max_row is None:
        amg_core.approx_ideal_restriction_pass1(R_rowptr, C.indptr, C.indices,
                                                C.data, Cpts, splitting)
    else:
        amg_core.approx_ideal_restriction_pass1(R_rowptr, C.indptr, C.indices,
                                                C.data, Cpts, splitting, max_row)

    # Build restriction operator
    nnz = R_rowptr[-1]
    R_colinds = np.zeros(nnz, dtype='int32')
    R_data = np.zeros(nnz, dtype=A.dtype)
    amg_core.approx_ideal_restriction_pass2(R_rowptr, R_colinds, R_data, A.indptr,
                                            A.indices, A.data, C.indptr, C.indices,
                                            C.data, Cpts, splitting)

    R = csr_matrix((R_data, R_colinds, R_rowptr), shape=[nc,n])
    R.eliminate_zeros()
    return R



