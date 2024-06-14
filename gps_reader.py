import serial
import time

def read_gps_data(port='COM7', baudrate=9600):
    while True:
        try:
            ser = serial.Serial(port, baudrate)
            while True:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').strip()
                    return line  # Assuming each line contains a new set of coordinates
        except serial.SerialException as e:
            print(f"SerialException: {e}")
            time.sleep(5)  # Wait for 5 seconds before retrying
        except PermissionError as e:
            print(f"PermissionError: {e}")
            time.sleep(5)  # Wait for 5 seconds before retrying
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(5)  # Wait for 5 seconds before retrying

def parse_gps_data(data):
    try:
        lat, lon = map(float, data.split(','))
        return lat, lon
    except ValueError:
        return None, None
