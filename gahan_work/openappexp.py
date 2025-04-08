import speech_recognition as sr
import pyttsx3
import subprocess
import os

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts = pyttsx3.init()

# Map voice commands to app paths
app_dict = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    "excel": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    # Add more apps and their full paths here
}

def speak(text):
    tts.say(text)
    tts.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Sorry, there's a problem with the speech service.")
        return ""

def launch_app(command):
    for app_name in app_dict:
        if app_name in command:
            app_path = app_dict[app_name]
            try:
                subprocess.Popen(app_path)
                speak(f"Opening {app_name}")
                return
            except FileNotFoundError:
                speak(f"Could not find {app_name}")
                return
    speak("Application not found in list.")

# Main loop
if __name__ == "__main__":
    speak("Voice app launcher initialized. Say the name of the application.")
    while True:
        cmd = listen()
        if "exit" in cmd or "quit" in cmd:
            speak("Goodbye!")
            break
        elif cmd:
            launch_app(cmd)
