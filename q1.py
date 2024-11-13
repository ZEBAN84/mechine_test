import pandas as pd
import numpy as np
import folium
from haversine import haversine

# Load the data
data = pd.read_csv('C:/Users/91859/Documents/vs code/mechine test/latitude_longitude_details (2).csv')

# Check column names to ensure correct access
print("Columns in CSV:", data.columns)

# Ensure 'latitude' and 'longitude' column names are correct in the file
if 'latitude' not in data.columns or 'longitude' not in data.columns:
    raise ValueError("Ensure 'latitude' and 'longitude' columns are present in the CSV file.")

# Calculate distances between consecutive points to identify discontinuities
data['distance_to_previous'] = [0] + [
    haversine(
        (data.loc[i - 1, 'latitude'], data.loc[i - 1, 'longitude']),
        (data.loc[i, 'latitude'], data.loc[i, 'longitude'])
    ) for i in range(1, len(data))
]

# Define a threshold (based on IQR) to detect discontinuities
q75, q25 = np.percentile(data['distance_to_previous'][1:], [75, 25])
iqr = q75 - q25
distance_threshold = q75 + 1.5 * iqr

# Fix discontinuous points by interpolating outliers
corrected_data = data.copy()
for i in range(1, len(corrected_data)):
    if corrected_data.loc[i, 'distance_to_previous'] > distance_threshold:
        prev_point = corrected_data.loc[i - 1, ['latitude', 'longitude']]
        next_point = corrected_data.loc[min(i + 1, len(corrected_data) - 1), ['latitude', 'longitude']]
        # Interpolating latitude and longitude
        corrected_data.loc[i, 'latitude'] = (prev_point['latitude'] + next_point['latitude']) / 2
        corrected_data.loc[i, 'longitude'] = (prev_point['longitude'] + next_point['longitude']) / 2

# Save corrected data to CSV
corrected_path = 'C:/Users/91859/Documents/vs code/mechine test/latitude_longitude_cleaned.csv'
corrected_data[['latitude', 'longitude', 'Terrain']].to_csv(corrected_path, index=False)
print("Corrected data saved to:", corrected_path)

# Initialize the map centered around the average location
center = [data['latitude'].mean(), data['longitude'].mean()]
map_ = folium.Map(location=center, zoom_start=15)

# Coordinates for original and corrected paths
original_coords = list(zip(data['latitude'], data['longitude']))
corrected_coords = list(zip(corrected_data['latitude'], corrected_data['longitude']))

# Plot the original path with red markers and a connecting red line
for lat, lon in original_coords:
    folium.Marker(
        location=[lat, lon],
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(map_)
folium.PolyLine(original_coords, color='red', weight=2.5, opacity=0.8, tooltip="Original Path").add_to(map_)

# Plot the corrected path with blue markers and a connecting blue line
for lat, lon in corrected_coords:
    folium.Marker(
        location=[lat, lon],
        icon=folium.Icon(color='blue', icon='cloud')
    ).add_to(map_)
folium.PolyLine(corrected_coords, color='blue', weight=2.5, opacity=0.8, tooltip="Corrected Path").add_to(map_)

# Save the map with both paths to an HTML file
output_map_path = 'C:/Users/91859/Documents/vs code/mechine test/path_comparison_map.html'
map_.save(output_map_path)
print("Map with original and corrected paths saved as:", output_map_path)
