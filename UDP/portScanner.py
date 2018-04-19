import argparse
from socket import *

def printBanner(connSock,tgtport):
    try:
        if(tgtport == 80):
            connSock.send(" GET HTTP/1.1 \r\n")
        else:
            connSock.send(" \r\n")

        results = connSock.recv(4096)
        print('Banner :' + str[results])
    except:
        print('Banner not Available')
def connScanTCP(tgtHost,tgtPort):
    try:
        connSock = socket(AF_INET,SOCK_STREAM)
        connSock.connect(tgtHost,tgtPort)
        print(' %d TCP Open ' % tgtPort)
        printBanner(connSock,tgtPort)
    except:
        print(' %d Port Closed ' % tgtPort)

    finally:
        connSock.close()
def connScanUDP(tgtHost,tgtPort):
    try:
        connSock = socket(AF_INET,SOCK_DGRAM)
        connSock.connect(tgtHost,tgtPort)
        print('% %d UDP Open ' % tgtPort)
        printBanner(connSock,tgtPort)
    except:
        print(' %d UDP Closed ' % tgtPort)
def portScan(tgtHost,tgtPorts,isUDP):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('Error : Unknown Host ')
        exit(0)

    try:
        tgtName = gethostbyaddr(tgtIP)
        print(tgtName)
    except:
        print('Scan Result ' + tgtIP + '..')

    setdefaulttimeout(10)

    for tgtPort in tgtPorts:
        if not isUDP:
            connScanTCP(tgtHost,int(tgtPort))
        else:
            connScanUDP(tgtHost,int(tgtPort))
def main():
    parser = argparse.ArgumentParser("Smart Port SCanner")
    parser.add_argument("-a","--address",type=str,help="Target IP address")
    parser.add_argument("-p","--port",type=str,help="TargetIPAddress")
    parser.add_argument("-u","--udp",help="Include a UDP Port Scan",action="Store_True")
    args = parser.parse_args()
    ipaddress = args.address
    portNumber= args.port.split(",")
    isUDP = args.udp
    portScan(ipaddress,portNumber,isUDP)
if __name__ == '__main__':
    main()