from socket import AF_INET, SOCK_STREAM, socket

def chatClient():
    with socket(AF_INET, SOCK_STREAM) as s:
        address = ("127.0.0.1", 3450)
        print(address)
        
        s.connect(address)
        
        s.send("avanti".encode())
        
    chatClient()