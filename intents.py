import os
from common_ground import *
import speech_recognition as sr
from pyautogui import *
import time, random, os,base64,urllib3, datetime, cb1
import speech_recognition as sr
import time, socket, sys
#Get the hostname, IP Address from socket and set Port
global soc
voice = 2
soc = socket.socket()
shost = socket.gethostname()
#ip = socket.gethostbyname(shost)
#get information to connect with the server
server_host = 'totc.ddns.net'
port = 1234
#print('Trying to connect to the server: {}, ({})'.format(server_host, port))
try:
    soc.connect((server_host, port))
    print("Connected...\n")
    soc.send(b"asst1")
    say('Now connected to NExt')
    soc.recv(1024)
    soc.close()
except OSError:
    say('Peripherals not connecting. All routed commands have been disabled.')
def log(voiceNum):
    with open("voiceNum.log","w+") as file:
        file.write(voiceNum)
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
    from data import *
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
checker=False
def keystroke(keys,sec):
    time.sleep(sec)
    typewrite(keys)
def process(INPUT):
    try:
        soc = socket.socket()
        server_host = 'totc.ddns.net'
        port = 1234
        soc.connect((server_host, port))
        soc.send(b"asst1")
        soc.recv(1024)
        time.sleep(1)
    except:
        pass
    import os, threading
    goodb=['i should have burned this place down when i had the chance','i was just learning to love']
    response='blank'
    try:
        if 'pc command ' in INPUT:
            INPUT='to P1 '+INPUT.replace('pc command ','')
            soc.send(INPUT.encode())
            soc.recv(1024)
            response='command executed successfully'
        elif 'send it to pc ' in INPUT:
            INPUT='to P1 '+INPUT.replace('send it to pc ','')
            soc.send(INPUT.encode())
            soc.recv(1024)
            repsonse="command executed successfully"
        elif 'turn' in INPUT and 'tree' in INPUT:
            INPUT='to LIGHT1 '+INPUT
            soc.send(INPUT.encode())
            soc.recv(1024)
            response='command executed successfully'
        elif 'turn the tree' in INPUT:
            INPUT='to LIGHT1 '+INPUT
            soc.send(INPUT.encode())
            soc.recv(1024)
            response='command executed successfully'
        elif INPUT=="restart next server":
            soc.send("to server restart".encode())
            response='command executed successfully'
    except:
        response="Routed commands have been disabled"
    if "type" in INPUT:
        if response=='command executed successfully' or response =="PC routed commands have been disabled":
            pass
        else:
            keystroke(INPUT.replace("type",""), 5)
            response="I typed it."
    elif "change voice engine to " in INPUT:
        INPUT=INPUT.replace("change voice engine to ", '')
        if INPUT=="espeak" or INPUT=="speak":
            log("1")
            response="wow. I like my new voice"
        elif INPUT=="festival":
            log("2")
            response="wow. I like my new voice"
        elif INPUT=="google":
            log("3")
            response="wow. I like my new voice"
        else:
            response="that is not an engine for me now. Unless I misheard you, in which case please try again."
    elif "type" in INPUT:
        if response=='command executed successfully' or response =="PC routed commands have been disabled":
            pass
        else:
            keystroke(INPUT.replace("type",""), 5)
            response="I typed it."
    elif INPUT == 'rap':
        if response=='command executed successfully' or response =="PC routed commands have been disabled":
            pass
        else:
            response=rap
    elif INPUT == "recite pi":
        if response=='command executed successfully' or response =="PC routed commands have been disabled":
            pass
        else:
            response='''3.1415926535897932384626433832795028841971693993751049445923078164062862089986280348253421170679 is... the... first 100... digits... holy cow that's a lot of numbers!'''
    elif "where is" in INPUT:
        if response=='command executed successfully' or response =="PC routed commands have been disabled":
            pass
        else:
            info = INPUT.split(" ")
            location = info[2]
            import os ; os.system('start chrome https://www.google.nl/maps/place/'+location+'&amp')
            response="Here is "+location
    elif INPUT.split(' ')[0] == 'should' and INPUT.split(' ')[1] == 'i':
        if response=='command executed successfully' or response =="PC routed commands have been disabled":
            pass
        else:
            response=random.choice(shouldi)
    elif INPUT=="i insult you to your face":
        os.system('aplay lizzy.wav')
        response=""
    elif INPUT=="your head is too fat":
        os.system("aplay wounded.wav")
    elif INPUT=="raspberry shutdown authorization right alpha indigo delta":
        say(random.choice(goodb))
        os.system('sudo shutdown now')
        response=""
    elif INPUT == "generate a comment":
        import data
        verb=random.choice(data.verbs)
        noun=random.choice(data.nouns)
        adj=random.choice(data.adjectives)
        response=adj,noun,verb
    elif INPUT == "how you doing" or INPUT == 'how you doin':
        if response=='command executed successfully' or response =="PC routed commands have been disabled":
            pass
        else:
            response="I'm doing good baby, how you doin?"
    elif 'search the web for' in INPUT:
        if response=='command executed successfully' or response =="PC routed commands have been disabled":
            pass
        else:
            def search():
                os.system('chromium-browser "https://www.google.com/search?q={}"'.format(INPUT.replace('search the web for ','')))
            threading.Thread(target=search).start()
            response="Searching..."
    elif INPUT.split(' ')[0] in questionIndicators and INPUT != "how you doing":
        if response=='command executed successfully' or response =="PC routed commands have been disabled":
            pass
        else:
            response=cb1.chat(INPUT)
    elif INPUT.split(' ')[0] =="are" and INPUT.split(' ')[1] == 'you':
        if response=='command executed successfully' or response =="PC routed commands have been disabled":
            pass
        else:
            response=knowledge(INPUT,offline)
    elif "simon says" in INPUT:
        if response=='command executed successfully' or response =="PC routed commands have been disabled":
            pass
        else:
            response=INPUT.replace("simon says ",'')
    elif INPUT=="hello there":
        os.system('aplay hellothe.wav')
        response=""
    elif INPUT=='nevermind':
        response=''
    elif INPUT=='reconnect':
            try:
                try:
                    soc.close()
                except:
                    pass
                soc = socket.socket()
                server_host = 'totc.ddns.net'
                port = 1234
                soc.connect((server_host, port))
                print("Connected...\n")
                soc.send(b"asst1")
                say('Now connected to NExt')
                soc.recv(1024)
            except:
                response="NExt server still down."
    else:
    #    response="Please rephrase the request."
        if response=='command executed successfully' or response == "PC routed commands have been disabled":
            pass
        else:
            response=cb1.chat(INPUT)
            if response == 'exitting. shutdown now':
                try:
                    soc.send(response.encode())
                except:
                    pass
                os.system('python3 test.py')
                exit()
            elif response == '.lern':
                try:
                    soc.send('exitting. shutdown now'.encode())
                except:
                    pass
                os.system('python3 Learn.py')
                exit()
            else:
                pass
    try:
        soc.send(b'server heartbeat')
        check=soc.recv(1024)
        check=check.decode()
        if check=="{quit}":
            response=response+". and the NExt server went down by the way, so routed commands disabled until further notice."
            checker=True
        elif check=='':
            pass
    except:
        checker=True
    try:    
        if checker == True:
            try:
                soc.connect((server_host, port))
                print("Connected...\n")
                soc.send(b"asst1")
                soc.recv(1024)
                say('Now connected to NExt')
                checker=False
                say("NExt is back online. Routed commands enabled.")
            except:
                pass
    except:
        pass
    #try:
    #    soc.send(b'.leeve')
    #    soc.close()
    #except:
    #    pass
    
    return response
