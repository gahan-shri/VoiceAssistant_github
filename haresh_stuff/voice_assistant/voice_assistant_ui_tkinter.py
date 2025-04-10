import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk  # For dropdown menu
import assistant_processor as ap  # Import the processing module

class VoiceAssistantUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry("500x500")
        
        # Instruction Label
        self.instruction_label = tk.Label(root, text="Type or speak your query below:", font=("Arial", 14))
        self.instruction_label.pack(pady=10)
        
        # Port Selection Dropdown
        self.port_label = tk.Label(root, text="Select Port:", font=("Arial", 12))
        self.port_label.pack(pady=5)
        
        self.port_var = tk.StringVar()
        self.port_dropdown = ttk.Combobox(root, textvariable=self.port_var, font=("Arial", 12))
        self.port_dropdown['values'] = ap.get_available_ports()  # Delegate port fetching
        self.port_dropdown.pack(pady=5)
        
        self.connect_button = tk.Button(root, text="Connect", font=("Arial", 12), command=self.connect_to_port)
        self.connect_button.pack(pady=5)
        
        # Input Text Box
        self.input_box = tk.Entry(root, font=("Arial", 12))
        self.input_box.pack(fill="x", padx=10, pady=5)
        
        # Response Text Area
        self.response_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), height=10)
        self.response_area.pack(fill="both", padx=10, pady=5, expand=True)
        self.response_area.insert(tk.END, "Response will appear here.")
        self.response_area.config(state="disabled")  # Make it read-only
        
        # Configure tags for conversation styling
        self.response_area.tag_config("user", foreground="blue", font=("Arial", 12, "bold"))
        self.response_area.tag_config("assistant", foreground="green", font=("Arial", 12))
        
        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        self.submit_button = tk.Button(button_frame, text="Submit", font=("Arial", 12), command=self.process_input)
        self.submit_button.pack(side="left", padx=5)
        
        self.speak_button = tk.Button(button_frame, text="Speak", font=("Arial", 12), command=self.process_speech)
        self.speak_button.pack(side="left", padx=5)
        
        self.exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 12), command=root.quit)
        self.exit_button.pack(side="left", padx=5)
        
        # Schedule the voice to play after the UI is fully loaded
        self.root.after(500, lambda: ap.play_initial_message())
    
    def connect_to_port(self):
        selected_port = self.port_var.get()
        if selected_port:
            response = ap.connect_to_port(selected_port)  # Delegate connection logic
            self.update_response("System", response)
        else:
            self.update_response("System", "No port selected.")
    
    def update_response(self, user_input, response):
        self.response_area.config(state="normal")  # Make it editable temporarily
        # Append user input and assistant response to the conversation thread
        self.response_area.insert(tk.END, f"\nYou: {user_input}\n", "user")
        self.response_area.insert(tk.END, f"Assistant: {response}\n\n", "assistant")
        self.response_area.config(state="disabled")  # Make it read-only again
        self.response_area.see(tk.END)  # Scroll to the latest entry
    
    def process_input(self):
        user_input = self.input_box.get().strip()  # Get input without converting to uppercase
        self.input_box.delete(0, tk.END)  # Clear the input box
        
        if not user_input:
            return  # Ignore empty input
        
        response = ap.process_user_input(user_input)  # Delegate processing to the new module
        self.update_response(user_input, response)  # Update the conversation thread
    
    def process_speech(self):
        try:
            user_input = ap.get_speech_input()  # Delegate speech input to the new module
            if user_input:
                self.input_box.insert(0, user_input)  # Display the recognized speech in the input box
                self.process_input()  # Process the recognized speech
        except Exception as e:
            self.update_response("Speech Input", "Error: Could not process speech.")
            print(e)

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantUI(root)
    root.mainloop()
