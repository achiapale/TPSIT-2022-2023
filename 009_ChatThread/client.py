import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect(("127.0.0.1", 8000))

    while True:
        invia = input("Inserisci nel messaggio da inviare: ")
        s.sendall(invia.encode('utf8'))

    s.close()

if __name__ == "__main__":
    main()