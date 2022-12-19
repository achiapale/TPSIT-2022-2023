from socket import socket, AF_INET, SOCK_STREAM
import threading
import time

def server(conn, address):
    try:
        while True:
            print(f"Connesso con {address}")

            # ricevo il messaggio
            msg = conn.recv(4096).decode()

            # verifico che l'utente non voglia chiudere il programma
            if msg == "exit":
                running = False
                print("Chiusura connessione. ")
                conn.sendall(("exit".encode()))
                conn.close()
            else:
            conn.sendall((str(risultato).encode()))
        
    except:
        print("Error")
        

def main():
    # creazione del socket e connessione
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("127.0.0.1", 8000))
    s.listen()

    while True:
        # accetto la connessione
        conn, address = s.accept()
        print(f"Connesso con {address}")

        # creazione dell'oggetto thread
        t = threading.Thread(target=server, args = (conn, address,))
        #faccio partire il thread
        t.start()

if __name__ == "__main__":
    main()