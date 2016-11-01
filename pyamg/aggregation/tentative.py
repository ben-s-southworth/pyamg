"""Tentative prolongator"""

__docformat__ = "restructuredtext en"

import numpy as np
from scipy.sparse import isspmatrix_csr, bsr_matrix, csr_matrix
from pyamg import amg_core

__all__ = ['fit_candidates']


def fit_candidates(AggOp, B, tol=1e-10, cost=[0.0]):
    """Fit near-nullspace candidates to form the tentative prolongator

    Parameters
    ----------
    AggOp : csr_matrix
        Describes the sparsity pattern of the tentative prolongator.
        Has dimension (#blocks, #aggregates)
    B : array
        The near-nullspace candidates stored in column-wise fashion.
        Has dimension (#blocks * blocksize, #candidates)
    tol : scalar
        Threshold for eliminating local basis functions.
        If after orthogonalization a local basis function Q[:, j] is small,
        i.e. ||Q[:, j]|| < tol, then Q[:, j] is set to zero.
    cost : {list containing one scalar}
        cost[0] is incremented to reflect a FLOP estimate for this function

    Returns
    -------
    (T, Bc) : (bsr_matrix, array)
        The tentative prolongator T is a sparse block matrix with dimensions
        (#blocks * blocksize, #aggregates * #candidates) formed by dense blocks
        of size (blocksize, #candidates).  The coarse level candidates are
        stored in Bc which has dimensions (#aggregates * #candidates,
        #candidates).

    See Also
    --------
    amg_core.fit_candidates

    Notes
    -----
        Assuming that each row of AggOp contains exactly one non-zero entry,
        i.e. all unknowns belong to an aggregate, then T and Bc satisfy the
        relationship B = T*Bc.  In other words, the near-nullspace candidates
        are represented exactly by the tentative prolongator.

        If AggOp contains rows with no non-zero entries, then the range of the
        tentative prolongator will not include those degrees of freedom. This
        situation is illustrated in the examples below.

    References
    ----------
    .. [1] Vanek, P. and Mandel, J. and Brezina, M.,
       "Algebraic Multigrid by Smoothed Aggregation for
       Second and Fourth Order Elliptic Problems",
       Computing, vol. 56, no. 3, pp. 179--196, 1996.
       http://citeseer.ist.psu.edu/vanek96algebraic.html


    Examples
    --------
    >>> from scipy.sparse import csr_matrix
    >>> from pyamg.aggregation.tentative import fit_candidates
    >>> # four nodes divided into two aggregates
    ... AggOp = csr_matrix( [[1, 0],
    ...                      [1, 0],
    ...                      [0, 1],
    ...                      [0, 1]] )
    >>> # B contains one candidate, the constant vector
    ... B = [[1],
    ...      [1],
    ...      [1],
    ...      [1]]
    >>> T, Bc = fit_candidates(AggOp, B)
    >>> T.todense()
    matrix([[ 0.70710678,  0.        ],
            [ 0.70710678,  0.        ],
            [ 0.        ,  0.70710678],
            [ 0.        ,  0.70710678]])
    >>> Bc
    array([[ 1.41421356],
           [ 1.41421356]])
    >>> # Two candidates, the constant vector and a linear function
    ... B = [[1, 0],
    ...      [1, 1],
    ...      [1, 2],
    ...      [1, 3]]
    >>> T, Bc = fit_candidates(AggOp, B)
    >>> T.todense()
    matrix([[ 0.70710678, -0.70710678,  0.        ,  0.        ],
            [ 0.70710678,  0.70710678,  0.        ,  0.        ],
            [ 0.        ,  0.        ,  0.70710678, -0.70710678],
            [ 0.        ,  0.        ,  0.70710678,  0.70710678]])
    >>> Bc
    array([[ 1.41421356,  0.70710678],
           [ 0.        ,  0.70710678],
           [ 1.41421356,  3.53553391],
           [ 0.        ,  0.70710678]])
    >>> # aggregation excludes the third node
    ... AggOp = csr_matrix( [[1, 0],
    ...                      [1, 0],
    ...                      [0, 0],
    ...                      [0, 1]] )
    >>> B = [[1],
    ...      [1],
    ...      [1],
    ...      [1]]
    >>> T, Bc = fit_candidates(AggOp, B)
    >>> T.todense()
    matrix([[ 0.70710678,  0.        ],
            [ 0.70710678,  0.        ],
            [ 0.        ,  0.        ],
            [ 0.        ,  1.        ]])
    >>> Bc
    array([[ 1.41421356],
           [ 1.        ]])

    """
    if not isspmatrix_csr(AggOp):
        raise TypeError('expected csr_matrix for argument AggOp')

    B = np.asarray(B)
    if B.dtype not in ['float32', 'float64', 'complex64', 'complex128']:
        B = np.asarray(B, dtype='float64')

    if len(B.shape) != 2:
        raise ValueError('expected 2d array for argument B')

    if B.shape[0] % AggOp.shape[0] != 0:
        raise ValueError('dimensions of AggOp %s and B %s are \
                          incompatible' % (AggOp.shape, B.shape))

    N_fine, N_coarse = AggOp.shape

    K1 = int(B.shape[0] / N_fine)  # dof per supernode (e.g. 3 for 3d vectors)
    K2 = B.shape[1]                # candidates

    # the first two dimensions of Bc and Tx are collapsed later
    Bc = np.empty((N_coarse, K2, K2), dtype=B.dtype)  # coarse candidates
    Tx = np.empty((AggOp.nnz, K1, K2), dtype=B.dtype)  # BSR data array

    AggOp_csc = AggOp.tocsc()

    fn = amg_core.fit_candidates
    fn(N_fine, N_coarse, K1, K2,
       AggOp_csc.indptr, AggOp_csc.indices, Tx.ravel(),
       B.ravel(), Bc.ravel(), tol)

    # TODO replace with BSC matrix here
    T = bsr_matrix((Tx.swapaxes(1, 2).copy(), AggOp_csc.indices,
                    AggOp_csc.indptr), shape=(K2*N_coarse, K1*N_fine))
    T = T.T.tobsr()
    Bc = Bc.reshape(-1, K2)

    cost[0] += 2.0*B.shape[1]*B.shape[1]*float(T.shape[0])

    return T, Bc
