from socket import AF_INET, SOCK_STREAM, socket
from packet import *

def chatClient(receiver):
    with socket (AF_INET, SOCK_STREAM) as s:
        s.connect(receiver)

        with open("prova.pdf", "rb") as f:
            s.sendall(Packet(Packet.newFile, b'').to_bytes(), receiver)

            data = True

        while data:
            data = f.read(4096)
            if data:
                s.sendto(Packet(Packet.goOn, data).tobytes(), receiver)
                s.sendto(Packet(Packet.endFile, b'').tobytes(), receiver)


if __name__ == "__main__":
    receiver = ("0.0.0.0", 5000)
    chatClient(receiver)
