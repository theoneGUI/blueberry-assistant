import win32com.client as wincl
from pyautogui import *
import time, random, os,base64,urllib3, datetime, cb1
def say(text):
    speak = wincl.Dispatch("SAPI.SpVoice")
    print(text)
    speak.Speak(text)
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
def keystroke(keys,sec):
    time.sleep(sec)
    typewrite(keys)
def processor(INPUT):
    if "type" in INPUT:
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
    elif INPUT == 'play' or INPUT == 'pause':
        hotkey('playpause')
        if INPUT=='play':
            response='playing...'
        elif INPUT=='pause':
            response='pausing...'
        else:
            response="okay"
    elif INPUT.split(' ')[0] == 'should' and INPUT.split(' ')[1] == 'i':
        response=random.choice(data.shouldi)
    elif INPUT.split(' ')[0] == 'start':
        hotkey('win')
        keystroke(INPUT.replace('start ',''),.5)
        keystroke('\n',2)
        response='Starting '+INPUT.replace('start ','')
    elif INPUT == "how you doing":
        response="I'm doing good baby, how you doin?"
    elif "run" in INPUT:
        hotkey('win')
        keystroke("cmd",1)
        typewrite('\n',3)
        def commandConverter(a):
            new=a.replace('run','')
            cmd=new.replace(' ','').lower()
            b=cmd.replace('space',' ')
            return b
        keystroke(commandConverter(INPUT),1)
        typewrite('\n',1)
        response="Running in CMD"
    elif 'search the web for' in INPUT:
        INPUT.replace('search the web for ',"")
        os.system('chrome "https://google.com/search/{}"'.format(INPUT))
    elif INPUT=="go to sleep":
        print("Sleeping")
        response="Sleeping"
        hotkey("win",'x')
        hotkey("u")
        hotkey('s')
    elif "song request" in INPUT:
        INPUT=INPUT.replace('song request','')
        hotkey('win')
        keystroke('itunes',1)
        hotkey('\n')
        time.sleep(10)
        press('tab',presses=4)
        typewrite(INPUT)
        press('down')
        hotkey('\n')
        time.sleep(2)
        hotkey('\n')
        response="playing {}".format(INPUT)
    elif INPUT=='':
        pass
        response=''
    else:
       response=cb1.chat(INPUT)
    if INPUT=="play" or INPUT == "pause":
        hotkey('pauseplay')
        response='okay'
    return response
