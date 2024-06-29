# *-* coding: utf-8 *-*
# @Author: @2sayle
# Date: 2024-29-06
# Version: 1.1
# Description: Main program of the Solar Panel Simulator with annual plots

from solarpanel import SolarPanel
import matplotlib.pyplot as plt
import numpy as np

# Create a solar panel object
mySolarPanel = SolarPanel(area=2, efficiency=20, tilt=30, orientation=0)

# Set constant parameters
hour = 15  # 3 PM each day
latitude = 48.85  # Paris, for example

# Prepare lists to store data
days = list(range(1, 366))
irradiances = []
powers = []

# Calculate irradiance and power for each day of the year
for day in days:
    irradiance = mySolarPanel.computeIrradiance(hour, day, latitude)
    power = mySolarPanel.computePower(irradiance)
    irradiances.append(irradiance)
    powers.append(power)

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot irradiance
ax1.plot(days, irradiances, 'r-')
ax1.set_title(f"Annual Irradiance at {hour}:00 (Latitude: {latitude}°)")
ax1.set_xlabel("Day of the Year")
ax1.set_ylabel("Irradiance (W/m²)")
ax1.grid(True)

# Plot power
ax2.plot(days, powers, 'b-')
ax2.set_title(f"Annual Power Production at {hour}:00")
ax2.set_xlabel("Day of the Year")
ax2.set_ylabel("Power (W)")
ax2.grid(True)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()

# Print some statistics
print(f"Average Irradiance: {np.mean(irradiances):.2f} W/m²")
print(f"Average Power: {np.mean(powers):.2f} W")
print(f"Maximum Irradiance: {np.max(irradiances):.2f} W/m²")
print(f"Maximum Power: {np.max(powers):.2f} W")