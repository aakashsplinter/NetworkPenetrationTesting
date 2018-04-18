import argparse
import threading
import socket

def ServeClient(ClientToServeSocket,clientIPAddress,portNumber):
    clientRequest = ClientToServeSocket.recv(4096)
    print(' Received Data from Client IP add : %s Port : %d Request : %s' % (clientIPAddress, portNumber,clientRequest))
    ClientToServeSocket.send(" I am server")
    ClientToServeSocket.close()

def StartServer(portNumber):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind("0.0.0.0",portNumber)
    server.listen(10)
    print ("Listening Locally on port %d " %portNumber)

    while True:
        client.Address = server.accept()
        print ("Connected with Client : %s:%d " %(Address[0],Address[1]))
        ServeClientThread = threading.Thread(target=ServeClient,args=(client,Address[0],Address[1]))
        ServeClientThread.start()

def main():
    parser = argparse.ArgumentParser(" TCP Server Listener")
    parser.add_argument("-p","--port",type=int,help="Port Number to Listen to",default=4444)
    args = parser.parse_args()
    portNumber = args.port
    StartServer(portNumber)
