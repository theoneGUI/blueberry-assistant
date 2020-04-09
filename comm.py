print('setting up')
from win10toast import ToastNotifier 
  
# create an object to ToastNotifier class 
n = ToastNotifier() 
  
n.show_toast("Blueberry", "Preparing NExt satellite...", duration = 3) 
 #icon_path ="http://totc.ddns.net/images/t.png")
import time, sys, understanding,os, threading
import win32com.client as wincl
def say(text):
    speak = wincl.Dispatch("SAPI.SpVoice")
    print(text)
    speak.Speak(text)
import socket
soc=socket.socket()
shost=socket.gethostname()
ip=socket.gethostbyname(shost)
server_host='totc.ddns.net'
port=1234
dev_name="P1"
try:
    print("connecting...")
    soc.connect((server_host, port))
    print('Connected as {}\n'.format(dev_name))
    soc.send(dev_name.encode())
except:
    print('server not available! trying again...')
    while True:
        try:
            print("connecting...")
            soc.connect((server_host, port))
            print('Connected as {}\n'.format(dev_name))
            soc.send(dev_name.encode())
            break
        except:
            pass
#get a connection from client side
print('blueberry has connected.')
def toast(message):
    n.show_toast("Blueberry",message)
while True:
   message = soc.recv(1024)
   message = message.decode()
   if message=="{quit}":
       os.system(r"pythonw C:\Users\Aidan\Desktop\incoming\comm.py")
       exit()
   elif message=="{} life check".format(dev_name):
       soc.send(b'{} online'.format(dev_name))
   elif message=="Greetings from the cave!":
       pass
   elif "to {} ".format(dev_name) in message:
       message=message.replace("to {} ".format(dev_name),'')
       print(message)
       thread1=threading.Thread(target=toast(message))
       thread1.start()
       say(understanding.processor(message))
       msg="received and executed"
       msg=msg.encode()
       soc.send(msg)
       thread1.join()
   else:
       print(message)
