import serial
import time 
'''# Replace with your Arduino's port (e.g., 'COM3' on Windows, '/dev/ttyUSB0' on Linux/Mac)
arduino_port = '/dev/ttyACM0'

# Set the baud rate to match your Arduino's setting (common baud rates: 9600, 115200)
baud_rate = 9600

# Open the serial connection
ser = serial.Serial(arduino_port, baud_rate,timeout=1.0)
while 1:
 ser.reset_input_buffer()
 data = ser.readline().decode('utf-8')
 print(type(data),end="\n")  
'''

def serial_begin():
    # Create the serial object
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1.0)
    ser.reset_input_buffer()

    # Collect all available data
    data = ""
    while ser.in_waiting > 0:
        data += ser.readline().decode('utf-8')

    # Return the collected data, or None if nothing was read
    return data if data else None

      
gaza = serial_begin()
print(gaza)