from flask import Flask, render_template
from gps_reader import read_gps_data, parse_gps_data
from map_creator import create_map

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/update')
def update_map():
    gps_data = read_gps_data()
    latitude, longitude = parse_gps_data(gps_data)
    create_map(latitude, longitude)
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
