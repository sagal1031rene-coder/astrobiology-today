! pip install numpy matplotlib scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 1. PROPUESTA DE DESVIACIÓN HACIA LA TIERRA
t = np.linspace(-80, 80, 400)
t_pts = np.array([-80, -40, 0, 30, 53.6, 70, 80])
y_pts_full = np.array([2.10, 1.60, 0.75, 0.20, -0.60, -1.25, -1.60])
x_pts_full = np.array([1.00, 1.15, 1.32, 1.36, 1.30, 1.12, 1.00])
cs_x_full = CubicSpline(t_pts, x_pts_full)
cs_y_full = CubicSpline(t_pts, y_pts_full)
x_full = cs_x_full(t)
y_full = cs_y_full(t)

theta = np.linspace(0, 2*np.pi, 300)
R_earth = 1.0
R_mars = 1.524

t_pts_dev = np.array([-80, -40, 0, 30, 53.6, 70, 80])
y_pts_earth = np.array([2.10, 1.40, 0.50, -0.30, -0.80, -1.00, -1.10])
x_pts_earth = np.array([1.00, 1.10, 1.00, 0.90, 0.95, 1.00, 1.00])
cs_x_earth = CubicSpline(t_pts_dev, x_pts_earth)
cs_y_earth = CubicSpline(t_pts_dev, y_pts_earth)
x_earth_dest = cs_x_earth(t)
y_earth_dest = cs_y_earth(t)

plt.figure(figsize=(8, 8), dpi=100)
plt.plot(0, 0, marker='*', markersize=18, color='#e6b800', markeredgecolor='#b38f00', label='Sol')
plt.plot(R_earth * np.cos(theta), R_earth * np.sin(theta), linestyle='--', color='#2ca02c', label='Órbita de la Tierra')
plt.plot(R_mars * np.cos(theta), R_mars * np.sin(theta), linestyle='--', color='#ff7f7f', label='Órbita de Marte')
plt.plot(x_full, y_full, color='#cc0029', label='Trayectoria Original')
plt.plot(x_earth_dest, y_earth_dest, color='#9467bd', linestyle='-.', label='Trayectoria Desviada')
plt.plot(x_earth_dest[200], y_earth_dest[200], 'go', label='Punto de Intercepción')
plt.title('Propuesta de Desviación hacia la Tierra')
plt.legend()
plt.grid(True, linestyle=':')
plt.show()

# 2. COMPARATIVA JÚPITER VS MARTE
G = 6.67430e-11
M_mars = 6.39e23
M_jupiter = 1.898e27
v_inf = 25000.0
r_p_mars = 3389e3 + 200e3
r_p_jup = 71492e3 + 5000e3

def deflexion(M, r_p, v):
    mu = G * M
    return np.degrees(2.0 * np.arcsin(1.0 / (1.0 + (r_p * (v**2)) / mu)))

theta_m = deflexion(M_mars, r_p_mars, v_inf)
theta_j = deflexion(M_jupiter, r_p_jup, v_inf)

print(f"Deflexión máxima Marte: {theta_m:.6f} grados")
print(f"Deflexión máxima Júpiter: {theta_j:.2f} grados")
