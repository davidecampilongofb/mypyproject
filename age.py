from datetime import datetime

data_min_nascita = datetime.strptime("21-07-1960", "%d-%m-%Y")
data_max_nascita = datetime.strptime("21-07-2023", "%d-%m-%Y")

while True:
    data_attuale = datetime.now()
    data_input = input("Quando sei nato? Inserisci nel formato DD-MM-YYYY\n")
    ora_input = input("A che ora? Inserisci nel formato HH-MM-SS\n")
    
    try:
        data_completa_input = f"{data_input} {ora_input}"
        data_nascita = datetime.strptime(data_completa_input, "%d-%m-%Y %H-%M-%S")
        
        if data_min_nascita <= data_nascita <= data_max_nascita:
            differenza = data_attuale - data_nascita

            giorni = differenza.days
            secondi_totali = differenza.seconds
            ore = secondi_totali // 3600
            minuti = (secondi_totali % 3600) // 60
            secondi = secondi_totali % 60

            print(f"✅ Grazie! Stai vivendo da {giorni} giorni, {ore} ore, {minuti} minuti, {secondi} secondi.\n")

            proseguo = input("Simuliamo quanto ti resta? Inserisci data (DD-MM-YY) o X per uscire: ").upper()

            if proseguo == "X":
                break
            else:
                try:
                    data_morte = datetime.strptime(proseguo, "%d-%m-%y")
                    tempo_restante = data_morte - data_attuale

                    if tempo_restante.total_seconds() > 0:
                        giorni_rimanenti = tempo_restante.days
                        print(f"🪦 Ti restano circa {giorni_rimanenti} giorni di vita... 🍃")
                    else:
                        print("😵‍💫 Sei già oltre la data inserita...")

                    break  # Fine del ciclo dopo la simulazione

                except ValueError:
                    print("⚠️ Data non valida. Riprova con il formato DD-MM-YY o scrivi X per uscire.")
                    break  # Esce comunque dopo errore, puoi togliere se vuoi ripetere
        else:
            print("⚠️ Devi avere almeno 10 anni e massimo 50 anni per giocare. Riprova.\n")

    except ValueError:
        print("⚠️ Formato non valido. Riprova usando il formato DD-MM-YYYY per la data e HH-MM-SS per l'orario.\n")
