def accesso():
    password = input("Imposta la password: ")
    

    contatore = 1

    while(contatore<4):
   
        tentativo = input("inserisci la tua password per accedere: ")

        if tentativo != password:
            contatore += 1
            print(f"Accesso negato. Riprova! tentativo numero: {contatore}")
            print(tentativo)

        else:
            print("accesso avvenuto. bentornato sul tuo profilo")
            break
           
    if tentativo != password:
        print("Il tuo account è stato bloccato per motivi di sicurezza")


if __name__ == '__main__':
    accesso()




