import serial
import time

# Set up the serial connection to COM3
ser = serial.Serial('COM3', baudrate=9600, timeout=1)

# Give some time for the connection to establish
time.sleep(2)

print("Connected to: " + ser.portstr)

try:
    while True:
        if ser.in_waiting > 0:
            # Read the data from the serial buffer
            data = ser.readline().decode('utf-8').rstrip()
            if data:
                print(f"Received: {data}")
except KeyboardInterrupt:
    print("Program interrupted")

finally:
    # Close the serial connection
    ser.close()
    print("Serial connection closed")