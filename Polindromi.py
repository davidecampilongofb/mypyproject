def pulisci_frase(frase):
    frase = frase.lower()

    frasepulita = ""
    for carattere in frase:
        if carattere.isalnum():
            frasepulita += carattere
    return frasepulita

def controllo_palindromo(testo):
    return testo == testo[::-1]

def main():
    while True:
        frase = input("Scrivi la frase/parola che vuoi far controllare (oppure 'x' per uscire): ")
        if frase.lower() == 'x':
            print("Uscita dal programma. Ciao!")
            break
        
        frasepulita = pulisci_frase(frase)
        
        if frasepulita == "":
            print("Hai inserito solo caratteri non validi. Riprova.")
            continue
        
        if controllo_palindromo(frasepulita):
            print("✅ È un palindromo!")
        else:
            print("❌ Non è un palindromo.")

if __name__ == '__main__':
    main()
