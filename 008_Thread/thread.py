import threading
import time

def funzione():
    # la funzione threading.current_thread() legge il nome della funzione in esecuzione
    print(f"Partenza", threading.current_thread().name, "\n")
    print(f"Elaborazione", threading.current_thread().name, "\n")
    time.sleep(2)
    print(f"Lavoro finito", threading.current_thread().name, "\n")


def main():
    # punta all'indirizo della cella a cui punta la funzione
    # print(funzione)

    # creo un oggetto thread
    # target serve per far girare il metodo run (che in questo caso fa partire funzione)
    # args passa i parametri che si richiamano nella funzione
    t = threading.Thread(target = funzione)

    # richiamo la funzione start del thread
    t.start()

    #per avere un flusso più controllato (finisce il thread prima di passare ad un altro)
    t.join()

    t2 = threading.Thread(target = funzione)
    t2.start()

    t2.join()

    funzione()


if __name__ == "__main__":
    main()