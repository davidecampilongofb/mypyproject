import random

def imposta_pin():
    while True:
        scegli_pin = input("Scegli il PIN di 4 cifre del tuo conto corrente: \n")
        if scegli_pin.isdigit() and len(scegli_pin) == 4:
            print(f"✅ PIN salvato correttamente: {scegli_pin}")
            return scegli_pin
        else:
            print("❌ Input non valido. Riprova.")

def gestisci_conto(scegli_pin):
    tentativi = 0
    while tentativi < 3:
        accesso = input("Inserisci il PIN per accedere (3 tentativi): \n")
        if accesso == scegli_pin:
            saldo = random.randint(-100, 1000)
            print(f"Bentornato. Il tuo saldo è: {saldo}")

            tentativi2 = 0
            while True:

                scelta = input("Scelta operazione: 1.Prelievo 2.Deposito 3.Esci\n")

                if not scelta.isdigit():
                    print("Input non valido. Inserisci 1, 2 o 3.")
                    continue

                operaz = int(scelta)

                if operaz == 1: 
                    importo = random.randint(1, 1000)
                    if saldo - importo < 0:
                        print(f"Saldo insufficiente ({saldo}), impossibile prelevare {importo}.")
                    else:
                        saldo -= importo
                        print(f"Prelievo di {importo} riuscito. Saldo attuale: {saldo}")

                elif operaz == 2: 
                    importo = random.randint(1, 100)
                    saldo += importo
                    print(f"Deposito di {importo} riuscito. Saldo attuale: {saldo}")

                elif operaz == 3: 
                    print("Uscita dal C/C. Arrivederci")
                    return 

                else:
                    tentativi2 += 1
                    print("Operazione richiesta sconosciuta. Riprova.")
                    if tentativi2 == 3:
                        print("3 tentativi fallisi. Uscita dal C/C")
                        break
            

        else:
            tentativi += 1
            print(f"❌ Pin Errato. Tentativo {tentativi} fallito.")

    print("Il tuo account è stato bloccato.")

def main():
    pin = imposta_pin()
    gestisci_conto(pin)

if __name__ == "__main__":
    main() 
