from socket import socket, AF_INET, SOCK_STREAM

def main():
    # creo il socket e connetto con il server
    cl = socket(AF_INET, SOCK_STREAM)
    cl.connect(("127.0.0.1", 8000))

    running = True
    while running:
        try:
            # chiedo in input l'operazione da fare
            operazione = input("Inserisci operazione (exit per uscire): ")
            cl.sendall(operazione.encode())

            # ricevo la risposta e la stampo
            risp = cl.recv(4096).decode()
            print(risp)
        except:
            running = False

if __name__ == "__main__":
    main()