from socket import AF_INET, SOCK_DGRAM, socket
from packet import *

def chatClient():
    with open("prova.pdf", "rb") as f:
        buffer = f.read()
        #verifico che il tipo del buffer sia bytes
        #print(type(buffer))

        #boolean che verifica se il file è finito
        finito = False

        #mando ogni volta 4 byte
        min = 0
        max = min+4096

        with socket(AF_INET, SOCK_DGRAM) as s:
            while(finito == False):
                pkt = Packet(buffer[min:max])
                s.sendto(pkt.to_bytes())
        min = max

#lancio il programma
if __name__ == "__main__":
    chatClient()