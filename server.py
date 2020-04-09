#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import datetime, os
def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    try:
        name = client.recv(BUFSIZ).decode("utf8")
        msg = "%s has joined this server" % name
        broadcast(bytes(msg, "utf8"))
        clients[client] = name
        while True:
            msg = client.recv(BUFSIZ)
            if msg.decode() == 'to server restart':
                os.system('python3 server.py')
                exit()
            broadcast(msg)
    except ConnectionResetError:
        print("client forcibly left {}".format(datetime.datetime.now()))
        #broadcast(b"{quit}")
        #os.system("python3 server.py")
        #broadcast(msg)
        #print(str(msg))
        #'''
        #else:
        #    client.send(bytes("{quit}", "utf8"))
        #    client.close()
        #    del clients[client]
        #    broadcast(bytes("%s has left the chat." % name, "utf8"))
        #    break
        #'''

def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    print(msg)
    for sock in clients:
        try:
            sock.send(bytes(prefix,'utf8')+msg)
        except:
            print("individual send failed for client {}".format(sock))



clients = {}
addresses = {}

HOST = ''
PORT = 1234
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
while True:
    try:
        if __name__ == "__main__":
            SERVER.listen(5)
            print("Waiting for connection...")
            ACCEPT_THREAD = Thread(target=accept_incoming_connections)
            ACCEPT_THREAD.start()
            ACCEPT_THREAD.join()
            SERVER.close()
    except:
        print("server fault. unhandled disconnect. restarting...")
        print("time: {}".format(datetime.datetime.now()))

