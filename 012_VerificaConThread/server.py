from socket import socket, AF_INET, SOCK_STREAM
import threading

# dimensione massima dei messaggi che possono essere ricevuti
BUFSIZE = 1024

# questa funzione legge il file e restituisce l'host e la porta di client e server
def leggiFile():
    file = open("confserver.txt", "r")
    righe = file.readlines()
    file.close()

    file2 = open("confserver.txt", "r")
    righe2 = file2.readlines()
    file2.close()

    return righe[0], righe[1], righe2[0], righe2[1]

class Connection(threading.Thread):
    # costruttore
    def __init__(self, client):
        # richiamo il metodo della classe padre
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        # ricezione del messaggio
        data = self.client.recv(BUFSIZE).decode()
        print(data + " da " + threading.current_thread().name)

        # verifico che l'utente non voglia chiudere il programma
        if data.lower() == "exit":
            print("CHiusura della connessione. \n")
            client.cose()

        else:
            # splitto i dati ricevuti
            data = data.split(";")

            # se il primo dato è salva, allora inserisco nella lista user e messaggio
            if data[0] == "salva":
                lista.append((data[1], data[2]))
                print(lista)

            # se il primo dato è leggi, invio il primo messaggio che mi è stato inviato
            if data[0] == "leggi":
                inviaMessaggioVecchio(s, lista)


# invio al client il messaggio più vecchio (con la funzione pop[0])
def inviaMessaggioVecchio(s, lista):
    print(lista.pop[0])
    s.sendall(lista.pop[0]).encode('utf8')


def main(lista):
    # richiamo la funzione del file epr trovare host e porta
    portS, hostS, portC, portC = leggiFile()

    # apro il socket e faccio il bind con i valori letti da file
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((hostS, int(portS)))

        # il server è in continuo ascolto
        while True:
            # metto il server in ascolto
            s.listen()

            # accetto la richiesta di connessione
            client, clientAddress = s.accept()

            # creazione del thread
            t = Connection(client)
            t.start()            


if __name__ == "__main__":
    lista = []
    main(lista)