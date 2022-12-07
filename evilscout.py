# A PoC implementation of the EvilScout detection algorithm.
from scapy.all import *
import ipaddress
import argparse
# LEASED IP FILE
BASE_NET = '192.168.0.0/24'
REVERSE_IP = '192.168.12.0/24'

def argsHandler():
    dsc = 'PoC script to validate EvilScout method of detection'
    parser = argparse.ArgumentParser(description=dsc)
    parser.add_argument('-reverse', action='store_true', help='Detection is performed on the PI2B')
    parser.add_argument('-i', help='Select the interface to sniff', required=True)
    args = parser.parse_args()
    return args

def checkPacket(packet,net_ip, twins_list):
    src_flag = True
    dst_flag = True
    
    try:
        src_ip = str(packet[IP].src)
        # Check if IP is in Network
        if not(ipaddress.ip_address(src_ip) in ipaddress.ip_network(net_ip)):
            twin_ip = src_ip
            if not(twin_ip in twins_list):
                twins_list.append(twin_ip)
                print('EvilTwin detected. src addr {}'.format(src_ip))


    except:
        print('Error while trying to read the packet!')



if __name__ == '__main__':
    twins_list = []
    args = argsHandler()
    if(args.reverse):
        net_ip = REVERSE_IP
    else:
        net_ip = BASE_NET

    sniff(iface=args.i, filter='ip', prn=lambda x: checkPacket(x,net_ip,twins_list))
    print('End of script')
