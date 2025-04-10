import serial
import time

ser = None  # Global variable for the serial connection

def initialize_serial(port, baudrate=9600):
    global ser
    ser = serial.Serial(port, baudrate)
    print(f"Connected to {port} at {baudrate} baudrate.")

def send_command(command):
    command *= 5  # Repeat the command 5 times
    if ser and ser.is_open:
        ser.write(command.encode())
        print(f"Sent command: {command}")
    else:
        print("Serial port is not open.")

def oodu():
    try:
        while True:
            command = input("Enter command (F: Forward, B: Backward, L: Left, R: Right, S: Stop) ,X: exit :").upper()
            if command in ['F', 'B', 'L', 'R', 'S']:
                send_command(command * 5)
            elif command == 'X':
                print("Exiting program...")
                break
            else:
                print("Invalid command. Please enter F, B, L, R, or S.")
    except KeyboardInterrupt:
        print("Exiting program")
    finally:
        if ser:
            ser.close()