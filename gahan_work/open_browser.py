import os

def command(text):
    if "open" in text:
        text = text.replace("open","")
        if 'Notepad' or 'notepad' in text:
            os.startfile('C:\\WINDOWS\\system32\\Notepad') ##notepad file location
    elif "close" in text:
        text = text.replace("close","")
        if 'Notepad' or 'notepad' in text:
            os.system("TASKKILL /F /IM Notepad.exe") ##Notepad.exe matu change paniko 





command("open Notepad")
# command("close Notepad")