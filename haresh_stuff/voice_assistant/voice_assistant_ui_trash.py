from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView  # Import ScrollView for wrapping long text
import tts as t
import assi as g
import stt as s
from kivy.animation import Animation  # Import Animation for button animations

class VoiceAssistantUI(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Label to display instructions
        self.instruction_label = Label(text="Type or speak your query below:", font_size=18, size_hint=(1, 0.2))
        self.layout.add_widget(self.instruction_label)
        
        # TextInput for user input
        self.input_box = TextInput(
            hint_text="Type your query or command here",
            multiline=False,
            size_hint=(1, 0.2),
            font_size=18,  # Ensure text is readable
            padding_y=(10, 10)  # Add padding for better usability
        )
        self.layout.add_widget(self.input_box)
        
        # ScrollView to wrap the response text
        response_container = ScrollView(size_hint=(1, 0.3))
        self.response_label = Label(
            text="Response will appear here.",
            font_size=16,
            size_hint=(1, None),
            height=100,
            text_size=(self.layout.width - 20, None),  # Adjust text wrapping
            halign="center",
            valign="middle"
        )
        response_container.add_widget(self.response_label)
        self.layout.add_widget(response_container)
        
        # Buttons for Submit and Exit
        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=10)
        
        self.submit_button = Button(text="Submit", size_hint=(0.5, 1))
        self.submit_button.bind(on_press=self.process_input)
        button_layout.add_widget(self.submit_button)
        
        self.speak_button = Button(text="Speak", size_hint=(0.5, 1))
        self.speak_button.bind(on_press=self.process_speech)
        button_layout.add_widget(self.speak_button)
        
        self.exit_button = Button(text="Exit", size_hint=(0.5, 1))
        self.exit_button.bind(on_press=lambda instance: (self.animate_button(instance), self.stop()))
        button_layout.add_widget(self.exit_button)
        
        self.layout.add_widget(button_layout)
        
        t.sollu("Ask whatever you want to do")
        return self.layout

    def animate_button(self, button):
        # Create an animation that changes the button size and color
        anim = Animation(size_hint=(0.6, 1), duration=0.1) + Animation(size_hint=(0.5, 1), duration=0.1)
        anim.start(button)

    def process_input(self, instance):
        self.animate_button(instance)  # Animate the button when clicked
        user_input = self.input_box.text.strip().upper()  # Strip whitespace and convert to uppercase
        self.input_box.text = ""  # Clear the input box
        
        if "ROBO" in user_input:
            x = user_input.split()
            response = "Moving robo " + str(x[1:])
        elif "EXIT" in user_input:
            response = "Exiting the program"
            self.response_label.text_size = (self.layout.width, None)  # Update text wrapping dynamically
            self.response_label.text = response  # Update the response label
            t.sollu(response)
            self.stop()
            return
        else:
            user_input = user_input.title()
            response = g.generate(user_input)
        
        self.response_label.text_size = (self.layout.width, None)  # Update text wrapping dynamically
        self.response_label.text = response  # Update the response label
        t.sollu(response)  # Play the voice after updating the response text

    def process_speech(self, instance):
        self.animate_button(instance)  # Animate the button when clicked
        try:
            user_input = s.kelu().upper()
            self.input_box.text = user_input  # Display the recognized speech in the input box
            self.process_input(instance)  # Process the recognized speech
        except Exception as e:
            self.response_label.text = "Error: Could not process speech."
            print(e)

if __name__ == "__main__":
    VoiceAssistantUI().run()
