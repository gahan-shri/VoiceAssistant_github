import speech_recognition as st
import pyttsx3 

def say(text):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = st.Recognizer()
    with st.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0)
        print("listening...")
        r.pause_threshold=1
        audio = r.listen(source)
        try:
            print("Recognising...")
            text = r.recognize_google(audio, language ='en-in')
            print(f"User said : {text}\n")
        except Exception as e:
            print(e)
            print("unable to recognise your voice")
            return "sorry i am unable to recognise"
        return text


while True:
    text = takecommand()
    say(text)