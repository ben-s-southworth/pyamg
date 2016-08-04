# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.5
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_amg_core', [dirname(__file__)])
        except ImportError:
            import _amg_core
            return _amg_core
        if fp is not None:
            try:
                _mod = imp.load_module('_amg_core', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _amg_core = swig_import_helper()
    del swig_import_helper
else:
    import _amg_core
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def signof(*args):
    """
    signof(int a) -> int
    signof(float a) -> float
    signof(double a) -> double
    """
    return _amg_core.signof(*args)

def conjugate(*args):
    """
    conjugate(float const & x) -> float
    conjugate(double const & x) -> double
    conjugate(std::complex< float > const & x) -> std::complex< float >
    conjugate(std::complex< double > const & x) -> std::complex< double >
    """
    return _amg_core.conjugate(*args)

def real(*args):
    """
    real(float const & x) -> float
    real(double const & x) -> double
    real(std::complex< float > const & x) -> float
    real(std::complex< double > const & x) -> double
    """
    return _amg_core.real(*args)

def imag(*args):
    """
    imag(float const & x) -> float
    imag(double const & x) -> double
    imag(std::complex< float > const & x) -> float
    imag(std::complex< double > const & x) -> double
    """
    return _amg_core.imag(*args)

def mynorm(*args):
    """
    mynorm(float const & x) -> float
    mynorm(double const & x) -> double
    mynorm(std::complex< float > const & x) -> float
    mynorm(std::complex< double > const & x) -> double
    """
    return _amg_core.mynorm(*args)

def mynormsq(*args):
    """
    mynormsq(float const & x) -> float
    mynormsq(double const & x) -> double
    mynormsq(std::complex< float > const & x) -> float
    mynormsq(std::complex< double > const & x) -> double
    """
    return _amg_core.mynormsq(*args)

def zero_real(*args):
    """
    zero_real(float & x) -> float
    zero_real(double & x) -> double
    zero_real(std::complex< float > & x) -> std::complex< float >
    zero_real(std::complex< double > & x) -> std::complex< double >
    """
    return _amg_core.zero_real(*args)

def zero_imag(*args):
    """
    zero_imag(float & x) -> float
    zero_imag(double & x) -> double
    zero_imag(std::complex< float > & x) -> std::complex< float >
    zero_imag(std::complex< double > & x) -> std::complex< double >
    """
    return _amg_core.zero_imag(*args)

def pinv_array(*args):
    """
    pinv_array(float [] AA, int const m, int const n, char const TransA)
    pinv_array(double [] AA, int const m, int const n, char const TransA)
    pinv_array(std::complex< float > [] AA, int const m, int const n, char const TransA)
    pinv_array(std::complex< double > [] AA, int const m, int const n, char const TransA)
    """
    return _amg_core.pinv_array(*args)

def incomplete_mat_mult_dense2sparse(*args):
    """
    incomplete_mat_mult_dense2sparse(float const [] A, float const [] B, int const [] S_rowptr, int const [] S_colinds, float [] S_data, int const m, int const d, int const n)
    incomplete_mat_mult_dense2sparse(double const [] A, double const [] B, int const [] S_rowptr, int const [] S_colinds, double [] S_data, int const m, int const d, int const n)
    """
    return _amg_core.incomplete_mat_mult_dense2sparse(*args)

def incomplete_mat_subtract(*args):
    """
    incomplete_mat_subtract(int const [] S_rowptr, int const [] S_colinds, float [] S_data, int const [] A_rowptr, int const [] A_colinds, float const [] A_data, float const tau)
    incomplete_mat_subtract(int const [] S_rowptr, int const [] S_colinds, double [] S_data, int const [] A_rowptr, int const [] A_colinds, double const [] A_data, double const tau)
    """
    return _amg_core.incomplete_mat_subtract(*args)

def maximal_independent_set_serial(num_rows, Ap, Aj, active, C, F, x):
    """maximal_independent_set_serial(int const num_rows, int const [] Ap, int const [] Aj, int const active, int const C, int const F, int [] x) -> int"""
    return _amg_core.maximal_independent_set_serial(num_rows, Ap, Aj, active, C, F, x)

def maximal_independent_set_parallel(num_rows, Ap, Aj, active, C, F, x, y, max_iters):
    """maximal_independent_set_parallel(int const num_rows, int const [] Ap, int const [] Aj, int const active, int const C, int const F, int [] x, double const [] y, int const max_iters) -> int"""
    return _amg_core.maximal_independent_set_parallel(num_rows, Ap, Aj, active, C, F, x, y, max_iters)

def maximal_independent_set_k_parallel(num_rows, Ap, Aj, k, x, y, max_iters):
    """maximal_independent_set_k_parallel(int const num_rows, int const [] Ap, int const [] Aj, int const k, int [] x, double const [] y, int const max_iters)"""
    return _amg_core.maximal_independent_set_k_parallel(num_rows, Ap, Aj, k, x, y, max_iters)

def vertex_coloring_mis(num_rows, Ap, Aj, x):
    """vertex_coloring_mis(int const num_rows, int const [] Ap, int const [] Aj, int [] x) -> int"""
    return _amg_core.vertex_coloring_mis(num_rows, Ap, Aj, x)

def vertex_coloring_jones_plassmann(num_rows, Ap, Aj, x, z):
    """vertex_coloring_jones_plassmann(int const num_rows, int const [] Ap, int const [] Aj, int [] x, double [] z) -> int"""
    return _amg_core.vertex_coloring_jones_plassmann(num_rows, Ap, Aj, x, z)

def vertex_coloring_LDF(num_rows, Ap, Aj, x, y):
    """vertex_coloring_LDF(int const num_rows, int const [] Ap, int const [] Aj, int [] x, double const [] y) -> int"""
    return _amg_core.vertex_coloring_LDF(num_rows, Ap, Aj, x, y)

def bellman_ford(*args):
    """
    bellman_ford(int const num_rows, int const [] Ap, int const [] Aj, int const [] Ax, int [] x, int [] z)
    bellman_ford(int const num_rows, int const [] Ap, int const [] Aj, float const [] Ax, float [] x, int [] z)
    bellman_ford(int const num_rows, int const [] Ap, int const [] Aj, double const [] Ax, double [] x, int [] z)
    """
    return _amg_core.bellman_ford(*args)

def lloyd_cluster(*args):
    """
    lloyd_cluster(int const num_rows, int const [] Ap, int const [] Aj, int const [] Ax, int const num_seeds, int [] x, int [] w, int [] z)
    lloyd_cluster(int const num_rows, int const [] Ap, int const [] Aj, float const [] Ax, int const num_seeds, float [] x, int [] w, int [] z)
    lloyd_cluster(int const num_rows, int const [] Ap, int const [] Aj, double const [] Ax, int const num_seeds, double [] x, int [] w, int [] z)
    """
    return _amg_core.lloyd_cluster(*args)

def breadth_first_search(Ap, Aj, seed, order, level):
    """breadth_first_search(int const [] Ap, int const [] Aj, int const seed, int [] order, int [] level)"""
    return _amg_core.breadth_first_search(Ap, Aj, seed, order, level)

def connected_components(num_nodes, Ap, Aj, components):
    """connected_components(int const num_nodes, int const [] Ap, int const [] Aj, int [] components) -> int"""
    return _amg_core.connected_components(num_nodes, Ap, Aj, components)

def apply_householders(*args):
    """
    apply_householders(float [] z, float const [] B, int const n, int const start, int const stop, int const step)
    apply_householders(double [] z, double const [] B, int const n, int const start, int const stop, int const step)
    apply_householders(std::complex< float > [] z, std::complex< float > const [] B, int const n, int const start, int const stop, int const step)
    apply_householders(std::complex< double > [] z, std::complex< double > const [] B, int const n, int const start, int const stop, int const step)
    """
    return _amg_core.apply_householders(*args)

def householder_hornerscheme(*args):
    """
    householder_hornerscheme(float [] z, float const [] B, float const [] y, int const n, int const start, int const stop, int const step)
    householder_hornerscheme(double [] z, double const [] B, double const [] y, int const n, int const start, int const stop, int const step)
    householder_hornerscheme(std::complex< float > [] z, std::complex< float > const [] B, std::complex< float > const [] y, int const n, int const start, int const stop, int const step)
    householder_hornerscheme(std::complex< double > [] z, std::complex< double > const [] B, std::complex< double > const [] y, int const n, int const start, int const stop, int const step)
    """
    return _amg_core.householder_hornerscheme(*args)

def apply_givens(*args):
    """
    apply_givens(float const [] B, float [] x, int const n, int const nrot)
    apply_givens(double const [] B, double [] x, int const n, int const nrot)
    apply_givens(std::complex< float > const [] B, std::complex< float > [] x, int const n, int const nrot)
    apply_givens(std::complex< double > const [] B, std::complex< double > [] x, int const n, int const nrot)
    """
    return _amg_core.apply_givens(*args)

def tracemin_preconditioner(*args):
    """
    tracemin_preconditioner(int const [] S_rowptr, int const [] S_colinds, float [] S_data, float const [] Aff_diag, float const [] Bc, float const tau, float const K, int const nc, int const nb)
    tracemin_preconditioner(int const [] S_rowptr, int const [] S_colinds, double [] S_data, double const [] Aff_diag, double const [] Bc, double const tau, double const K, int const nc, int const nb)
    """
    return _amg_core.tracemin_preconditioner(*args)

def gauss_seidel(*args):
    """
    gauss_seidel(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, int const row_start, int const row_stop, int const row_step)
    gauss_seidel(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, int const row_start, int const row_stop, int const row_step)
    gauss_seidel(int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, std::complex< float > [] x, std::complex< float > const [] b, int const row_start, int const row_stop, int const row_step)
    gauss_seidel(int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, std::complex< double > [] x, std::complex< double > const [] b, int const row_start, int const row_stop, int const row_step)
    """
    return _amg_core.gauss_seidel(*args)

def bsr_gauss_seidel(*args):
    """
    bsr_gauss_seidel(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, int const row_start, int const row_stop, int const row_step, int const blocksize)
    bsr_gauss_seidel(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, int const row_start, int const row_stop, int const row_step, int const blocksize)
    bsr_gauss_seidel(int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, std::complex< float > [] x, std::complex< float > const [] b, int const row_start, int const row_stop, int const row_step, int const blocksize)
    bsr_gauss_seidel(int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, std::complex< double > [] x, std::complex< double > const [] b, int const row_start, int const row_stop, int const row_step, int const blocksize)
    """
    return _amg_core.bsr_gauss_seidel(*args)

def jacobi(*args):
    """
    jacobi(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, float [] temp, int const row_start, int const row_stop, int const row_step, float const [] omega)
    jacobi(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, double [] temp, int const row_start, int const row_stop, int const row_step, double const [] omega)
    jacobi(int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, std::complex< float > [] x, std::complex< float > const [] b, std::complex< float > [] temp, int const row_start, int const row_stop, int const row_step, std::complex< float > const [] omega)
    jacobi(int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, std::complex< double > [] x, std::complex< double > const [] b, std::complex< double > [] temp, int const row_start, int const row_stop, int const row_step, std::complex< double > const [] omega)
    """
    return _amg_core.jacobi(*args)

def bsr_jacobi(*args):
    """
    bsr_jacobi(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, float [] temp, int const row_start, int const row_stop, int const row_step, int const blocksize, float const [] omega)
    bsr_jacobi(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, double [] temp, int const row_start, int const row_stop, int const row_step, int const blocksize, double const [] omega)
    bsr_jacobi(int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, std::complex< float > [] x, std::complex< float > const [] b, std::complex< float > [] temp, int const row_start, int const row_stop, int const row_step, int const blocksize, std::complex< float > const [] omega)
    bsr_jacobi(int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, std::complex< double > [] x, std::complex< double > const [] b, std::complex< double > [] temp, int const row_start, int const row_stop, int const row_step, int const blocksize, std::complex< double > const [] omega)
    """
    return _amg_core.bsr_jacobi(*args)

def gauss_seidel_indexed(*args):
    """
    gauss_seidel_indexed(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, int const [] Id, int const row_start, int const row_stop, int const row_step)
    gauss_seidel_indexed(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, int const [] Id, int const row_start, int const row_stop, int const row_step)
    gauss_seidel_indexed(int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, std::complex< float > [] x, std::complex< float > const [] b, int const [] Id, int const row_start, int const row_stop, int const row_step)
    gauss_seidel_indexed(int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, std::complex< double > [] x, std::complex< double > const [] b, int const [] Id, int const row_start, int const row_stop, int const row_step)
    """
    return _amg_core.gauss_seidel_indexed(*args)

def jacobi_ne(*args):
    """
    jacobi_ne(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, float const [] Tx, float [] temp, int const row_start, int const row_stop, int const row_step, float const [] omega)
    jacobi_ne(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, double const [] Tx, double [] temp, int const row_start, int const row_stop, int const row_step, double const [] omega)
    jacobi_ne(int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, std::complex< float > [] x, std::complex< float > const [] b, std::complex< float > const [] Tx, std::complex< float > [] temp, int const row_start, int const row_stop, int const row_step, std::complex< float > const [] omega)
    jacobi_ne(int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, std::complex< double > [] x, std::complex< double > const [] b, std::complex< double > const [] Tx, std::complex< double > [] temp, int const row_start, int const row_stop, int const row_step, std::complex< double > const [] omega)
    """
    return _amg_core.jacobi_ne(*args)

def gauss_seidel_nr(*args):
    """
    gauss_seidel_nr(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float [] z, int const col_start, int const col_stop, int const col_step, float const [] Tx, float const omega)
    gauss_seidel_nr(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double [] z, int const col_start, int const col_stop, int const col_step, double const [] Tx, double const omega)
    gauss_seidel_nr(int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, std::complex< float > [] x, std::complex< float > [] z, int const col_start, int const col_stop, int const col_step, std::complex< float > const [] Tx, float const omega)
    gauss_seidel_nr(int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, std::complex< double > [] x, std::complex< double > [] z, int const col_start, int const col_stop, int const col_step, std::complex< double > const [] Tx, double const omega)
    """
    return _amg_core.gauss_seidel_nr(*args)

def gauss_seidel_ne(*args):
    """
    gauss_seidel_ne(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, int const row_start, int const row_stop, int const row_step, float const [] Tx, float const omega)
    gauss_seidel_ne(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, int const row_start, int const row_stop, int const row_step, double const [] Tx, double const omega)
    gauss_seidel_ne(int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, std::complex< float > [] x, std::complex< float > const [] b, int const row_start, int const row_stop, int const row_step, std::complex< float > const [] Tx, float const omega)
    gauss_seidel_ne(int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, std::complex< double > [] x, std::complex< double > const [] b, int const row_start, int const row_stop, int const row_step, std::complex< double > const [] Tx, double const omega)
    """
    return _amg_core.gauss_seidel_ne(*args)

def block_jacobi(*args):
    """
    block_jacobi(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, float const [] Tx, float [] temp, int const row_start, int const row_stop, int const row_step, float const [] omega, int const blocksize)
    block_jacobi(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, double const [] Tx, double [] temp, int const row_start, int const row_stop, int const row_step, double const [] omega, int const blocksize)
    block_jacobi(int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, std::complex< float > [] x, std::complex< float > const [] b, std::complex< float > const [] Tx, std::complex< float > [] temp, int const row_start, int const row_stop, int const row_step, std::complex< float > const [] omega, int const blocksize)
    block_jacobi(int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, std::complex< double > [] x, std::complex< double > const [] b, std::complex< double > const [] Tx, std::complex< double > [] temp, int const row_start, int const row_stop, int const row_step, std::complex< double > const [] omega, int const blocksize)
    """
    return _amg_core.block_jacobi(*args)

def block_gauss_seidel(*args):
    """
    block_gauss_seidel(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, float const [] Tx, int const row_start, int const row_stop, int const row_step, int const blocksize)
    block_gauss_seidel(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, double const [] Tx, int const row_start, int const row_stop, int const row_step, int const blocksize)
    block_gauss_seidel(int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, std::complex< float > [] x, std::complex< float > const [] b, std::complex< float > const [] Tx, int const row_start, int const row_stop, int const row_step, int const blocksize)
    block_gauss_seidel(int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, std::complex< double > [] x, std::complex< double > const [] b, std::complex< double > const [] Tx, int const row_start, int const row_stop, int const row_step, int const blocksize)
    """
    return _amg_core.block_gauss_seidel(*args)

def extract_subblocks(*args):
    """
    extract_subblocks(int const [] Ap, int const [] Aj, float const [] Ax, float [] Tx, int const [] Tp, int const [] Sj, int const [] Sp, int const nsdomains, int const nrows)
    extract_subblocks(int const [] Ap, int const [] Aj, double const [] Ax, double [] Tx, int const [] Tp, int const [] Sj, int const [] Sp, int const nsdomains, int const nrows)
    extract_subblocks(int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, std::complex< float > [] Tx, int const [] Tp, int const [] Sj, int const [] Sp, int const nsdomains, int const nrows)
    extract_subblocks(int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, std::complex< double > [] Tx, int const [] Tp, int const [] Sj, int const [] Sp, int const nsdomains, int const nrows)
    """
    return _amg_core.extract_subblocks(*args)

def overlapping_schwarz_csr(*args):
    """
    overlapping_schwarz_csr(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, float const [] Tx, int const [] Tp, int const [] Sj, int const [] Sp, int nsdomains, int nrows, int row_start, int row_stop, int row_step)
    overlapping_schwarz_csr(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, double const [] Tx, int const [] Tp, int const [] Sj, int const [] Sp, int nsdomains, int nrows, int row_start, int row_stop, int row_step)
    overlapping_schwarz_csr(int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, std::complex< float > [] x, std::complex< float > const [] b, std::complex< float > const [] Tx, int const [] Tp, int const [] Sj, int const [] Sp, int nsdomains, int nrows, int row_start, int row_stop, int row_step)
    overlapping_schwarz_csr(int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, std::complex< double > [] x, std::complex< double > const [] b, std::complex< double > const [] Tx, int const [] Tp, int const [] Sj, int const [] Sp, int nsdomains, int nrows, int row_start, int row_stop, int row_step)
    """
    return _amg_core.overlapping_schwarz_csr(*args)

def symmetric_strength_of_connection(*args):
    """
    symmetric_strength_of_connection(int const n_row, float const theta, int const [] Ap, int const [] Aj, float const [] Ax, int [] Sp, int [] Sj, float [] Sx)
    symmetric_strength_of_connection(int const n_row, double const theta, int const [] Ap, int const [] Aj, double const [] Ax, int [] Sp, int [] Sj, double [] Sx)
    symmetric_strength_of_connection(int const n_row, float const theta, int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, int [] Sp, int [] Sj, std::complex< float > [] Sx)
    symmetric_strength_of_connection(int const n_row, double const theta, int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, int [] Sp, int [] Sj, std::complex< double > [] Sx)
    """
    return _amg_core.symmetric_strength_of_connection(*args)

def naive_aggregation(n_row, Ap, Aj, x, y):
    """naive_aggregation(int const n_row, int const [] Ap, int const [] Aj, int [] x, int [] y) -> int"""
    return _amg_core.naive_aggregation(n_row, Ap, Aj, x, y)

def standard_aggregation(n_row, Ap, Aj, x, y):
    """standard_aggregation(int const n_row, int const [] Ap, int const [] Aj, int [] x, int [] y) -> int"""
    return _amg_core.standard_aggregation(n_row, Ap, Aj, x, y)

def fit_candidates(*args):
    """
    fit_candidates(int const n_row, int const n_col, int const K1, int const K2, int const [] Ap, int const [] Ai, float [] Ax, float const [] B, float [] R, float const tol)
    fit_candidates(int const n_row, int const n_col, int const K1, int const K2, int const [] Ap, int const [] Ai, double [] Ax, double const [] B, double [] R, double const tol)
    fit_candidates(int const n_row, int const n_col, int const K1, int const K2, int const [] Ap, int const [] Ai, std::complex< float > [] Ax, std::complex< float > const [] B, std::complex< float > [] R, float const tol)
    fit_candidates(int const n_row, int const n_col, int const K1, int const K2, int const [] Ap, int const [] Ai, std::complex< double > [] Ax, std::complex< double > const [] B, std::complex< double > [] R, double const tol)
    """
    return _amg_core.fit_candidates(*args)

def satisfy_constraints_helper(*args):
    """
    satisfy_constraints_helper(int const RowsPerBlock, int const ColsPerBlock, int const num_block_rows, int const NullDim, float const [] x, float const [] y, float const [] z, int const [] Sp, int const [] Sj, float [] Sx)
    satisfy_constraints_helper(int const RowsPerBlock, int const ColsPerBlock, int const num_block_rows, int const NullDim, double const [] x, double const [] y, double const [] z, int const [] Sp, int const [] Sj, double [] Sx)
    satisfy_constraints_helper(int const RowsPerBlock, int const ColsPerBlock, int const num_block_rows, int const NullDim, std::complex< float > const [] x, std::complex< float > const [] y, std::complex< float > const [] z, int const [] Sp, int const [] Sj, std::complex< float > [] Sx)
    satisfy_constraints_helper(int const RowsPerBlock, int const ColsPerBlock, int const num_block_rows, int const NullDim, std::complex< double > const [] x, std::complex< double > const [] y, std::complex< double > const [] z, int const [] Sp, int const [] Sj, std::complex< double > [] Sx)
    """
    return _amg_core.satisfy_constraints_helper(*args)

def calc_BtB(*args):
    """
    calc_BtB(int const NullDim, int const Nnodes, int const ColsPerBlock, float const [] b, int const BsqCols, float [] x, int const [] Sp, int const [] Sj)
    calc_BtB(int const NullDim, int const Nnodes, int const ColsPerBlock, double const [] b, int const BsqCols, double [] x, int const [] Sp, int const [] Sj)
    calc_BtB(int const NullDim, int const Nnodes, int const ColsPerBlock, std::complex< float > const [] b, int const BsqCols, std::complex< float > [] x, int const [] Sp, int const [] Sj)
    calc_BtB(int const NullDim, int const Nnodes, int const ColsPerBlock, std::complex< double > const [] b, int const BsqCols, std::complex< double > [] x, int const [] Sp, int const [] Sj)
    """
    return _amg_core.calc_BtB(*args)

def incomplete_mat_mult_bsr(*args):
    """
    incomplete_mat_mult_bsr(int const [] Ap, int const [] Aj, float const [] Ax, int const [] Bp, int const [] Bj, float const [] Bx, int const [] Sp, int const [] Sj, float [] Sx, int const n_brow, int const n_bcol, int const brow_A, int const bcol_A, int const bcol_B)
    incomplete_mat_mult_bsr(int const [] Ap, int const [] Aj, double const [] Ax, int const [] Bp, int const [] Bj, double const [] Bx, int const [] Sp, int const [] Sj, double [] Sx, int const n_brow, int const n_bcol, int const brow_A, int const bcol_A, int const bcol_B)
    incomplete_mat_mult_bsr(int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, int const [] Bp, int const [] Bj, std::complex< float > const [] Bx, int const [] Sp, int const [] Sj, std::complex< float > [] Sx, int const n_brow, int const n_bcol, int const brow_A, int const bcol_A, int const bcol_B)
    incomplete_mat_mult_bsr(int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, int const [] Bp, int const [] Bj, std::complex< double > const [] Bx, int const [] Sp, int const [] Sj, std::complex< double > [] Sx, int const n_brow, int const n_bcol, int const brow_A, int const bcol_A, int const bcol_B)
    """
    return _amg_core.incomplete_mat_mult_bsr(*args)

def truncate_rows_csr(*args):
    """
    truncate_rows_csr(int const n_row, int const k, int const [] Sp, int [] Sj, float [] Sx)
    truncate_rows_csr(int const n_row, int const k, int const [] Sp, int [] Sj, double [] Sx)
    truncate_rows_csr(int const n_row, int const k, int const [] Sp, int [] Sj, std::complex< float > [] Sx)
    truncate_rows_csr(int const n_row, int const k, int const [] Sp, int [] Sj, std::complex< double > [] Sx)
    """
    return _amg_core.truncate_rows_csr(*args)

_amg_core.F_NODE_swigconstant(_amg_core)
F_NODE = _amg_core.F_NODE

_amg_core.C_NODE_swigconstant(_amg_core)
C_NODE = _amg_core.C_NODE

_amg_core.U_NODE_swigconstant(_amg_core)
U_NODE = _amg_core.U_NODE

def classical_strength_of_connection(*args):
    """
    classical_strength_of_connection(int const n_row, float const theta, int const [] Ap, int const [] Aj, float const [] Ax, int [] Sp, int [] Sj, float [] Sx)
    classical_strength_of_connection(int const n_row, double const theta, int const [] Ap, int const [] Aj, double const [] Ax, int [] Sp, int [] Sj, double [] Sx)
    classical_strength_of_connection(int const n_row, float const theta, int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, int [] Sp, int [] Sj, std::complex< float > [] Sx)
    classical_strength_of_connection(int const n_row, double const theta, int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, int [] Sp, int [] Sj, std::complex< double > [] Sx)
    """
    return _amg_core.classical_strength_of_connection(*args)

def maximum_row_value(*args):
    """
    maximum_row_value(int const n_row, float [] x, int const [] Ap, int const [] Aj, float const [] Ax)
    maximum_row_value(int const n_row, double [] x, int const [] Ap, int const [] Aj, double const [] Ax)
    maximum_row_value(int const n_row, std::complex< float > [] x, int const [] Ap, int const [] Aj, std::complex< float > const [] Ax)
    maximum_row_value(int const n_row, std::complex< double > [] x, int const [] Ap, int const [] Aj, std::complex< double > const [] Ax)
    """
    return _amg_core.maximum_row_value(*args)

def rs_cf_splitting(n_nodes, Sp, Sj, Tp, Tj, splitting):
    """rs_cf_splitting(int const n_nodes, int const [] Sp, int const [] Sj, int const [] Tp, int const [] Tj, int [] splitting)"""
    return _amg_core.rs_cf_splitting(n_nodes, Sp, Sj, Tp, Tj, splitting)

def cljp_naive_splitting(n, Sp, Sj, Tp, Tj, splitting, colorflag):
    """cljp_naive_splitting(int const n, int const [] Sp, int const [] Sj, int const [] Tp, int const [] Tj, int [] splitting, int const colorflag)"""
    return _amg_core.cljp_naive_splitting(n, Sp, Sj, Tp, Tj, splitting, colorflag)

def rs_direct_interpolation_pass1(n_nodes, Sp, Sj, splitting, Bp):
    """rs_direct_interpolation_pass1(int const n_nodes, int const [] Sp, int const [] Sj, int const [] splitting, int [] Bp)"""
    return _amg_core.rs_direct_interpolation_pass1(n_nodes, Sp, Sj, splitting, Bp)

def rs_direct_interpolation_pass2(*args):
    """
    rs_direct_interpolation_pass2(int const n_nodes, int const [] Ap, int const [] Aj, float const [] Ax, int const [] Sp, int const [] Sj, float const [] Sx, int const [] splitting, int const [] Bp, int [] Bj, float [] Bx)
    rs_direct_interpolation_pass2(int const n_nodes, int const [] Ap, int const [] Aj, double const [] Ax, int const [] Sp, int const [] Sj, double const [] Sx, int const [] splitting, int const [] Bp, int [] Bj, double [] Bx)
    """
    return _amg_core.rs_direct_interpolation_pass2(*args)

def cr_helper(*args):
    """
    cr_helper(int const [] A_rowptr, int const [] A_colinds, float const [] B, float [] e, int [] indices, int [] splitting, float [] gamma, float const thetacs, float [] cost)
    cr_helper(int const [] A_rowptr, int const [] A_colinds, double const [] B, double [] e, int [] indices, int [] splitting, double [] gamma, double const thetacs, double [] cost)
    """
    return _amg_core.cr_helper(*args)

def apply_distance_filter(*args):
    """
    apply_distance_filter(int const n_row, float const epsilon, int const [] Sp, int const [] Sj, float [] Sx)
    apply_distance_filter(int const n_row, double const epsilon, int const [] Sp, int const [] Sj, double [] Sx)
    """
    return _amg_core.apply_distance_filter(*args)

def apply_absolute_distance_filter(*args):
    """
    apply_absolute_distance_filter(int const n_row, float const epsilon, int const [] Sp, int const [] Sj, float [] Sx)
    apply_absolute_distance_filter(int const n_row, double const epsilon, int const [] Sp, int const [] Sj, double [] Sx)
    """
    return _amg_core.apply_absolute_distance_filter(*args)

def min_blocks(*args):
    """
    min_blocks(int const n_blocks, int const blocksize, float const [] Sx, float [] Tx)
    min_blocks(int const n_blocks, int const blocksize, double const [] Sx, double [] Tx)
    """
    return _amg_core.min_blocks(*args)

def evolution_strength_helper(*args):
    """
    evolution_strength_helper(float [] Sx, int const [] Sp, int const [] Sj, int const nrows, float const [] x, float const [] y, float const [] b, int const BDBCols, int const NullDim, float const tol)
    evolution_strength_helper(double [] Sx, int const [] Sp, int const [] Sj, int const nrows, double const [] x, double const [] y, double const [] b, int const BDBCols, int const NullDim, double const tol)
    evolution_strength_helper(std::complex< float > [] Sx, int const [] Sp, int const [] Sj, int const nrows, std::complex< float > const [] x, std::complex< float > const [] y, std::complex< float > const [] b, int const BDBCols, int const NullDim, float const tol)
    evolution_strength_helper(std::complex< double > [] Sx, int const [] Sp, int const [] Sj, int const nrows, std::complex< double > const [] x, std::complex< double > const [] y, std::complex< double > const [] b, int const BDBCols, int const NullDim, double const tol)
    """
    return _amg_core.evolution_strength_helper(*args)

def incomplete_mat_mult_csr(*args):
    """
    incomplete_mat_mult_csr(int const [] Ap, int const [] Aj, float const [] Ax, int const [] Bp, int const [] Bj, float const [] Bx, int const [] Sp, int const [] Sj, float [] Sx, int const num_rows)
    incomplete_mat_mult_csr(int const [] Ap, int const [] Aj, double const [] Ax, int const [] Bp, int const [] Bj, double const [] Bx, int const [] Sp, int const [] Sj, double [] Sx, int const num_rows)
    incomplete_mat_mult_csr(int const [] Ap, int const [] Aj, std::complex< float > const [] Ax, int const [] Bp, int const [] Bj, std::complex< float > const [] Bx, int const [] Sp, int const [] Sj, std::complex< float > [] Sx, int const num_rows)
    incomplete_mat_mult_csr(int const [] Ap, int const [] Aj, std::complex< double > const [] Ax, int const [] Bp, int const [] Bj, std::complex< double > const [] Bx, int const [] Sp, int const [] Sj, std::complex< double > [] Sx, int const num_rows)
    """
    return _amg_core.incomplete_mat_mult_csr(*args)
# This file is compatible with both classic and new-style classes.


