from socket import AF_INET, SOCK_DGRAM, socket
from packet import *


def chatClient(HOST, PORT, NAME):
    running = True
    with socket(AF_INET, SOCK_DGRAM) as s:
        while running == True:
            msg = input("Inserire il messaggio. Se vuoi uscire, digitare 'exit': ")
            if(msg != "exit"):
                running = False
            else:
                pkt = Packet(NAME, MSG)
                s.sendto(pkt.to_bytes(), HOST, PORT)


if __name__ == "__main__":
    HOST = input("Inserisci l'indirizzo dell'host: ")
    PORT = input("Inserisci il numero della porta: ")
    NAME = input("Inserire il nome: ")
    
    while True:
        chatClient(HOST, PORT, NAME)