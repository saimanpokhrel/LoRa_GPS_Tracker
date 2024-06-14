from flask import Flask, render_template, jsonify
from gps_reader import read_gps_data, parse_gps_data
from map_creator import create_map
import threading

app = Flask(__name__)

latest_coords = {'lat': 0.0, 'lon': 0.0}

def update_coords():
    global latest_coords
    while True:
        gps_data = read_gps_data()
        latitude, longitude = parse_gps_data(gps_data)
        if latitude and longitude:
            latest_coords['lat'] = latitude
            latest_coords['lon'] = longitude
            create_map(latitude, longitude)

@app.route('/')
def dashboard():
    return render_template('dashboard.html', coords=latest_coords)

@app.route('/coords')
def get_coords():
    return jsonify(latest_coords)

if __name__ == '__main__':
    threading.Thread(target=update_coords, daemon=True).start()
    app.run(debug=True)
