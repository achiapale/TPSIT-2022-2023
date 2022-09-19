from socket import AF_INET, SOCK_DGRAM, socket

def chatClient(HOST, PORT, MSG):
    with socket(AF_INET, SOCK_DGRAM) as s:
        MSG = MSG.encode('utf8')
        s.sendto(MSG, (f"{HOST}", int(PORT)))



if __name__ == "__main__":
    HOST = input("Inserisci l'indirizzo dell'host: ")
    PORT = input("Inserisci il numero della porta: ")
    MSG = input("Inserire il messaggio: ")
    while True:
        chatClient(HOST, PORT, MSG)