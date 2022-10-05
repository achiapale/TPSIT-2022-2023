from socket import AF_INET, SOCK_DGRAM, socket
from packet import *

#byte che voglio leggere
BUFFER_SIZE = 1024

HOST = "127.0.0.1"
PORT = 5000
# interfaccia su cui vogiamo ascoltare
# possibilità:  1. localhost (127.0.0.1)
#               2. indirizzo di una mia interfaccia -> utile perchè se si hanno più schede di rete si hanno più ip


# per trasferire dei dati si utilizzano i bytes (in utf8) e non le stringhe
# oggetto di tipo bytes -> array di byte

def chatServer(HOST, PORT):
    running = True
    # quando si esce da with il socket viene automaticamente chiuso
    # non serve al fondo mettere s.close()
    with socket(AF_INET, SOCK_DGRAM) as s:
        # nel bind si passa una tupla, non si possono aggiungere altri elementi
        s.bind((HOST, PORT))
        while running == True:
            msg = s.recvfrom(BUFFER_SIZE)
            print(msg)
            pkt = Packet.from_bytes(msg[0])
            print(f"l'username: ", {pkt.username}, " ha inviato il messaggio: ", {pkt.message})


# eseguito solo da terminale
if __name__ == "__main__":
    chatServer(HOST, PORT)