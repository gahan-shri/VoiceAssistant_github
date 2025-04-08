import pyttsx3

def say(text):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voices',voice[0].id)
    engine.say(text)
    engine.runAndWait()

while True:
    text = input(print("type any line you just wanted to spell"))
    say(text)