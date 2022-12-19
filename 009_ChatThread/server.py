import threading
import time
import socket

def answer(client):
    while True:
        msg = client.recv(4096).decode('utf8')
        print(msg)

        try:
            # esegue lo script che viene mandato dal client
            result = eval(msg)
            print(result)
        except:
            print("errore nell'inserimento del messaggio\n")
            client.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(("127.0.0.1", 8000))
    
    s.listen()

    while True:
        client, clientAddress = s.accept()
        print(f"connesso con {clientAddress}")
        
        t = threading.Thread(target = answer, args=(client,))
        t.start()




if __name__ == "__main__":
    main()