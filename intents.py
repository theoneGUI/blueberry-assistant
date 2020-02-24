import os
from common_ground import *
import speech_recognition as sr
from pyautogui import *
import time, random, os,base64,urllib3, datetime, cb1
import speech_recognition as sr
import time, socket, sys
#Get the hostname, IP Address from socket and set Port

http=urllib3.PoolManager()
greetings=("hi","good to see you", "greetings","yo","hey dare","sup","hello")
questionIndicators=("who", "what","when",'where','why','how')
try:
    ds=http.request("GET",'https://google.com').data
    offline=False
except:
    print("offline: adapting...")
    offline=True
try:
    import data
except:
    print('fatal error: data file not found')
    time.sleep(2)
    print('forced to exit...')
    exit()
def listen():
    try:
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            print("listening")
            audio = r.listen(source)
            r.adjust_for_ambient_noise(source)
        print("transcribing...")
        dialog=r.recognize_google(audio).lower()
        return dialog
    except sr.UnknownValueError:
        say("Say again?")

def keystroke(keys,sec):
    time.sleep(sec)
    typewrite(keys)
def process(INPUT):
    import os, threading
    try:
        if 'send to pc ' in INPUT:
            INPUT=INPUT.replace('send to pc ','')
            soc.send(INPUT.encode())
            soc.recv(1024)
            response='command executed successfully'
        elif 'send it to computer ' in INPUT:
            INPUT=INPUT.replace('send it to computer ','')
            soc.send(INPUT.encode())
            soc.recv(1024)
            response='command executed successfully'
        elif 'send it to pc ' in INPUT:
            INPUT=INPUT.replace('send it to pc ','')
            soc.send(INPUT.encode())
            soc.recv(1024)
            response='command executed successfully'
        elif 'send to computer ' in INPUT:
            INPUT=INPUT.replace('send to computer ','')
            soc.send(INPUT.encode())
            soc.recv(1024)
            response='command executed successfully'
    except:
        response="PC routed commands have been disabled"
    if "type" in INPUT:
        keystroke(INPUT.replace("type",""), 5)
        response="I typed it."
    elif "type" in INPUT:
        keystroke(INPUT.replace("type",""), 5)
        response="I typed it."
    elif INPUT == 'rap':
        response=data.rap
    elif INPUT == "recite pi":
        response='''3.1415926535897932384626433832795028841971693993751049445923078164062862089986280348253421170679 is... the... first 100... digits... holy cow that's a lot of numbers!'''
    elif "where is" in INPUT:
        data = INPUT.split(" ")
        location = data[2]
        import os ; os.system('start chrome https://www.google.nl/maps/place/'+location+'&amp')
        response="Here is "+location
    elif INPUT.split(' ')[0] == 'should' and INPUT.split(' ')[1] == 'i':
        response=random.choice(data.shouldi)
    elif INPUT == "how you doing" or INPUT == 'how you doin':
        response="I'm doing good baby, how you doin?"
    elif 'search the web for' in INPUT:
        def search():
            os.system('chromium-browser "https://www.google.com/search?q={}"'.format(INPUT.replace('search the web for ','')))
        threading.Thread(target=search).start()
        response="Searching..."
    elif INPUT.split(' ')[0] in questionIndicators and INPUT != "how you doing":
        response=cb1.chat(INPUT)
    elif INPUT.split(' ')[0] =="are" and INPUT.split(' ')[1] == 'you':
        response=data.knowledge(INPUT,offline)
    elif "simon says" in INPUT:
        response=INPUT.replace("simon says ",'')

    else:
    #    response="Please rephrase the request."
        response=cb1.chat(INPUT)
        if response == 'exitting. shutdown now':
            try:
                soc.send(response.encode())
            except:
                pass
            os.system('python test.py')
            exit()
        elif response == '.lern':
            try:
                soc.send('exitting. shutdown now'.encode())
            except:
                pass
            os.system('python Learn.py')
            exit()
        else:
            pass
    return response
