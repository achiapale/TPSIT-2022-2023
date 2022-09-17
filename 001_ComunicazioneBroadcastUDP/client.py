from socket import AF_INET, SOCK_DGRAM, socket

PORT = input("Inserisci il numero della porta: ")
HOST = input("Inserisci l'indirizzo dell'host: ")

def chatClient():
    with socket(AF_INET, SOCK_DGRAM) as s:
        msg = "hello world"
        msg = msg.encode('utf8')
        s.sendto(msg, (f"{HOST}", int(PORT)))


if __name__ == "__main__":
    while True:
        chatClient()