from socket import AF_INET, SOCK_DGRAM, socket
from packet import *


def chatServer(buffer):
    running = True
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind((buffer))
        while running == True:
            buffer = s.recvfrom(BUFFER_SIZE)
            pkt = Packet.from_bytes(buffer[:4096])
            print(ptk.buffer)


# eseguito solo da terminale
if __name__ == "__main__":
    chatServer(buffer)