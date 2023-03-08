import concurrent.futures
import subprocess
import time

ip_list = ["104.110.240.88", "18.66.112.92", "10.0.0.1"]

def ping(ip_address):
    res = subprocess.call(["ping", "-c", "1", "-t", "200", ip_address], stdout=subprocess.PIPE)
    return res == 0

def ping_ips(ip_list):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = {executor.submit(ping, ip): ip for ip in ip_list}
        for future in concurrent.futures.as_completed(results):
            ip = results[future]
            if future.result():
                print(f"{ip} is UPPPP")
            else:
                print(f"{ip} is down")

while True:
    print("Scanning...")
    ping_ips(ip_list)
    time.sleep(5)
