from socket import socket, AF_INET, SOCK_STREAM
import sys
import threading

# dimensione massima dei messaggi che possono essere ricevuti
BUFSIZE = 1024

# questa funzione legge il file e restituisce l'host e la porta sia del client che del server
def leggiFile():
    file = open("confclient.txt", "r")
    righe = file.readlines()
    file.close()

    file2 = open("confserver.txt", "r")
    righe2 = file2.readlines()
    file2.close()

    return righe[0], righe[1], righe2[0], righe2[1]



# classe opzioni per prendere parametri da riga di comando
class Opzioni:
    def __init__(self, message):
        self.message = message

# funzione che verifica che il messaggio sia corretto
# in base al messggio svolge due operaizoni differenti
def verificaMessagio(s, message, host, port):
    # verifico se l'utente vuole chiudere il programma
    if message.lower() == "exit":
        print("Chiusura della connessione. \n")
        s.sendall(message.encode("utf-8"))
        s.close()
    # se npn vuole chiudere il programma, verifico quale operazione svolgere
    elif message.lower() == "salva":
        # se l'utente inserisce salva, invio il comando 'salva' (per ricordare all'utente cosa ha inserito),
        # il messaggio e lo user che richiedo in input
        user = input("Inserire il nome utente: ")
        mex = input("Inserire il messaggio: ")
        s.sendall(f"{message};{user};{mex}".encode('utf8'))
        s.close()

    elif message.lower() == "leggi":
        
        # ricevo i dati dal server
        data = s.recv(BUFSIZE).decode('utf8')

        # mostra a schermo i messaggi appena ricevuti dal server
        print(data)

    # mssaggio di errore se il messaggio da riga di comando è errato
    else:
        print("Il comando inserito non è valido. Riprovare\n")
        

# funzione main (a cui passo args per leggere i dati da riga di comando)
def main(args):
    # classe opzioni con il messaggio
    opt = Opzioni(args[1])
    # trovo host e porta dal file
    portC, hostC, portS, hostS = leggiFile()
    
    # apro il socket
    with socket(AF_INET, SOCK_STREAM) as s:
        
        # connetto il socket
        s.connect((hostC, int(portC)))
    
        # verifico che il messaggio sia corretto
        verificaMessagio(s, opt.message, hostS, portS)


if __name__ == "__main__":
    main(sys.argv)