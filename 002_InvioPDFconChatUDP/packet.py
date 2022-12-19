class Packet:
    INIZIO = 0
    CONTINUA = 1
    FINE = 2

    # costruttore
    def __init__(self, blocco, stato):
        self.blocco = blocco
        self.stato = stato


    # decodifica dei messaggi 
    def to_bytes(self):
        # il numero che passo è la quantità di byte che occupa la variabile
        return b''.join([self.stato.to_bytes(1, "big"),
                len(self.blocco).to_bytes(2, "big"), self.blocco])

    # codifica dei messaggi con un metodo statico (non prende parametri)
    @staticmethod
    def from_bytes(buffer):
        # leggo il primo byte e lo converto in intero; stesso procedimento per la lunghezza e il blocco (che va da 3 fino alla sua lunghezza)
        stato = int.from_bytes(buffer[0:1],'big')
        lungh = int.from_bytes(buffer[1:3], 'big')
        blocco = buffer[3: 3+lungh], 'big'

        return Packet[blocco, stato]


if __name__ == "__main__":
    # istanzio un oggetto
    pkt = Packet(b'ciao', False)
    print(pkt.to_bytes())

    buffer = pkt.from_bytes()
    pkt2 = Packet.from_bytes(buffer)

    # test per vedere se la codifica e la decofica restituiscono la stessa cosa
    assert(pkt.stato == pkt2.stato)
    assert(pkt.blocco == pkt2.blocco)