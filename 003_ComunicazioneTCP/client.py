from socket import AF_INET, SOCK_STREAM, socket

def chatClient(receiver):
    with socket(AF_INET, SOCK_STREAM) as s:
        # connetto il client al server
        # come indirizzo utilizzo il localhost
        s.connect(receiver)
        while True:
        # invio dei dati e codico in utf-8
            s.send("messaggio inviato".encode('utf-8'))


if __name__ == "__main__":
    receiver = ("127.0.0.1", 3450)
    chatClient(receiver)
