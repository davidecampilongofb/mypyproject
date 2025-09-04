import time
import random

def main():
    piani = list(range(1, 8))
    piano_attuale = random.randint(1, 7)

    while True:
        
        try:
            print(f"\n🚪 L'ascensore si trova al piano {piano_attuale}")
            pianoscelto = int(input("Digita il piano a cui vuoi andare (1-7):\n"))

            if pianoscelto not in piani:
                print("❌ Piano non valido! Deve essere tra 1 e 7.")
                continue

            print(f"Ascensore in movimento dal piano {piano_attuale} al piano {pianoscelto}...")

            if pianoscelto > piano_attuale:
                for piano in range(piano_attuale + 1, pianoscelto + 1):
                    time.sleep(1)
                    print(f"⬆️ Salendo... Piano {piano}")
                    
            elif pianoscelto < piano_attuale:
                for piano in range(piano_attuale - 1, pianoscelto - 1, -1):
                    time.sleep(1)
                    print(f"⬇️ Scendendo... Piano {piano}")
            else:
                print("⏹ Sei già al piano richiesto.")

            print("✅ Arrivato al piano!")

            piano_attuale = pianoscelto


            risposta = input("Vuoi prendere di nuovo l'ascensore? (s/n): ").lower()
            if risposta == 'n':
                print("👋 Ciao! Grazie per aver usato l'ascensore.")
                break 
            elif risposta != 's':
                print("❓ Risposta non riconosciuta. Uscita dal programma.")
                break


        except ValueError:
            print("❌ Inserisci un numero valido (es. 1, 2, 3...)")

if __name__ == '__main__':
    main()
