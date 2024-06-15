import serial
import folium
import webbrowser
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

ser = serial.Serial('COM3', 9600, timeout=1)

def read_coordinates():
    while True:
        try:
            data = ser.readline().decode('ascii').strip()
            if data:
                lat, lon = map(float, data.split(','))
                return lat, lon
        except (ValueError, IndexError):
            continue

latitude, longitude = read_coordinates()

mymap = folium.Map(location=[latitude, longitude], zoom_start=15)
folium.Marker([latitude, longitude], tooltip='Location').add_to(mymap)

map_filename = 'map.html'
mymap.save(map_filename)

print(f"Map created with coordinates: Latitude={latitude}, Longitude={longitude}")

def serve_map():
    port = 8000
    os.chdir(os.path.dirname(os.path.abspath(map_filename)))
    
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    url = f'http://localhost:{port}/{map_filename}'
    
    print(f"Serving map at {url}")
    webbrowser.open(url)
    
    httpd.serve_forever()

serve_map()
