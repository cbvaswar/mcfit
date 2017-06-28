"""
======================
Cosmology applications
======================
"""

from .mcfit import mcfit
from . import kernels
from numpy import pi, real_if_close


__all__ = ['P2xi', 'xi2P', 'DoubleSphericalBessel', 'TophatVar', 'GaussVar', 'ExcursionSet']


class P2xi(mcfit):
    """
    Power spectrum to correlation function
    """
    def __init__(self, k, l=0, q=1.5, N=None, lowring=True):
        self.l = l
        UK = kernels.Mellin_SphericalBesselJ(l)
        prefac = real_if_close(1j**l) * k**3 / (2*pi)**1.5
        postfac = 1
        mcfit.__init__(self, k, UK, q, N=N, lowring=lowring, prefac=prefac, postfac=postfac)


class xi2P(mcfit):
    """
    Correlation function to power spectrum
    Also radial profile to its Fourier transform
    """
    def __init__(self, r, l=0, q=1.5, N=None, lowring=True):
        self.l = l
        UK = kernels.Mellin_SphericalBesselJ(l)
        prefac = r**3
        postfac = (2*pi)**1.5 / real_if_close(1j**l)
        mcfit.__init__(self, r, UK, q, N=N, lowring=lowring, prefac=prefac, postfac=postfac)


class DoubleSphericalBessel(mcfit):
    r"""
    .. math:: G(y_1; \alpha) \equiv G(y_1, y_2=\alpha y_1)
                = \int_0^\infty F(x) j_{l_1}(xy_1) j_{l_2}(xy_2) \,x^2\d x

    Parameters
    ----------
    alpha : float
        y2 / y1
    l : int, optional
        default to 0
    l1 : int, optional
        default to l
    l2 : int, optional
        default to l
    """
    def __init__(self, x, alpha, l=0, l1=None, l2=None, q=1.5, N=None, lowring=True):
        self.alpha = alpha
        self.l1 = l1 if l1 is not None else l
        self.l2 = l2 if l2 is not None else l
        UK = kernels.Mellin_DoubleSphericalBesselJ(alpha, l1, l2)
        prefac = x**3
        postfac = 1
        mcfit.__init__(self, x, UK, q, N=N, lowring=lowring, prefac=prefac, postfac=postfac)


class TophatVar(mcfit):
    """
    Variance in a top-hat window
    """
    def __init__(self, k, q=1.5, N=None, lowring=True):
        UK = kernels.Mellin_TophatSq(3)
        prefac = k**3 / (2 * pi**2)
        postfac = 1
        mcfit.__init__(self, k, UK, q, N=N, lowring=lowring, prefac=prefac, postfac=postfac)


class GaussVar(mcfit):
    """
    Variance in a Gaussian window
    """
    def __init__(self, k, q=1.5, N=None, lowring=True):
        UK = kernels.Mellin_GaussSq()
        prefac = k**3 / (2 * pi**2)
        postfac = 1
        mcfit.__init__(self, k, UK, q, N=N, lowring=lowring, prefac=prefac, postfac=postfac)


class ExcursionSet(mcfit):
    """
    Excursion set trajectory
    BCEK 91 model
    """
    def __init__(self, k, q=0, N=None, lowring=True):
        raise NotImplementedError
