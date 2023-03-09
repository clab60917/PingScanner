import subprocess
import time

def ping(ip_address):
    res = subprocess.call(["ping", "-c", "1", "-t", "200", ip_address], stdout=subprocess.PIPE)
    return res == 0

ip_addresses = input("Enter IP addresses to ping (separated by spaces): ").split()
while True:
    print("Scanning...")
    for ip_address in ip_addresses:
        if ping(ip_address):
            print(f"{ip_address} is UP")
        else:
            print(f"{ip_address} is down")
    time.sleep(5)
