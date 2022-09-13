from socket import AF_INET, SOCK_DGRAM, socket

#byte che voglio leggere
BUFFER_SIZE = 1024

# interfaccia su cui vogiamo ascoltare
# possibilità:  1. localhost (127.0.0.1)
#               2. indirizzo di una mia interfaccia -> utile perchè se si hanno più schede di rete si hanno più ip

HOST = "0.0.0.0"

# > di 1024
PORT = 5000

mystr = "ciao" # oggetto di tipo stringa

# per trasferire dei dati si utilizzano i bytes (in utf8) e non le stringhe
# oggetto di tipo bytes -> array di byte

def chatServer():
    while True:
    # quando si esce da with il socket viene automaticamente chiuso
    # non serve al fondo mettere s.close()
        with socket(AF_INET, SOCK_DGRAM) as s:
            # nel bind si passa una tupla, non si possono aggiungere altri elementi
            s.bind((HOST, PORT))
            msg = s.recvfrom(BUFFER_SIZE)
            # msg è un bytes, ma noi lo vogliamo in stringa
            msg = msg[0].decode('utf8')
            print(msg)


# eseguito solo da terminale
if __name__ == "__main__":
    chatServer()