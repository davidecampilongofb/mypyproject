import random

quiz = [
    {"domanda 1": "Chi scoprì l’America?",
     "opzioni": ["Cristoforo Colombo", "Vasco da Gama", "Magellano", "Marco Polo"],
     "indice": 0},
    {"domanda 2": "In che anno cadde il Muro di Berlino?",
     "opzioni": ["1987", "1989", "1991", "1993"],
     "indice": 1},
    {"domanda 3": "Chi vinse il Mondiale di calcio 2018?",
     "opzioni": ["Brasile", "Argentina", "Francia", "Germania"],
     "indice": 2},
    {"domanda 4": "Chi scrisse 'La Divina Commedia'?",
     "opzioni": ["Dante Alighieri", "Petrarca", "Boccaccio", "Manzoni"],
     "indice": 0},
    {"domanda 5": "Qual è la capitale del Giappone?",
     "opzioni": ["Pechino", "Tokyo", "Kyoto", "Osaka"],
     "indice": 1},
    {"domanda 6": "Chi è l'attuale presidente degli Stati Uniti (2025)?",
     "opzioni": ["Donald Trump", "Joe Biden", "Barack Obama", "Kamala Harris"],
     "indice": 1},
    {"domanda 7": "In che anno iniziò la Seconda Guerra Mondiale?",
     "opzioni": ["1937", "1939", "1941", "1945"],
     "indice": 1},
    {"domanda 8": "Chi ha vinto il Premio Nobel per la Pace nel 2009?",
     "opzioni": ["Papa Francesco", "Barack Obama", "Nelson Mandela", "Greta Thunberg"],
     "indice": 1},
    {"domanda 9": "Qual è la capitale dell'Australia?",
     "opzioni": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
     "indice": 2},
    {"domanda 10": "Chi è il fondatore di Microsoft?",
     "opzioni": ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Elon Musk"],
     "indice": 1},
    {"domanda 11": "Quale squadra ha vinto più Champions League?",
     "opzioni": ["Barcellona", "Real Madrid", "Milan", "Liverpool"],
     "indice": 1},
    {"domanda 12": "Chi dipinse la Gioconda?",
     "opzioni": ["Michelangelo", "Raffaello", "Leonardo da Vinci", "Caravaggio"],
     "indice": 2},
    {"domanda 13": "In quale anno è stato lanciato il primo iPhone?",
     "opzioni": ["2005", "2007", "2009", "2011"],
     "indice": 1},
    {"domanda 14": "Qual è il pianeta più vicino al Sole?",
     "opzioni": ["Mercurio", "Venere", "Terra", "Marte"],
     "indice": 0},
    {"domanda 15": "Chi scrisse '1984'?",
     "opzioni": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Ernest Hemingway"],
     "indice": 0},
    {"domanda 16": "Quale città ha ospitato le Olimpiadi del 2016?",
     "opzioni": ["Tokyo", "Londra", "Pechino", "Rio de Janeiro"],
     "indice": 3},
    {"domanda 17": "Chi fu il primo uomo a camminare sulla Luna?",
     "opzioni": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Michael Collins"],
     "indice": 1},
    {"domanda 18": "Qual è la moneta ufficiale del Regno Unito?",
     "opzioni": ["Euro", "Sterlina", "Dollaro", "Franco"],
     "indice": 1},
    {"domanda 19": "Chi è l'autore di 'Il Signore degli Anelli'?",
     "opzioni": ["C.S. Lewis", "J.R.R. Tolkien", "George R.R. Martin", "Philip Pullman"],
     "indice": 1},
    {"domanda 20": "In quale sport eccelle Usain Bolt?",
     "opzioni": ["Nuoto", "Corsa", "Salto in lungo", "Ciclismo"],
     "indice": 1},
    {"domanda 21": "Chi ha scritto 'La Divina Commedia'?",
     "opzioni": ["Dante Alighieri", "Petrarca", "Boccaccio", "Leopardi"],
     "indicegiusto": 0},
    {"domanda 22": "Qual è la capitale del Giappone?",
     "opzioni": ["Seoul", "Tokyo", "Pechino", "Bangkok"],
     "indicegiusto": 1},
    {"domanda 23": "In quale anno è caduto il Muro di Berlino?",
     "opzioni": ["1992", "1987", "1989", "1990"],
     "indicegiusto": 2},
    {"domanda 24": "Chi ha dipinto 'La Gioconda'?",
     "opzioni": ["Caravaggio", "Michelangelo", "Leonardo da Vinci", "Raffaello"],
     "indicegiusto": 2},
    {"domanda 25": "Qual è il simbolo chimico dell'oro?",
     "opzioni": ["Pb", "Ag", "Fe", "Au"],
     "indicegiusto": 3},
    {"domanda 26": "Quando è iniziata la Seconda Guerra Mondiale?",
     "opzioni": ["1942", "1945", "1939", "1937"],
     "indicegiusto": 2},
    {"domanda 27": "Chi ha scritto il romanzo '1984'?",
     "opzioni": ["Ray Bradbury", "Aldous Huxley", "George Orwell", "Philip K. Dick"],
     "indicegiusto": 2},
    {"domanda 28": "Qual è il fiume più lungo del mondo?",
     "opzioni": ["Yangtze", "Mississippi", "Nilo", "Amazon"],
     "indicegiusto": 3},
    {"domanda 29": "Chi ha scoperto la penicillina?",
     "opzioni": ["Louis Pasteur", "Gregor Mendel", "Marie Curie", "Alexander Fleming"],
     "indicegiusto": 3},
    {"domanda 30": "In quale città si trova il Colosseo?",
     "opzioni": ["Firenze", "Napoli", "Venezia", "Roma"],
     "indicegiusto": 3},
    {"domanda 31": "Quale sport è noto come 'il re degli sport'?",
     "opzioni": ["Tennis", "Rugby", "Calcio", "Basket"],
     "indicegiusto": 2},
    {"domanda 32": "Chi è stato il primo uomo sulla Luna?",
     "opzioni": ["Buzz Aldrin", "Neil Armstrong", "Michael Collins", "Yuri Gagarin"],
     "indicegiusto": 1},
    {"domanda 33": "Qual è la lingua ufficiale in Brasile?",
     "opzioni": ["Spagnolo", "Inglese", "Francese", "Portoghese"],
     "indicegiusto": 3},
    {"domanda 34": "Chi ha scritto 'Il Piccolo Principe'?",
     "opzioni": ["Victor Hugo", "Jules Verne", "Antoine de Saint-Exupéry", "Émile Zola"],
     "indicegiusto": 2},
    {"domanda 35": "Quale paese ha ospitato le Olimpiadi del 2016?",
     "opzioni": ["Brasile", "Russia", "Cina", "Regno Unito"],
     "indicegiusto": 0},
    {"domanda 36": "Qual è la formula chimica dell'acqua?",
     "opzioni": ["O2", "CO2", "H2O", "H2"],
     "indicegiusto": 2},
    {"domanda 37": "Secondo la leggenda, quando fu fondata Roma?",
     "opzioni": ["700 a.C.", "753 a.C.", "800 a.C.", "650 a.C."],
     "indicegiusto": 1},
    {"domanda 38": "Chi ha composto la Nona Sinfonia?",
     "opzioni": ["Bach", "Mozart", "Beethoven", "Chopin"],
     "indicegiusto": 2},
    {"domanda 39": "Qual è la capitale della Svezia?",
     "opzioni": ["Oslo", "Helsinki", "Stoccolma", "Copenaghen"],
     "indicegiusto": 2},
    {"domanda 40": "Qual è il simbolo chimico del ferro?",
     "opzioni": ["Fe", "Au", "Ag", "Pb"],
     "indicegiusto": 0}
]

