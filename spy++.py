import socket, threading
import tkinter as tk
from tkinter import StringVar
soc=socket.socket()
shost=socket.gethostname()
ip=socket.gethostbyname(shost)
server_host='192.168.1.1'
port=1234
def listener():
    quote=StringVar()
    quote.set("--BEGIN--")
    sok=socket.socket()
    server_host='totc.ddns.net'
    port=1234
    root = tk.Tk()
    root.title('incoming')
    S = tk.Scrollbar(root)
    T = tk.Text(root, height=4, width=50)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.insert(tk.END, quote)
    tk.mainloop()
    while True:
        quote=quote+soc.recv(1024).decode()+'\n'
try:
    soc.connect((server_host, port))
    print('Connected as probe\n')
    soc.send(b"spy")
except:
    print('server not available! aborting...')
#threading.Thread(target=listener).start()
#while True:
#    msg=input('OUTGOING: ')
#    soc.send(msg.encode())
while True:
    msg=soc.recv(1024)
    print(msg.decode())
