from socket import socket, AF_INET, SOCK_STREAM
import threading


def main():
    # creo il socket
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("127.0.0.1", 8000))
    
    while True:
        # richiedo in input il valore, lo codifico e invio al server
        operazione = input("Inserisci un valore; digitare EXIT per chiudere il programma. ")
        client.sendall(operazione.encode("utf-8"))

         
        #ricevo il messaggio
        risposta = client.recv(4096)
        
        risposta = risposta.decode("utf-8")

        # verifico che non si voglia chiudere il programma
        if risposta.upper() == "EXIT":
            print("Connessione chiusa. ")
            client.close()
            break
        else:
            # stampo il messaggio ricevuto
            print(f"Tabellina del {operazione}: {risposta}\n")


if __name__ == "__main__":
    main()