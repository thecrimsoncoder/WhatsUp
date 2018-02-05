import ipaddress
import os
import subprocess
from colorama import init
init();

def START():
    print("+-------------------------------------+")
    print("|        W H A T S U P . P Y          |")
    print("| By: Sean McElhare (TheCrimsonCoder) |")
    print("+-------------------------------------+")
    user_input = input("Please enter an IP (192.168.1.32) or a CIDR (192.168.1.0/24): ")
    if('/' in user_input):
        print("[IP]             [STATUS]             [DNS]")
        hosts_list = getSubnetHosts(user_input)
        pingSubnetHosts(hosts_list)
    else:
        print("[IP]             [STATUS]             [DNS]")
        pingHost(user_input)
def getSubnetHosts(CIDR):
    return ipaddress.ip_network(CIDR).hosts()
def pingSubnetHosts(LIST):
    for subnetHost in LIST:
        pingHost(str(subnetHost))
    print('\033[1;33;44m' + "~~~~~~~~~~~~~~~~~~~Mission Accomplished!~~~~~~~~~~~~~~~~~~~" + '\033[0m')
def pingHost(IP):
    try:
        PING = subprocess.check_output(['ping',IP],shell=False,encoding = 'utf8')
        if('TTL' in PING):
            DNS = subprocess.check_output(['nslookup',IP],shell=False,encoding = 'utf8')
            if('Name' in DNS):
                DNS = DNS.split()
                print(str(IP) + "       " + '\033[32m' + "ONLINE" + "              " + '\033[0m' + DNS[5])
            else:
                print(str(IP) + "       " + '\033[32m' + "ONLINE" + "              " + '\033[0m' + "Non-Existent")
        elif('unreachable' in PING):
            print(str(IP) + "       " + '\033[1;31;47m' + "UNREACHABLE" + '\033[0m' + "         " + "N/A")
    except subprocess.CalledProcessError as e:
        print(str(IP) + "       " + '\033[1;41;37m' + "OFFLINE" + '\033[0m' + "               " + "N/A")
START();
