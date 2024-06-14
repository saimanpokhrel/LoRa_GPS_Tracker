import serial

def read_gps_data(port='COM3', baudrate=9600):
    ser = serial.Serial(port, baudrate)
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(line)  # Process or save the data as needed
            return line  # Assuming each line contains a new set of coordinates

# Example usage:
if __name__ == "__main__":
    gps_data = read_gps_data()
    print(gps_data)
