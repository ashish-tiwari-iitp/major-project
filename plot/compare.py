import matplotlib.pyplot as plt
import numpy as np

# Data
methods = ['FCFS', 'GA', 'NSGA-II (Proposed)']
fuel_consumption = [4.5, 3.9, 3.5]
avg_delay = [20, 15, 10]
satisfaction = [75, 80, 88]

# Create figure and axis objects
fig, ax1 = plt.subplots()

# Bar chart for Fuel Consumption
ax1.bar(methods, fuel_consumption, color='lightblue', label='Fuel Consumption (L/km)')
ax1.set_xlabel('Method')
ax1.set_ylabel('Fuel Consumption (L/km)', color='lightblue')
ax1.tick_params(axis='y', labelcolor='lightblue')

# Create second y-axis for Avg Delay and Satisfaction
ax2 = ax1.twinx()
ax2.plot(methods, avg_delay, color='orange', marker='o', label='Avg Delay (min)')
ax2.plot(methods, satisfaction, color='green', marker='o', label='Passenger Satisfaction (%)')
ax2.set_ylabel('Avg Delay (min) / Satisfaction (%)', color='black')
ax2.tick_params(axis='y')

# Title and show the plot
plt.title('Performance Comparison of Methods')
fig.tight_layout()  # Ensure everything fits
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.show()