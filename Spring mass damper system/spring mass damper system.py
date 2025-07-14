import numpy as np
import matplotlib.pyplot as plt

# System Parameters
m = 1.0  # Mass (kg)
k = 100.0  # Spring stiffness (N/m)

# Calculate natural frequency
omega_n = np.sqrt(k / m)

# Time array for simulation
time = np.linspace(0, 5, 500)  # 5 seconds, 500 points

# Initial conditions
x0 = 0.1  # Initial displacement (m)
v0 = 0.0  # Initial velocity (m/s)

plt.figure(figsize=(10, 6))

# --- Underdamped Case (zeta < 1) ---
c_under = 0.5 * 2 * m * omega_n  # Choose c for zeta = 0.5
zeta_under = c_under / (2 * m * omega_n)
omega_d_under = omega_n * np.sqrt(1 - zeta_under**2)

# Constants for underdamped solution
A_under = x0
B_under = (v0 + zeta_under * omega_n * x0) / omega_d_under

x_under = np.exp(-zeta_under * omega_n * time) * \
          (A_under * np.cos(omega_d_under * time) + B_under * np.sin(omega_d_under * time))
plt.plot(time, x_under, label=f'Underdamped (ζ = {zeta_under:.2f})')

# --- Critically Damped Case (zeta = 1) ---
c_crit = 1.0 * 2 * m * omega_n  # Choose c for zeta = 1.0
zeta_crit = c_crit / (2 * m * omega_n)

# Constants for critically damped solution
A_crit = x0
B_crit = v0 + omega_n * x0

x_crit = (A_crit + B_crit * time) * np.exp(-omega_n * time)
plt.plot(time, x_crit, label=f'Critically Damped (ζ = {zeta_crit:.2f})', linestyle='--')

# --- Overdamped Case (zeta > 1) ---
c_over = 1.5 * 2 * m * omega_n  # Choose c for zeta = 1.5
zeta_over = c_over / (2 * m * omega_n)

lambda1_over = -zeta_over * omega_n + omega_n * np.sqrt(zeta_over**2 - 1)
lambda2_over = -zeta_over * omega_n - omega_n * np.sqrt(zeta_over**2 - 1)

# Constants for overdamped solution
# Using initial conditions: x(0) = x0, v(0) = v0
# x0 = A + B
# v0 = A*lambda1 + B*lambda2
# Solve for A and B
B_over = (v0 - lambda1_over * x0) / (lambda2_over - lambda1_over)
A_over = x0 - B_over

x_over = A_over * np.exp(lambda1_over * time) + B_over * np.exp(lambda2_over * time)
plt.plot(time, x_over, label=f'Overdamped (ζ = {zeta_over:.2f})', linestyle=':')

plt.title('Spring-Mass-Damper System Response')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid(True)
plt.legend()
plt.show()


