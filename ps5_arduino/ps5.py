import evdev
from evdev import InputDevice, categorize, ecodes
import serial

# Replace with your device path
device = InputDevice('/dev/input/event18')  # Initialize the PS5 controller device
arduino = serial.Serial('/dev/ttyACM0', 115200)  # Initialize the serial connection to the Arduino

print(device)  # Print information about the PS5 controller

# Loop to read input events from the PS5 controller
for event in device.read_loop():
    if event.type == ecodes.EV_KEY:  # Check if the event is a key/button event
        keyevent = categorize(event)  # Categorize the key event
        data = f"KEY,{keyevent.scancode},{keyevent.keystate}\n"  # Format the key event data
        arduino.write(data.encode())  # Send the formatted data to the Arduino
        print(f"Sent to Arduino: {data}")  # Print the data sent to the Arduino for debugging
    elif event.type == ecodes.EV_ABS:  # Check if the event is an absolute axis event (analog control)
        absevent = categorize(event)  # Categorize the absolute axis event
        data = f"ABS,{absevent.event.code},{absevent.event.value}\n"  # Format the absolute axis event data
        arduino.write(data.encode())  # Send the formatted data to the Arduino
        print(f"Sent to Arduino: {data}")  # Print the data sent to the Arduino for debugging
