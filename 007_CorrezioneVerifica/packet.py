class Packet:
    def __init__(self, comando, utente, messaggio):
        self.comando = comando
        self.utente = utente
        self.messaggio = messaggio

    def encode(self):
        res = self.comando + ";" + self.utente + ";" + self.messaggio
        return res.encode()
    
    @staticmethod
    def decode(buffer):
        strPacchetto = buffer.decode()
        campi = strPacchetto.split(";")
        comando = campi[0]
        utente = campi[1]
        messaggio = campi[2]
        return Packet(comando, utente, messagio)


    

