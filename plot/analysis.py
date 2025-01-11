import matplotlib.pyplot as plt
import numpy as np

# Data
fuel_weight = np.array([50, 70, 90])
fuel_consumption = np.array([3.5, 3.2, 3.0])
avg_delay = np.array([10, 12, 15])
satisfaction = np.array([88, 85, 80])

# Plot
plt.figure(figsize=(8, 6))

# Fuel Consumption Line
plt.plot(fuel_weight, fuel_consumption, label='Fuel Consumption (L/km)', color='blue', marker='o')

# Avg Delay Line
plt.plot(fuel_weight, avg_delay, label='Avg Delay (min)', color='red', marker='o')

# Passenger Satisfaction Line
plt.plot(fuel_weight, satisfaction, label='Passenger Satisfaction (%)', color='green', marker='o')

# Labels and Title
plt.xlabel('Fuel Weight (%)')
plt.ylabel('Objective Values')
plt.title('Changes in Objective Values with Varying Fuel Weight')
plt.legend()

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()