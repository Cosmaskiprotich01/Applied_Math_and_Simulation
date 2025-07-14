import numpy as np
import matplotlib.pyplot as plt

# Parameters for Newton's Law of Cooling
T_s = 20.0  # Ambient temperature (degrees Celsius)
T_0 = 90.0  # Initial temperature of coffee (degrees Celsius)
k = 0.05    # Cooling constant (per minute)

# Simulation time
time_start = 0
time_end = 60      # Simulate for 60 minutes
num_steps = 500    # Number of time points

time = np.linspace(time_start, time_end, num_steps) # Time points for simulation

# Calculate the temperature at each time point using Newton's Law of Cooling
# T(t) = T_s + (T_0 - T_s) * e^(-k*t)
temperature = T_s + (T_0 - T_s) * np.exp(-k * time)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time, temperature, label=f'T(t) = {T_s} + ({T_0} - {T_s})e^(-{k}t)')

# Add a horizontal line for ambient temperature
plt.axhline(y=T_s, color='r', linestyle='--', label='Ambient Temperature (T_s)')

plt.title('Coffee Cooling Simulation (Newton\'s Law of Cooling)')
plt.xlabel('Time (minutes)')
plt.ylabel('Temperature (degrees Celsius)')
plt.grid(True)
plt.legend()
plt.show()


