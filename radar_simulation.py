import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light (m/s)
pulse_time = 2e-6  # Round-trip time (2 microseconds)

# Distance Calculation
distance = (c * pulse_time) / 2  # Distance (meters)
print(f"Target Distance: {distance} meters")

# Simulating Signal Transmission and Reception
time = np.linspace(0, 1e-5, 1000)  # Time range (10 microseconds)
signal = np.sin(2 * np.pi * 1e6 * time)  # Radar signal (1 MHz frequency)
reflected_signal = np.roll(signal, 50)  # Delayed reflected signal

# Visualization
plt.figure(figsize=(10, 6))
plt.plot(time, signal, label="Transmitted Signal")
plt.plot(time, reflected_signal, label="Reflected Signal", linestyle="--")
plt.legend()
plt.title("Radar Signal Simulation")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
