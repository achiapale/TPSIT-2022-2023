from socket import AF_INET, SOCK_DGRAM, socket
from packet import Packet

MAXSIZE = 8096

def scriviFile():
    print(pezzi)


def chatServer(pezzi):
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.bind(("0.0.0.0", 5000))

        finito = False

        # lista dei pezzi dei file
        pezzi = []

        while not finito:
            dati, da = s.recvfrom(MAXSIZE)
            pkt = Packet.from_bytes(dati)

            if pkt.stato == Packet.INIZIO:
                # parto dall'inizio
                pezzi = []
            elif pkt.stato == Packet.CONTINUA:
                # aggiungo un pezzo del file nella lista
                pezzi.append(pkt.blocco)
            else:
                # quando il file è stato inviato tutto, lo scrivo
                print("scrittura file")
                scriviFile(b''.join(pezzi))




if __name__ == "__main__":
    chatServer()