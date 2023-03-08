import subprocess
import time

# Liste d'adresses IP à pinguer
ip_list = ["104.110.240.88", "18.66.112.92", "10.0.0.1"]

# Fonction pour effectuer un ping et retourner True si l'hôte est accessible, False sinon
def ping(ip_address):
    res = subprocess.call(["ping", "-c", "1", "-t", "200", ip_address], stdout=subprocess.PIPE)
    return res == 0

# Boucle infinie pour pinger en continu
while True:
    print("Scanning...")
    for ip_address in ip_list:
        if ping(ip_address):
            print(f"{ip_address} is up")
        else:
            print(f"{ip_address} is down")
    time.sleep(5) # Attendre 5 secondes avant de repinger