def normalize_quiz(raw_quiz):
    """Trasforma ogni elemento in dict con chiavi standard: 'domanda','opzioni','indice'."""
    normalized = []
    for item in raw_quiz:
        # trova la chiave che contiene il testo della domanda
        domanda_text = None
        for k, v in item.items():
            if k.startswith("domanda"):
                domanda_text = v
                break
        # trova l'indice corretto (può essere 'indice' o 'indicegiusto')
        indice = item.get("indice")
        if indice is None:
            indice = item.get("indicegiusto")
        # opzioni
        opzioni = item.get("opzioni", [])
        if domanda_text is None or indice is None:
            # salta elementi malformati
            continue
        normalized.append({"domanda": domanda_text, "opzioni": opzioni, "indice": indice})
    return normalized

def main():
    raw = quiz
    quiz_norm = normalize_quiz(raw)

    nome = input("Ciao! scrivi il tuo nome per cominciare il quiz:\n")
    print(f"\nBenvenuto/a {nome}! Per avanzare, devi indovinare ogni domanda. In bocca al lupo!\n")

    # prendi 10 domande casuali (se ce ne sono meno, prendi tutte)
    n = min(10, len(quiz_norm))
    domande_estratte = random.sample(quiz_norm, n)

    punti = 0
    for i, domanda in enumerate(domande_estratte, 1):
        print(f"Domanda {i}: {domanda['domanda']}")
        for idx, opzione in enumerate(domanda['opzioni'], 1):
            print(f"  {idx}. {opzione}")

        risposta = input("Scrivi il numero della risposta corretta: ").strip()
        if not risposta.isdigit():
            print("Input non valido: devi inserire il numero dell'opzione. Gioco terminato.")
            break

        scelta = int(risposta) - 1  # converti a 0-based
        if scelta == domanda['indice']:
            punti += 1
            print("Risposta corretta! ✅\n")
            # continua alla domanda successiva
        else:
            print(f"Sbagliato! La risposta giusta era: {domanda['opzioni'][domanda['indice']]}")
            print(f"Hai totalizzato {punti} punti. Gioco terminato.")
            break
    else:
        # eseguito se il ciclo non è stato interrotto (tutte risposte corrette)
        print(f"Complimenti! Hai risposto correttamente a tutte le {n} domande! Punti: {punti}")

if __name__ == "__main__":
    main()
