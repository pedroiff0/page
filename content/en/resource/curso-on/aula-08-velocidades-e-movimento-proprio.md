---
{"publish":true,"title":"🚀 Lecture 08 — Velocities & Proper Motion","created":"2026-07-23","modified":"2026-07-23T00:27:28.393-03:00","tags":["curso-on","galactic-archaeology","stellar-populations","stellar-kinematics"],"cssclasses":["page-grid","center-images"]}
---

# 🚀 Lecture 08 — Velocities & Proper Motion

> [!note] Summary
> The last piece of the puzzle (position, chemistry, age, and now kinematics): how to decompose a star's space velocity into radial and tangential components, and how to reference them to the Galaxy's Local Standard of Rest — the observational basis for any stellar dynamics study (Unit 3 of the syllabus).

> [!info] Lecture info
> **Course:** Galactic Archaeology and Stellar Populations
> **Institution:** National Observatory (ON), Brazil
> **Professor:** Hélio Dotto Perottoni

---

## 🎯 Radial and tangential velocity

A star's space velocity, relative to the Sun, decomposes into two vectors:

- **Radial velocity ($v_R$):** along the line of sight, measured via the **Doppler shift** of spectral lines.
- **Tangential velocity:** perpendicular to the line of sight, measured via **astrometric** techniques (proper motion + distance).

$v_R = c\,\frac{\Delta\lambda}{\lambda_0}$

where $\Delta\lambda$ is the Doppler shift and $\lambda_0$ the transition's rest wavelength. What's measured directly at the telescope is the **topocentric** $v_R$, which must be successively corrected to Earth's center (geocentric $v_R$) and then to the Sun's center (heliocentric $v_R$).

## 🗺️ Reference frame for space velocities

The reference frame for velocities in the Galaxy is based on the galactic Cartesian coordinate system (Lecture 07), with the same convention ambiguities regarding the radial axis direction. The Cartesian velocity components are called $(U,V,W)$; when reduced to the **Galactic Rest Frame**, cylindrical velocity components $(\Pi,\Theta,Z)$ are used, which coincide numerically with $(U,V,W)$ in the solar neighborhood.

## 🧭 Local Standard of Rest (LSR)

The **LSR** is defined by the **average** velocity of stars in the solar neighborhood. Since the only global motion of that neighborhood is rotational, the LSR corresponds to the circular velocity at the Sun's position:

$(\Pi_{LSR}, \Theta_{LSR}, Z_{LSR}) = (0, \Theta_0, 0)$

The value of $\Theta_0$ is still poorly constrained — the literature uses values between 180 and 250 km/s, with **220 km/s** the most commonly adopted. A star's **peculiar** velocity relative to the LSR is the difference between its velocity and $\Theta_0$.

The **Sun** itself has a peculiar velocity relative to the LSR — generally adopted as $(u,v,w)_\odot = (-9, 11, 6)\,$km/s \[see Mihalas & Binney 1980, Ch. 6, for the measurement methods]. That is, the **Sun moves somewhat faster** than the strict LSR. Any nearby star's heliocentric velocity is therefore the difference between the star's and the Sun's peculiar velocities.

### Radial velocity in other reference frames

For galactic dynamics studies, it's more appropriate to remove the solar velocity's contribution projected along the line of sight:

- **Relative to the LSR:** the radial velocity an observer co-moving with the LSR would measure.
- **Relative to the Galactic Standard of Rest (adopting $\Theta_0=220\,$km/s):** the radial velocity a **stationary** observer at the Galaxy's rest frame, at the Sun's current position, would measure. This is the most appropriate frame for studying the velocity distribution of stars across different sky directions.

## 🎯 Proper motion

The apparent shift of a star on the celestial sphere, caused by its **tangential** velocity, is called **proper motion**. It's measured in arcseconds traversed per unit time — typically **milliarcseconds/year (mas/yr)**.

To convert proper motion ($\mu$) into tangential velocity, the **distance** $d$ to the object must be known (see Lecture 07):

$v_{tan} = 4.74\,\mu\,[''/\text{yr}]\; \cdot\; d\,[\text{pc}] \quad \text{km/s}$

The observed proper motion will be **large** when:

1. The distance to the object is **small**, or
2. The object has a **large** tangential velocity relative to the Sun.

Typical proper motions are $< 0.1''$/year; few stars have $\mu > 1.0''$/year. Proper motion can be decomposed along the axes of the coordinate system used — e.g., $\mu_\alpha$ and $\mu_\delta$ in equatorial coordinates.

---

## 📌 Key concepts

- **Radial velocity (Doppler) + tangential velocity (proper motion + distance) = full space velocity.**
- **LSR:** mean circular velocity at the Sun's position, $\Theta_0\approx220\,$km/s; the Sun has its own peculiar velocity relative to it, $(u,v,w)_\odot=(-9,11,6)\,$km/s.
- **Proper motion depends on distance:** the same $v_{tan}$ produces a larger $\mu$ the closer the star is — take care when comparing $\mu$ across populations at very different distances.

## 🔗 References and related

- Mihalas & Binney (1980), Ch. 6 — determining the Sun's motion relative to the LSR
- [CursoON — overview](en/resource/curso-on)
- [Lecture 07 — Distances, Distance Scale & Coordinate Systems](en/resource/curso-on/aula-07-distancias-e-coordenadas) — direct prerequisite (distance enters the $\mu \to v_{tan}$ conversion)
- [Anomaly Detection in Gaia Data](en/research/anomaly-detection) — LSR kinematics is one of the pre-processing filters used in my research
