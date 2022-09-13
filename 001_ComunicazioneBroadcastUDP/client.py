from socket import AF_INET, SOCK_DGRAM, socket

PORT = 5000
HOST = "192.168.95.255"

def chatClient():
    with socket(AF_INET, SOCK_DGRAM) as s:
        msg = "hello world"
        msg = msg.encode('utf8')
        s.sendto(msg, (HOST, PORT))


if __name__ == "__main__":
    chatClient()