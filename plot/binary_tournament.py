import matplotlib.pyplot as plt
import numpy as np

# Data for NSGA-II without and with binary tournament selection
# (Fuel Consumption in Liters/km, Avg Delay in Minutes)
nsga_ii_w_o_binary_tournament = {
    'fuel_consumption': np.array([3.8, 3.7, 3.6, 3.7, 3.9, 4.0, 3.8, 3.6, 3.9, 3.5, 3.6, 3.7, 3.8, 3.9, 3.9]),
    'avg_delay': np.array([12, 12, 11.8, 12.1, 12.2, 12.0, 12.3, 12.4, 11.9, 12.1, 12.0, 12.3, 12.5, 11.8, 12.0])
}

nsga_ii_with_binary_tournament = {
    'fuel_consumption': np.array([3.5, 3.4, 3.6, 3.5, 3.3, 3.5, 3.4, 3.6, 3.5, 3.7, 3.6, 3.4, 3.5, 3.6, 3.7, 3.8, 3.5, 3.3, 3.7, 3.6, 3.5, 3.4, 3.6, 3.7, 3.5]),
    'avg_delay': np.array([10, 9.8, 10.2, 9.9, 10.3, 10.1, 10.0, 9.7, 10.2, 10.4, 10.1, 9.9, 10.0, 9.8, 10.3, 9.7, 10.2, 9.9, 10.0, 10.1, 10.0, 9.8, 9.9, 10.2, 9.7])
}

# Plotting
plt.figure(figsize=(10, 6))

# Plot for NSGA-II without Binary Tournament (using blue)
plt.scatter(
    nsga_ii_w_o_binary_tournament['fuel_consumption'],
    nsga_ii_w_o_binary_tournament['avg_delay'],
    color='blue',
    label='NSGA-II without Binary Tournament',
    alpha=0.6,
    edgecolors='black'
)

# Plot for NSGA-II with Binary Tournament (using green)
plt.scatter(
    nsga_ii_with_binary_tournament['fuel_consumption'],
    nsga_ii_with_binary_tournament['avg_delay'],
    color='green',
    label='NSGA-II with Binary Tournament',
    alpha=0.6,
    edgecolors='black'
)

# Highlighting key data points for better visibility (Min values and max values)
plt.scatter(3.8, 12, color='red', marker='x', label='NSGA-II w/o Binary Tournament Min')
plt.scatter(3.5, 10, color='orange', marker='x', label='NSGA-II with Binary Tournament Min')

# Labels and Title
plt.title('Pareto Fronts for NSGA-II with and without Binary Tournament Selection')
plt.xlabel('Fuel Consumption (Liters/km)')
plt.ylabel('Avg Delay (Minutes)')
plt.legend()

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()