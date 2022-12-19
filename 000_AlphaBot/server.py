from socket import AF_INET, SOCK_STREAM, socket
import time
from AlphaBot import AlphaBot

def chatServer():
    with socket(AF_INET, SOCK_STREAM) as s:
    
        s.bind(("0.0.0.0", 3450))
        
        ab = AlphaBot()

        s.listen()
        print("In Ascolto")
        
        client, clientAddress = s.accept()
        
        while True:
            msg = client.recv(1024).decode('utf8')
            
            if(msg == 'avanti'):
                print('sto andando avanti')
                ab.forward()
                time.sleep(3)
                ab.stop()
                ab.right()
                time.sleep(3)
                ab.stop()


if __name__ == "__main__":
    chatServer()
