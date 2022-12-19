from socket import AF_INET, SOCK_STREAM, socket
from packet import *
from lettura import *


def chatServer():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("0.0.0.0", 5000))
        s.listen()

        print("Server in ascolto")

        file = []
        while True:
            cient, clientAddress = s.accept()

            packet = Packet.from_bytes(msg)
            if packet.status == Packet.newFile:
                file = []

            if packet.data and len(packet.data) > 0:
                file.append(packet.data)

            if packet.status == Paacket.endFile:
                write(b'', join(file))


if __name__ == "__main__":
    chatServer()


