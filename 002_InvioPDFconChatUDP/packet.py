# | 1 byte (lunghezza di username) | username | 2 byte (lunghezza message) | message

class Packet:
    def __init__ (self, username, message):
        #validazione
        self.username = username
        self.message = message

    #converte un oggetto Packet in bytes
    def to_bytes(self):
        #array di buffer vuoto
        # oppure buufer = bytes()
        buffer = b''

        username_bytes = self.username.encode('utf8')

        #restituisce la lunghezza in byte del messaggio
        #1 si riferisce al numero di bytes utilizzati; big serve per mettere le cifre più significativa nei byte più piccoli
        buffer = len(username_bytes).to_bytes(1, 'big')
        buffer = buffer + username_bytes

        message_bytes = self.message.encode('utf8')
        buffer = buffer + len(message_bytes).to_bytes(2, "big")
        buffer = buffer + message_bytes 

        return buffer    

    #potrà essere richiamato anche se non ci sono oggetti
    @staticmethod
    def from_bytes(buffer):
        username_size = int.from_bytes(buffer[0:1], 'big')
        username = buffer[1: username_size + 1].decode('utf8')
        message_size = int.from_bytes(buffer[username_size + 1:username_size + 3], "big")
        message = buffer[username_size + 3: username_size + 3 + message_size].decode('utf8')
        return Packet(username, message)


def run_tests():
    pkt0 = Packet("username", "message")
    pkt1 = Packet.from_bytes(pkt0.to_bytes())
    #funzione di python che restituisce vero se i due parmetri sono uguali
    #se sono diversi da un errore e interrompe il programma
    assert(pkt0.message == pkt1.message)
    assert(pkt0.username == pkt1.username)




if __name__ == "__main__":
    run_tests()     