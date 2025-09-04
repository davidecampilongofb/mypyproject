import urllib.request
import json

def risultati(conversionedati):
    # i character stanno dentro i result giusto
    for character in conversionedati["results"]:
        
        print(f"Nome: {character['name']}")
        print(f"Specie: {character['species']}")
        print(f"Stato: {character['status']}")
        print("---------------")

# Funzione principale per fare la richiesta e ottenere i dati
def main():
    url = "https://rickandmortyapi.com/api/character/"  # URL corretto per ottenere i personaggi
    
    try:
        # Apri l'URL e fai la richiesta
        aperturaurl = urllib.request.urlopen(url)
        checkconnessione = aperturaurl.getcode()

        if checkconnessione == 200:
            print("Connessione col server avvenuta")

            letturaurl = aperturaurl.read()
            conversionedati = json.loads(letturaurl)

            # Passa i dati alla funzione 'risultati' per la visualizzazione
            risultati(conversionedati)

        else:
            print(f"Errore di connessione. Codice di stato: {checkconnessione}")

    except Exception as e:
        print(f"Si è verificato un errore: {e}")

# Esegui la funzione principale
if __name__ == "__main__":
    main()
