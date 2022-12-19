from socket import socket, AF_INET, SOCK_STREAM
import threading

# classe server
def server(conn, addr):
    while conn:
        # ricevo il messaggio
        msg = conn.recv(4096).decode('utf-8')

        # verifico che il messaggio non sia exit
        # se è exit, chiudo la connessione
        if msg.upper() == "EXIT":
            print("Connessione chiusa. ")
            conn.send(msg.encode("utf-8"))
            conn.close()
            break
        else:
            # eseguo nel try per evitare errori nell'eval
            try:
                result = eval(msg) 
                # print(result)

                # calcolo la tabellina
                tabellina = []
                for i in range(0, 11):
                    tabellina.append(result * i)

                    print(f"{msg} * {i} =  {tabellina[i]}")
    
    
                # invio il messaggio
                conn.sendall(str(tabellina).encode("utf-8"))

            except:
                # se genero un errore, stampo il messaggio d'errore
                print("Errore. ")

def main():
    # creazione del socket
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("127.0.0.1", 8000))
    s.listen()


    # accetto la connessione
    conn, addr = s.accept()
    print(f"Connesso con {addr}.")

    # creazione del thread
    t = threading.Thread(target=server, args=(conn, addr))
    t.start()

        
if __name__ == "__main__":
    main()