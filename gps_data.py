def parse_gps_data(data):
    try:
        lat, lon = map(float, data.split(','))
        return lat, lon
    except ValueError:
        return None, None

# Example usage:
gps_data = "12.345678,98.765432"
latitude, longitude = parse_gps_data(gps_data)
print(f"Latitude: {latitude}, Longitude: {longitude}")
