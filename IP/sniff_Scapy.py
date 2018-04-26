from scapy.all import *
import pygeoip
from IPy import IP as IPLIB
from socket import *
import time

conversations = {}
exclude_ip = {"10.0.0.18","127.0.0.1"}

def SavetoFile(traceInfo):
    try:
        filename = "Network_Monitor_LOg" + time.strftime("%d_%m_%y") + ".txt"
        fileLog = open(filename,a)
        fileLog.write(traceInfo)
        fileLog.write("\r\n")
        fileLog.write("----------------------------------")
        fileLog.write("\r\n")
        fileLog.close()
    except:
        pass

def getInfo(ipAddress):
    try:
        hostname = gethostbyaddr(ipAddress)[0]
    except:
        hostname = ""

    ip = IPLIB(ipAddress)
    if(ip.iptype()=="PRIVATE"):
        return "private IP,hostname : " + hostname

    try:
        geoip = pygeoip.Geoip('GeoIP.dat')
        ipRecord = geoip.record_by_addr(ipAddress)
        return "Country : %s ,Host : %s "%(country,hostname)
    except:
        return  "Can't Locate " + ipAddress + "Host" + hostname

def printPacket(sourceIP,destinationIP) :
    traceInfo = "[+] Source (%s) : %s -----> Destination (%s):%s" % (sourceIP,getInfo(sourceIP),destinationIP,getInfo(destinationIP))
    print(traceInfo)
    SavetoFile(traceInfo)

def startmonitor():
    try:
        if pkt.haslayer(IP):
            sourceIP = pkt.getlayer(IP).src
            destinationIP = pkt.getlayer(IP).dst

        if (destinationIP in exclude_ip):
            return

        uniquekey = sourceIP + destinationIP
        if(not conversations.has_key(uniquekey)):
            conversations[uniquekey] = 1
            printPacket(sourceIP,destinationIP)

    except (Exception,ex):
        print("Exception + " + str(ex))
        pass

def main():
    sniff(prn = startmonitor(),store = 0,filter = 'ip')

if __name__ == '__main__':
    main()

