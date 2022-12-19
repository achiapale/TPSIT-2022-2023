from socket import socket, AF_INET, SOCK_STREAM
import threading
import time

# creo una classe thread che eredita dalla classe Thread
class MyClassThread(threading.Thread):
    # costruttore
    def __init__(self, conn):
        # richiamo il metodo della classe padre
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        while True:
            # ricezione del messaggio
            ricevi = self.conn.recv(4096).decode()
            print(ricevi + " da " + threading.current_thread().name)

            # prendo in input la risposta e la invio
            risp = input("Inserisci una risposta a: ")
            self.conn.sendall(risp.encode())

            # verifico che non si voglia uscire dal programma
            if ricevi.lower() == "exit":
                running = False
                conn.sendall(("exit".encode()))
                conn.close()
        


def main():
    # creo il socket e mi metto in ascolto
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("127.0.0.1", 8000))
    s.listen()

    while True:
        # accettto la connessione 
        conn, address = s.accept()
        print(f"Connesso con {address}")
        
        # creo l'oggetto richiamando il messaggio
        t = MyClassThread(conn)

        t.start()

if __name__ == "__main__":
    main()