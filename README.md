# Spectral response of a nonlinear Jaynes-Cummings model

Here we will show the numerical simulation of the system, and a comparison with the analytical¹ expressions

The full-Hamiltonian in consideration to simulate is defined as

$$


\hat H^{D}_{\texttt{JC}}\!=\!\frac{\hbar\omega_{c}}{2}(\hat{A}^{\dagger}\hat{A}+\hat{A} \hat{A}^{\dagger}) + \frac{\hbar\omega_a}{2}\hat{\sigma}_{z}\!-\mathrm{i}\frac{\hbar\Omega_{0}}{2}(\hat{A}\hat{\sigma}_{+}\!-\!\hat{A}^{\dagger} \hat{\sigma}_{-}),



$$

where $\hat{A} = \hat{a}f(\hat{n})$ the new _deformed_ annihilation operator, that uses the _deformation function_ $f^2(\hat{n})=1+\chi\hat{n}$, for some parameter $\chi$ that acts a deformation strength.

Algorithmically, we define the deformed operators, then the Hamiltonian is obtained to obtain a evolution operator. This evolution operator is used to translate the operators in the two-time correlation function, and then the numerical integration of this correlation function is performed. The result is the frequency spectrum from $0$ to $t_{\mathrm{obs}}$.

_____

¹In a strict way, we do a semi-analytical approach, since we obtain the analytical two-time correlation functions, and then we numerically integrate this expression in order to obtain the frequency-dependent spectrum at time $t$.

---

---

Authors: L. Medina-Dozal, A.R. Urzúa , D. Aranda-Lozano, Carlos A.  Gonz ález-Gutiérrez , J. Récamier , and R. Rom án-Ancheyta.

Code developer: A.R. Urzúa

 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
