import numpy as np
import matplotlib.pyplot as plt

# Parameters
half_life = 5730  # Half-life of the radioactive substance (e.g., years)
decay_constant = np.log(2) / half_life  # Decay constant (lambda)
initial_nuclei = 1000  # Initial number of radioactive nuclei

# Simulation time
time_start = 0
time_end = half_life * 4  # Simulate for 4 half-lives
num_steps = 1000

time = np.linspace(time_start, time_end, num_steps)  # Time points for simulation

# Calculate the number of nuclei at each time point using the decay law
nuclei = initial_nuclei * np.exp(-decay_constant * time)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time, nuclei, label=f'N(t) = N₀ × e^(-λt) (Half-life = {half_life} units)', 
         linewidth=2, color='blue')

# Mark half-life points
for i in range(1, int(time_end / half_life) + 1):
    t_half = i * half_life
    n_half = initial_nuclei * (0.5)**i
    plt.plot([t_half, t_half], [0, n_half], 'k--', linewidth=0.8, alpha=0.7)
    plt.plot([0, t_half], [n_half, n_half], 'k--', linewidth=0.8, alpha=0.7)
    plt.text(t_half + 0.1, n_half, f'{i}T½', verticalalignment='bottom', 
             fontsize=9, fontweight='bold')

plt.title('Radioactive Decay Simulation', fontsize=14, fontweight='bold')
plt.xlabel('Time (arbitrary units)', fontsize=12)
plt.ylabel('Number of Radioactive Nuclei', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()