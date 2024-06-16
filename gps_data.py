def parse_gps_data(data):
    try:
        lat, lon = map(float, data.split(','))
        return lat, lon
    except ValueError:
        return None, None
