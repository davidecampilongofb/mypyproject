import random

def main():
    while True:
        try:
            sceltaprimo = int(input("Inserisci il primo numero dei cinque da giocare: \n"))
            sceltasecondo = int(input("Inserisci il secondo numero dei cinque da giocare: \n"))
            sceltaterzo = int(input("Inserisci il terzo numero dei cinque da giocare: \n"))
            sceltaquarto = int(input("Inserisci il quarto numero dei cinque da giocare: \n"))
            sceltaquinto = int(input("Inserisci il quinto numero dei cinque da giocare: \n"))

            print(f"Ecco i tuoi numeri scelti: {sceltaprimo}, {sceltasecondo}, {sceltaterzo}, {sceltaquarto}, {sceltaquinto}")

            # Creiamo una lista con i numeri scelti dall'utente
            listascelti = [sceltaprimo, sceltasecondo, sceltaterzo, sceltaquarto, sceltaquinto]

            # Creiamo i numeri casuali unici
            cinquenumericasuali = set()
            while len(cinquenumericasuali) < 5:  # Continua finché non abbiamo 5 numeri unici
                cinquenumericasuali.add(random.randint(1, 91))

            print(f"I numeri casuali estratti sono: {list(cinquenumericasuali)}")

            # Verifica se i numeri scelti dall'utente sono presenti nei numeri estratti
            numeri_indovinati = set(listascelti) & cinquenumericasuali  # Intersezione tra numeri scelti e numeri estratti

            # Controllo del numero di corrispondenze
            num_indovinati = len(numeri_indovinati)

            if num_indovinati == 5:
                print("Hai fatto Cinquinaaa!!!!!")
            elif num_indovinati == 4:
                print("Hai fatto Quaterna!")
            elif num_indovinati == 3:
                print("Hai fatto Terno!")
            elif num_indovinati == 2:
                print("Hai fatto Ambo!")
            elif num_indovinati == 1:
                print(f"Hai indovinato {num_indovinati} numero!")
            else:
                print("Purtroppo non hai indovinato nessun numero.")

            # Gestione delle opzioni di continuazione o uscita
            while True:
                game = input("Vuoi giocare ancora? Digita 1 per continuare, 2 per chiudere: ")
                if game == '1':
                    print("reload in progress . . .")
                    break  # Se l'utente inserisce '1', riprende il ciclo
                elif game == '2':
                    print("Grazie per aver giocato! Arrivederci.")
                    return  # Esce dalla funzione e termina il programma
                else:
                    print("Errore: opzione non valida. Per favore, inserisci 1 per continuare o 2 per uscire.")

        except ValueError:
            print("Errore: per favore inserisci un numero valido.")
            continue  # Se c'è un errore di input, chiedi di nuovo

if __name__ == "__main__":
    main()
