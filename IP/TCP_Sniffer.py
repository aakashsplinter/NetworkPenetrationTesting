import socket
import struct
from ctypes import *

class IPHeader(Structureucture):
    _fields_ = [
        ("ihl",         c_ubyte,4)
        ("version",     c_ubyte,4)
        ("tos",         c_ubyte)
        ("len",         c_ushort)
        ("id",          c_ushort)
        ("offset",      c_ushort)
        ("ttl",         c_ubyte)
        ("protocol_num",c_ubyte)
        ("sum",         c_ushort)
        ("src",         c_uint32)
        ("dst",         c_uint32)
    ]

    def __new__(self, data = None):
        return self.from_buffer_copy(data)

    def __init__(self,data = None):
        self.source_address = socket.inet_ntoa(struct.pack("@I",self.src))
        self.destination_address = socket.inet_ntoa(struct.pack("@I",self.dst))
        self.protocols = {1:"ICMP",6:"TCP",17:"UDP"}
        try:
            self.protocol = self.protocols(self.protocol_num)
        except:
            self.protocol = str(self.protocol_num)

def initTCPSocket():
    sniffer_tcp = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_TCP)
    sniffer_tcp.bind(("0.0.0.0",0))
    sniffer_tcp.setsockopt(socket.IPPROTO_TCP,socket.IP_HDRINCL,1)
    return sniffer_tcp

def StartSniffing():
    sniffer_tcp = initTCPSocket()
    print "Sniffer is Listening"
    try:
        while True:
            raw_buffer_tcp = sniffer_tcp.recvfrom(65535)[0]
            ip_header_tcp  = IPHeader(raw_buffer_tcp[0,20])
            if(ip_header_tcp.protocol == "TCP"):
                print("Protocol : %s %s -> %s" %(ip_header_tcp.protocol,ip_header_tcp.source_address,ip_header_tcp.destination_address))

    except:
        print("Exiting Program")
        exit(0)


def main()
    StartSniffing()

if __name__ == '__main__':
    main()