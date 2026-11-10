# 🌌 Astrobiology-Today: High-Precision Orbital Dynamics & Planetary Defense Framework

---

## 📌 Executive Overview & Parent Framework Architecture

**Astrobiology-Today** is the primary open-science scientific ecosystem and umbrella computational framework dedicated to high-precision celestial mechanics, planetary defense modeling, non-gravitational thermal perturbation mapping, and interstellar interloper kinematics.

This parent repository establishes the foundational mathematical algorithms, numerical ODE integrators, astrometric ephemeris pipelines, and physical perturbation tensors from which specialized research sub-repositories derive (including the Apophis 2029 close approach simulation suite and the 3I/ATLAS interstellar trajectory validation platform).

---

## 🛡️ Intellectual Property, Author Attribution & Open-Science Notice

> **IMPORTANT NOTICE FOR REVIEWERS, RESEARCHERS & REPOSITORIES**  
> This software suite and underlying mathematical framework were independently formulated and developed by **Rene Sagal Andrade**.
>
> * **Author:** Rene Sagal Andrade (System Architect & Astro-aerospace Analyst; University College London Alumnus)
> * **Primary Contact:** `sagal233rene@outlook.com` / `sagal1031rene@gmail.com`
> * **GitHub Repository:** [https://github.com/sagal1031rene-coder/astrobiology-today](https://github.com/sagal1031rene-coder/astrobiology-today)
> * **Licensing:** Licensed under the **MIT License**.
>
> **Anti-Plagiarism & Priority Attribution Clause:**  
> All mathematical formulations, custom adaptive integration routines, state-vector contingency arrays, and trajectory visualization pipelines are open for academic evaluation and reproducibility under Open Science standards. **Unauthorized re-licensing, distribution without proper attribution, or publication of this computational architecture under altered authorship constitutes academic misconduct**. Commit histories, time-stamped pushes, and cryptographic signatures within this ecosystem serve as verifiable proof of primary intellectual priority.

---

## 🔬 Core Scientific Domains & Derived Research Modules

### 1. Near-Earth Asteroid Flyby Dynamics: (99942) Apophis 2029
*Derived Module / Sub-system:* `Apophis 2029 Flyby Engine`

* **Deep Gravitational Flyby:** Models the April 13, 2029 close encounter using the implicit 15th-order Gauss-Radau adaptive integrator (**IAS15** engine) within **REBOUND** ($\tau = 10^{-12}$), resolving an absolute nominal geocentric perigee radius of **36,082.12 km** (standard Newtonian + Yarkovsky coupling) and **38,011.82 km** (pure 3-body baseline), passing deep beneath the **35,786 km** altitude operational geosynchronous satellite boundary.
* **Orbital Class Mutation (Aten $\rightarrow$ Apollo):** Quantifies planetary tidal torque that induces a permanent expansion of the heliocentric semi-major axis from $a_{\text{pre}} = 0.9241\text{ AU}$ up to $a_{\text{post}} = 0.9535\text{ AU}$ ($\Delta a = +0.0294\text{ AU}$), shifting Apophis permanently into the Apollo orbital family.
* **Tidal Strain & Eccentricity Peak:** Captures a sharp non-monotonic eccentricity peak of $e_{\text{peak}} = 0.1960$ precisely at the perigee vertex before stabilizing post-encounter at $e_{\text{post}} \approx 0.1812$.
* **Sub-Meter Yarkovsky Thermal Drift:** Injects a calibrated diurnal transverse thermal acceleration tensor ($A_2$ parameter), resolving a node convergence vertex at $t = 14.73\text{ days}$ post-initialization and isolating a net cumulative Yarkovsky spatial displacement of **$\Delta r_{\text{Yark}} = 0.00018\text{ km}$ (18.0 cm)**.

### 2. Interstellar Hyperbolic Kinematics: Comet 3I/ATLAS
*Derived Repository:* [https://github.com/sagal1031rene-coder/3iatlas-orbit-model](https://github.com/sagal1031rene-coder/3iatlas-orbit-model)

* **Hyperbolic Orbit Validation:** Validates the extreme unbound trajectory ($e = 6.1414$, $q = 1.3565\text{ AU}$, $v_\infty = 64.04\text{ km s}^{-1}$, gravitational deflection $\delta = 18.78^\circ$) using an adaptive RK45 integration scheme ($\text{TOL} = 10^{-9}$, $h_{\text{min}} \approx 1.2 \times 10^2\text{ s}$).
* **Cometary Non-Gravitational Accelerations:** Couples solar radiation pressure ($\text{AMR} = 1.05 \times 10^{-6}\text{ m}^2\text{ kg}^{-1}$) with an 8° offset asymmetric outgassing thrust inside $2.5\text{ AU}$, resolving a maximum perturbation of $6.48 \times 10^{-12}\text{ m s}^{-2}$ and an integrated spatial deflection of **236.36 meters**.
* **50-Myr Retrospective Galactic Origin:** Performs backward numerical integration under a multi-component galactic potential, confirming zero close stellar encounters within 50 million years and proving 3I/ATLAS is a pristine interstellar interloper escaping toward the celestial coordinates of Lyra.

---

## 🧮 Mathematical Engine & Unified Equations of Motion

### A. Heliocentric Multi-Body Gravitational & Thermal Acceleration
$$\frac{d\vec{v}_{\text{ast}}}{dt} = - \frac{G M_\odot}{r^3} \vec{r} + \sum_{j \in \{\text{Earth, Moon, Planets}\}} G M_j \left( \frac{\vec{r}_j - \vec{r}}{|\vec{r}_j - \vec{r}|^3} - \frac{\vec{r}_j}{r_j^3} \right) + \vec{a}_{\text{Yark}} + \vec{a}_{\text{comet}}$$

### B. Transverse Yarkovsky Thermal Acceleration Tensor
$$\vec{a}_{\text{Yark}} = A_2 \left( \frac{r_0}{r} \right)^\alpha \hat{t}$$
where $r_0 = 1.0\text{ AU}$, $\alpha = 2.0$, $\hat{t}$ is the heliocentric transverse unit vector, and $A_2$ parameters are calibrated against surface thermal inertia ($\Gamma$), bulk density ($\rho$), and spin axis obliquity ($\gamma$).

### C. Cometary Solar Radiation Pressure & Outgassing Vector
$$\vec{a}_{\text{rad}} = \frac{S_0 \cdot \text{AMR}}{c \cdot r_{\text{AU}}^2} \hat{r}, \quad \vec{a}_{\text{thrust}} = F_{\text{outgassing}}(r) \cdot \mathbf{R}(\theta_{\text{offset}}) \hat{r}$$

---

## ⚙️ Hybrid Architecture & Offline Contingency Framework

To prevent reliance on external API availability and guarantee 100% computational reproducibility across offline or cloud environment executions, the system utilizes a dual-layer data pipeline:

1. **Primary Interface:** Live orbital state retrieval via `astroquery.jplhorizons`.
2. **Offline Fallback Interface:** Localized JSON contingency arrays (`data/initial_state_vectors.json`) containing high-precision pre-cached ephemerides.

---

## 💻 Quick Start & Environment Setup

### 1. Repository Installation
```bash
git clone https://github.com/sagal1031rene-coder/astrobiology-today.git
cd astrobiology-today
pip install -r requirements.txt
```

### 2. Execution Modes
* **Full Simulation Run:**
  ```bash
  python main_simulation.py
  ```
* **Generate Visualization Figures:**
  ```bash
  python visualize_simulation.py
  ```

---

## 📖 Peer-Reviewed Manuscripts & Related Publications

1. **Sagal Andrade, R.** (2026). *High-Precision Numerical Mapping of Yarkovsky Perturbations and Non-Linear Flyby Dynamics of Asteroid (99942) Apophis in 2029*. **Astronomy and Computing** (Submitted).
2. **Sagal Andrade, R.** (2026). *An Open-Source Adaptive RK45 Software Framework for Hyperbolic Trajectory Validation: High-Precision Orbit Modeling of Interstellar Comet 3I/ATLAS*. **Astronomy and Computing** (Submitted).
3. **Sagal Andrade, R.** (2026). *3I/ATLAS Galactic Backtracking Framework: High-Precision Kinematics and Progenitor System Search via Gaia DR3*. **The Astronomical Journal**, AAS82079 (Submitted).

---

## 📄 Citation & BibTeX

If you utilize this framework, adaptive algorithms, or numerical state datasets in your research, please cite the framework and corresponding manuscripts:

```bibtex
@software{sagal_andrade_2026_astrobiology_today,
  author       = {Sagal Andrade, Rene},
  title        = {Astrobiology-Today: High-Precision Orbital Dynamics \& Planetary Defense Framework},
  month        = nov,
  year         = 2026,
  publisher    = {GitHub},
  version      = {v1.0.1},
  doi          = {10.5281/zenodo.XXXXXXX},
  url          = {https://github.com/sagal1031rene-coder/astrobiology-today}
}

@article{sagal_andrade_2026_apophis,
  author       = {Sagal Andrade, Rene},
  title        = {High-Precision Numerical Mapping of Yarkovsky Perturbations and Non-Linear Flyby Dynamics of Asteroid (99942) Apophis in 2029},
  journal      = {Astronomy and Computing},
  year         = 2026,
  note         = {Submitted}
}

@article{sagal_andrade_2026_3iatlas,
  author       = {Sagal Andrade, Rene},
  title        = {An Open-Source Adaptive RK45 Software Framework for Hyperbolic Trajectory Validation: High-Precision Orbit Modeling of Interstellar Comet 3I/ATLAS},
  journal      = {Astronomy and Computing},
  year         = 2026,
  note         = {Submitted}
}
```

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for details.
