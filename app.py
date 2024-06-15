from flask import Flask, render_template, jsonify, request
from gps_reader import read_gps_data, parse_gps_data
from map_creator import create_map
import threading
import serial
import serial.tools.list_ports

app = Flask(__name__)

latest_coords = {'lat': 27.6706, 'lon': 84.4385}
serial_port = None
selected_port = None
selected_baudrate = 9600

def update_coords():
    global latest_coords, serial_port
    while True:
        if serial_port and serial_port.is_open:
            gps_data = read_gps_data(serial_port, selected_baudrate)
            if gps_data:
                latitude, longitude = parse_gps_data(gps_data)
                if latitude is not None and longitude is not None:
                    latest_coords['lat'] = latitude
                    latest_coords['lon'] = longitude
                    create_map(latitude, longitude)

@app.route('/')
def dashboard():
    return render_template('dashboard.html', coords=latest_coords)

@app.route('/coords')
def get_coords():
    return jsonify(latest_coords)

@app.route('/ports')
def get_ports():
    ports = [port.device for port in serial.tools.list_ports.comports()]
    return jsonify(ports)

@app.route('/set_port', methods=['POST'])
def set_port():
    global selected_port
    selected_port = request.json['port']
    return jsonify(success=True)

@app.route('/set_baudrate', methods=['POST'])
def set_baudrate():
    global selected_baudrate
    selected_baudrate = request.json['baudrate']
    return jsonify(success=True)

@app.route('/connect', methods=['POST'])
def connect():
    global serial_port, selected_port, selected_baudrate
    if selected_port:
        try:
            serial_port = serial.Serial(selected_port, selected_baudrate)
            return jsonify(success=True)
        except serial.SerialException as e:
            return jsonify(success=False, error=str(e))
    return jsonify(success=False, error="No port selected")

@app.route('/disconnect', methods=['POST'])
def disconnect():
    global serial_port
    if serial_port:
        serial_port.close()
        serial_port = None
        return jsonify(success=True)
    return jsonify(success=False, error="No device connected")

if __name__ == '__main__':
    threading.Thread(target=update_coords, daemon=True).start()
    app.run(debug=True)
