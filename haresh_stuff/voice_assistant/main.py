import tkinter as tk
from voice_assistant_ui_tkinter import VoiceAssistantUI
import subprocess

if __name__ == "__main__":
    # Open all assistant-related files
    subprocess.Popen(["python", "d:\\coding\\Python\\voice_assistant\\stt.py"])
    subprocess.Popen(["python", "d:\\coding\\Python\\voice_assistant\\tts.py"])
    subprocess.Popen(["python", "d:\\coding\\Python\\voice_assistant\\assi.py"])
    subprocess.Popen(["python","d:\\coding\\Python\\voice_assistant\\serialSend.py"])

    # Launch the Tkinter UI
    root = tk.Tk()
    app = VoiceAssistantUI(root)
    root.mainloop()

