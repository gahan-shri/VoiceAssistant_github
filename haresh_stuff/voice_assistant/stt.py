import speech_recognition as sp
def kelu():
    r = sp.Recognizer()
    with sp.Microphone() as source:
        print("Please say something:")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
            return text
        except Exception as e:
            print(e)
            print("Sorry, I did not understand that.")
            return "say 0"