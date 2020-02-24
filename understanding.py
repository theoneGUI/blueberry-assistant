import os, intents, threading
import speech_recognition as sr
from common_ground import *
def listen():
    try:
        with mic as source:
            os.system('aplay computerbeep_73.wav > /dev/null')
            print("listening")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        print("processing...")
        os.system('aplay computerbeep_55.wav > /dev/null')
        dialog=r.recognize_google(audio).lower()
        print(dialog)
        resp=intents.process(dialog)
        os.system('aplay computerbeep_75.wav > /dev/null')
        say(resp)
        if resp == 'exitting...':
            exit()
        return dialog
    except sr.UnknownValueError:
        say("")
r = sr.Recognizer()
mic = sr.Microphone()

listen()
