import serial
import time


port = 'COM6'
baudrate = 9600

ser = serial.Serial(port, baudrate)

def send_command(command):
    ser.write(command.encode())
    print(f"Sent command: {command}")
def oodu():
    try:
        while True:
            command = input("Enter command (F: Forward, B: Backward, L: Left, R: Right, S: Stop) ,X: exit :").upper()
        
            if command in ['F', 'B', 'L', 'R', 'S']:
                send_command(command)
            elif command == 'X':
                print("Exitting program...")
                break
            else:
                print("Invalid command. Please enter F, B, L, R, or S.")
    except KeyboardInterrupt:
        print("Exiting program")

    finally:
        ser.close()