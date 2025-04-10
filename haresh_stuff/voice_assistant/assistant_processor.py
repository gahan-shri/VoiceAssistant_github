import serial
import serial.tools.list_ports
import tts as t
import stt as s
import assi as g
from app_opener import open_app  # Import the app_opener module

ser = None  # Global variable for the serial connection

def get_available_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]

def connect_to_port(port, baudrate=9600):
    global ser
    try:
        ser = serial.Serial(port, baudrate)
        return f"Connected to {port} at {baudrate} baudrate."
    except Exception as e:
        return f"Failed to connect to {port}: {e}"

def send_command(command):
    if ser and ser.is_open:
        ser.write(command.encode())
        return f"Sent command: {command}"
    else:
        return "Serial port is not open."

def process_user_input(user_input):
    if "ROBO" in user_input.upper():
        response = "Moving robo "
        if "FORWARD" in user_input.upper():
            response += "Forward"
            send_command("U")
        elif "BACKWARD" in user_input.upper():
            response += "Backward"
            send_command("D")
        elif "LEFT" in user_input.upper():
            response += "Left"
            send_command("L")
        elif "RIGHT" in user_input.upper():
            response += "Right"
            send_command("R")
        elif "STOP" in user_input.upper():
            response += "Stop"
            send_command("S")
        else:
            response += "Unknown direction"
        
    elif "OPEN" in user_input.upper():
        # Extract the app name after "OPEN"
        app_name = user_input.upper().replace("OPEN", "").strip()
        response = open_app(app_name)  # Use the app_opener module
    elif "EXIT" in user_input.upper():
        response = "Exiting the program"
    else:
        response = g.generate(user_input)
    
    # Ensure TTS is called correctly
    try:
        t.sollu(response)
    except Exception as e:
        print(f"Error in text-to-speech: {e}")
    
    return response

def get_speech_input():
    return s.kelu().strip()

def play_initial_message():
    try:
        t.sollu("Ask whatever you want to do")
    except Exception as e:
        print(f"Error in text-to-speech: {e}")
