import stt as s
import tts as t
import assi as g
import time
t.sollu("Ask whater you want to do")
while 1:
    a = s.kelu()
    a = a.upper()
    if "ROBO" in a:
        x = a.split()
        t.sollu("Moving robo "+str(x[1:]))
    elif "EXIT" in a:
        t.sollu("Exitting the program")
        break
    else:
        a = a.title()
        print(a)
        a = g.generate(a)
        print(a)
        t.sollu(a)