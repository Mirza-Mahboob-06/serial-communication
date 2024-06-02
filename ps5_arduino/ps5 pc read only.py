import evdev
from evdev import InputDevice, categorize, ecodes

# Replace with your device path
device = InputDevice('/dev/input/event18')  # Initialize the PS5 controller device

print(device)  # Print information about the PS5 controller

# Loop to read input events from the PS5 controller
for event in device.read_loop():
    if event.type == ecodes.EV_KEY:  # Check if the event is a key/button event
        keyevent = categorize(event)  # Categorize the key event
        print(f"Key Event - Scancode: {keyevent.scancode}, Keystate: {keyevent.keystate}")
    elif event.type == ecodes.EV_ABS:  # Check if the event is an absolute axis event (analog control)
        absevent = categorize(event)  # Categorize the absolute axis event
        print(f"ABS Event - Code: {absevent.event.code}, Value: {absevent.event.value}")
