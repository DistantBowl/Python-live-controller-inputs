from ursina import *
from time import sleep

app = Ursina()  # Create the application
app.close_window(app.win)  # and hide the application window

# List connected devices
devices = app.devices.get_devices()
print("Connected Devices:\n")
for i,device in enumerate(devices):
    print(f"{i}: {device}")

# Verify and select a device
verifying = True
while verifying:
    deviceID = input("\nSelect Device: ")
    if deviceID.isnumeric():
        deviceID = int(deviceID)
        if 0 <= deviceID < len(devices):
            device = devices[deviceID]
            print(f"selecting Device: {device.name}")
            print("-" * 40)
            verifying = False
        else:
            print("Device index out of range.")
    else:
        print("Please use an integer index")

# List button handles (names)
print("Button Handles:\n")
for i,button in enumerate(device.buttons):
    print(f"{i}: {button.handle}")
print("-"*40)

# Verify and select buttons for monitoring
verifying = True
while verifying:
    monitorButtons = input("\nButton handles to monitor (e.g. 0,4,10): ").strip().split(',')
    invalid = False
    for button in monitorButtons:
        if not button.isnumeric():
            print("Please use only integer indexes.")
            invalid = True
    if not invalid:
        verifying = False

# List axes handles (names)
print("Axis Handles:\n")
for i,axis in enumerate(device.axes):
    print(f"{i}: {axis.axis}")
print("-" * 40)

# Verify and select axes for monitoring
verifying = True
while verifying:
    monitorAxis = input("\nAxis handles to monitor (e.g. 0,2,3): ").strip().split(',')
    invalid = False
    for button in monitorAxis:
        if not button.isnumeric():
            print("Please use only integer indexes.")
            invalid = True
    if not invalid:
        verifying = False

# Define the input polling function
def update():
    for button in monitorButtons:
        print(f"{device.buttons[int(button)].handle}: {device.buttons[int(button)].pressed}")

    for axis in monitorAxis:
        print(f"{device.axes[int(axis)].axis}: {device.axes[int(axis)].value}")

    print("-"*40)

    sleep(1)

app.run()