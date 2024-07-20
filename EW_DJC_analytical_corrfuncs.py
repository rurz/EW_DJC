import numpy as np
import math

def Delta(omega_a, omega_c):
    return omega_a - omega_c

def Omega(Omega_0, n):
    return Omega_0 * np.sqrt(n + 1)

def fn(chi, n):
    return np.sqrt(1 + chi * n)

def Delta_n(omega_a, omega_c, chi, n):
    return Delta(omega_a, omega_c) - 2 * chi * omega_c * (n + 1)

def Omega_n(Omega_0, chi, n):
    return Omega(Omega_0, n) * fn(chi, n + 1)

def En0(omega_c, chi, n):
    return omega_c * (1 + chi * (2 * n + 1))

def phi(omega_a, omega_c, Omega_0, chi, n):
    return np.sqrt(Delta_n(omega_a, omega_c, chi, n) ** 2 + Omega_n(Omega_0, chi, n) ** 2)

def phi_p(omega_a, omega_c, Omega_0, chi, n):
    return phi(omega_a, omega_c, Omega_0, chi, n) + phi(omega_a, omega_c, Omega_0, chi, n - 1)

def phi_m(omega_a, omega_c, Omega_0, chi, n):
    return phi(omega_a, omega_c, Omega_0, chi, n) - phi(omega_a, omega_c, Omega_0, chi, n - 1)

########

def Gcorr_n(omega_a, omega_c, Omega_0, chi, n, t_1, t_2):
    return ((1/8.0) * np.exp(1j * En0(omega_c, chi, n) * (t_1 - t_2)) *
            np.exp(-(1j/2.0) * (phi_m(omega_a, omega_c, Omega_0, chi, n) * t_2 + phi_p(omega_a, omega_c, Omega_0, chi, n) * t_1)) * 
            (np.exp(1j * phi(omega_a, omega_c, Omega_0, chi, n) * t_1) * (1 + Delta_n(omega_a, omega_c, chi, n)/phi(omega_a, omega_c, Omega_0, chi, n)) + (1 - Delta_n(omega_a, omega_c, chi, n)/phi(omega_a, omega_c, Omega_0, chi, n))) * 
            ((1 + Delta_n(omega_a, omega_c, chi, n)/phi(omega_a, omega_c, Omega_0, chi, n)) + np.exp(1j * phi(omega_a, omega_c, Omega_0, chi, n) * t_2) * (1 - Delta_n(omega_a, omega_c, chi, n)/phi(omega_a, omega_c, Omega_0, chi, n))) * 
            (np.exp(1j * phi(omega_a, omega_c, Omega_0, chi, n - 1) * (t_1 - t_2)) * (1 + Delta_n(omega_a, omega_c, chi, n - 1)/phi(omega_a, omega_c, Omega_0, chi, n - 1)) + (1 - Delta_n(omega_a, omega_c, chi, n - 1)/phi(omega_a, omega_c, Omega_0, chi, n - 1)))
    )

def Gcorr_a(omega_a, omega_c, Omega_0, chi, alpha, t_1, t_2):
    return sum(np.exp(-(abs(alpha) ** 2)/2.0) * np.complex128([(alpha ** k) * Gcorr_n(omega_a, omega_c, Omega_0, chi, k, t_1, t_2)/math.sqrt(np.math.factorial(k)) for k in range(0, 35)]))
