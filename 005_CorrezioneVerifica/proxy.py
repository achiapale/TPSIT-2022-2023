import sys
from socket import socket, AF_INET, SOCK_STREAM

BUF_SIZE = 4096

# classe dove inizializzo i parametri da riga di comando
class Opzioni:
    def __init__(self, portaServer, host, port):
        self.portaServer = int(portaServer)
        self.host = host
        self.port  = int(port)

    def get_socket(self):
        return (self.host, self.port)

def richedi_dati(sock, percorso):
    # apro un altro socket per il client
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(sock)
        print("Richiesta")
        # passo la stringa aggiungendo il .json
        # mando due volte a capo al fondo perchè la richiesta vuole la riga vuota
        s.sendall(f"GET {percorso}.json HTTP/1.0 \n connection: close\n".encode('utf-8'))
        
        # faccio entrare data nel ciclo 
        # poi ricevo tutti i dati fino a quando ce ne sono (data != None)
        data = True
        # creo una lista dove inserire i dati
        dati = []
        print("Ricezione dati")
        while data != None:
            data = s.recv(BUF_SIZE)
            print("Ricevuto")
            data2 = s.recv(BUF_SIZE)
            print("Ricevuto")
            print(data)

            return data + data2

            # concateno tutto quello che mi sta arrivando
            #if data != None:
                # inserisco tutti i dati (buffer) in una lista
                #dati.append(data)
        
        # unisco la lista di buffer
        #dati = b''.join(dati)
        #print(dati)

def main(args):
    # richiamo la classe
    # la posizione 0 = nome del programma (io parto da 1)
    opt = Opzioni(args[1], args[2], args[3])

    # apro il socket
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("0.0.0.0", opt.portaServer))
        s.listen()

        # accetta più di un pacchetto
        while True:
            client, clientAddress = s.accept()
            # ricevo i dati e li stampo
            data = client.recv(BUF_SIZE)
            print(data)

            # trasformo i dati in una stringa e li splitto (voglio ottenere il percorso)
            data =  data.decode('utf-8')
            campi = data.split(" ")
            
            # richiamo la funzione dove passo host, porta e 
            # il percorso, che si trova nella posizione 1 della stringa

            # client
            data = richedi_dati(opt.get_socket(), campi[1])

            # invio i dati al client
            client.sendall(data)



if __name__ == "__main__":
    main(sys.argv)