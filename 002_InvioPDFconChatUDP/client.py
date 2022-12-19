from socket import AF_INET, SOCK_DGRAM, socket
from packet import *
import time

# quanti byte leggo ogni volta
BUFSIZE = 10

def invia_file(s, dest):
    with open("prova.pdf", "rb") as f:
        finito = False

        # all'inizio posso inviare un blocco vuoto
        # creo un pacchetto da inviare sulla rete (che inizialmente sarà vuoto)
        s.sendto(b'', Packet(b'', Packet.INIZIO).to_bytes(), dest)

        while not finito:
            # leggo tanti dati quanti sono nella BUFSIZE
            dati = f.read(BUFSIZE)
            if not dati:
                # leggo i dati e li invio in rete (sempre verificando che il file non sia finito)
                s.sendto(b'', Packet(dati, Packet.CONTINUA).to_bytes(), dest)

            
            else:
                # ho finito di leggere il file
                finito = True
                # invio il pacchetto dicendo che ho finito l'invio
                s.sendto(b'', Packet(b'', Packet.FINE).to_bytes(), dest)




def chatClient():
    # indirizzo del destinatario
    dest = ("127.0.0.1", 5000)
    with socket (AF_INET, SOCK_DGRAM) as s:
        invia_file(s, dest)
        
            

if __name__ == "__main__":
    chatClient()