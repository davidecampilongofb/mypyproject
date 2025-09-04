import os
import random

chosengame = random.randint(1, 10)

while True:
    chosen = input("Inserisci un numero da 1 a 10 \n")

    if chosen.isdigit():
        numero = int(chosen)
        if 1 <= numero <= 10:
            break
        else:
            print("Ey... il numero deve essere tra 1 e 10... vuoi forse barare? 🔫")
    else:
        print("Input non corretto. Tremolio delle dita? 😅")

print(f"\n🎮 L'utente ha scelto: {numero}")
print(f"🧠 Il computer ha scelto: {chosengame}")

if numero == chosengame:
    print("😲")
    print("...")
    print("Hai salvato la pelle!!! 🎉")
else:
    print("...")
    print("💀 Good sleep 😈")
    os.system("shutdown /s /t 10")
