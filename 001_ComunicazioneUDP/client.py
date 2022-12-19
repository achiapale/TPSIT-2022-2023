from socket import AF_INET, SOCK_DGRAM, socket
from packet import *


def chatClient(HOST, PORT, NAME):
    running = True
    with socket(AF_INET, SOCK_DGRAM) as s:
        while running == True:
            msg = input("Inserire il messaggio. Se vuoi uscire, digitare 'exit': ")
            if(msg.lower() != "exit"):
                break
    
            pkt = Packet(NAME, MSG)
            buffer = msg.to_bytes()
            print(buffer)
            
            s.sendto(buffer, (HOST, int(PORT)))


if __name__ == "__main__":
    HOST = input("Inserisci l'indirizzo dell'host: ")
    PORT = input("Inserisci il numero della porta: ")
    NAME = input("Inserire il nome: ")
    
    while True:
        chatClient(HOST, PORT, NAME)