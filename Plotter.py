import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Load the CSV file
file_path = 'youtube_stats_360p.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Convert 'speed' from Kbps to Mbps and 'buffer_health' to float
data['speed'] = data['speed'].str.replace(' Kbps', '').astype(float) / 1000
data['buffer_health'] = data['buffer_health'].str.replace(' s', '').astype(float)

# Calculate the average buffer health for each speed
avg_buffer_health = data.groupby('speed')['buffer_health'].min().reset_index()

# Apply a moving average to smooth out large deviations
window_size = 50  # Window size can be adjusted based on the desired level of smoothing
avg_buffer_health['smoothed_buffer_health'] = avg_buffer_health['buffer_health'].rolling(window=window_size, min_periods=1).mean()

# Check if adjacent nodes vary largely and adjust
max_variation = 0.25  # Max allowed variation (25%)
max_speed_difference = 20  # Maximum speed difference to consider adjustment (in Mbps)

for i in range(1, len(avg_buffer_health)):
    current_val = avg_buffer_health.loc[i, 'smoothed_buffer_health']
    previous_val = avg_buffer_health.loc[i-1, 'smoothed_buffer_health']
    speed_difference = avg_buffer_health.loc[i, 'speed'] - avg_buffer_health.loc[i-1, 'speed']

    if abs(current_val - previous_val) / previous_val > max_variation and speed_difference <= max_speed_difference:
        if current_val > previous_val:
            adjusted_val = (current_val + previous_val) / 4
        else:
            adjusted_val = (current_val + previous_val) / 4
            avg_buffer_health.loc[i-1, 'smoothed_buffer_health'] = adjusted_val
# Continue with the rest of your script, e.g., spline interpolation and plotting


# Spline interpolation for a smoother curve
X = avg_buffer_health['speed']
Y = avg_buffer_health['smoothed_buffer_health']
X_new = np.linspace(X.min(), X.max(), 1000)  # More points for a smoother curve
spl = make_interp_spline(X, Y, k=3)  # Cubic spline for smoothness
Y_smooth = spl(X_new)

Y_smooth = np.clip(Y_smooth, a_min=0, a_max=None)

outlier_threshold = 0.5  # Define the threshold for considering a value as an outlier
window_radius = 5  # Number of adjacent points to consider on either side

for i in range(window_radius, len(Y_smooth) - window_radius):
    local_mean = np.mean(Y_smooth[i-window_radius:i+window_radius+1])
    if abs(Y_smooth[i] - local_mean) / local_mean > outlier_threshold:
        Y_smooth[i] = local_mean  # Replace the outlier with the local mean



# Plotting

plt.figure(figsize=(12, 6))
plt.plot(X, Y, linestyle='solid')

# Define the range for the x-axis ticks
x_ticks = np.arange(0, X.max() + 2, 2)

# Set x-axis labels to be more granular
plt.xticks(x_ticks)

plt.title('Buffer Health vs. Network Speed (360p)')
plt.xlabel('Network Speed (Mbps)')
plt.ylabel('Buffer Health (s)')
plt.grid(True)
plt.show()

# Saving the processed data (optional)
avg_buffer_health.to_csv('smoothed_data_1080p.csv', index=False)
