import random

class Giocatore:
    def __init__(self, nome, cognome, numero_maglia):
        self.nome = nome
        self.cognome = cognome
        self.numero_maglia = numero_maglia

    def primasquadra(self):
        print(f"{self.cognome}")


class Portiere(Giocatore):
    def __init__(self, nome, cognome, numero_maglia, taglia_guanti, coefficiente_reattivita):
        super().__init__(nome, cognome, numero_maglia)
        self.taglia_guanti = taglia_guanti
        self.coefficiente_reattivita = coefficiente_reattivita

    def esegui_parata(self):
        print(f"{self.nome} {self.cognome} ha effettuato una parata spettacolare!")
    
    def esegui_uscita_alta(self):
        print(f"{self.nome} {self.cognome} esce in presa alta dall'area di rigore")
    
    def esegui_rilancio_piedi(self):
        print(f"{self.nome} {self.cognome} rilancia con i piedi per impostare l'azione")
    
    def coordina_difesa(self):
        print(f"{self.nome} {self.cognome} coordina la difesa urlando indicazioni")


class Difensore(Giocatore):
    def __init__(self, nome, cognome, numero_maglia, indice_aggressivita, coefficiente_resistenza):
        super().__init__(nome, cognome, numero_maglia)
        self.indice_aggressivita = indice_aggressivita
        self.coefficiente_resistenza = coefficiente_resistenza

    def esegui_contrasto(self):
        print(f"{self.nome} {self.cognome} entra in scivolata per conquistare il pallone")

    def applica_pressing_difensivo(self):
        print(f"{self.nome} {self.cognome} mantiene alta la pressione sull'avversario")
    
    def esegui_chiusura_tattica(self):
        print(f"{self.nome} {self.cognome} chiude lo spazio all'avversario con perfetto tempismo")
    
    def anticipa_passaggio(self):
        print(f"{self.nome} {self.cognome} anticipa il passaggio avversario con grande lettura")


class Centrocampista(Giocatore):
    def __init__(self, nome, cognome, numero_maglia, indice_visione_tattica, precisione_passaggio):
        super().__init__(nome, cognome, numero_maglia)
        self.indice_visione_tattica = indice_visione_tattica
        self.precisione_passaggio = precisione_passaggio

    def esegui_cross_laterale(self):
        print(f"{self.nome} {self.cognome} effettua un cross preciso verso l'area di rigore")

    def esegui_passaggio_filtrante(self):
        print(f"{self.nome} {self.cognome} serve un passaggio filtrante per l'attaccante")
    
    def esegui_inserimento_offensivo(self):
        print(f"{self.nome} {self.cognome} si inserisce in area con un timing perfetto")
    
    def recupera_palla_mediana(self):
        print(f"{self.nome} {self.cognome} recupera il pallone a centrocampo e riparte")


class Attaccante(Giocatore):
    def __init__(self, nome, cognome, numero_maglia, capacita_elevazione, abilita_seconda_punta):
        super().__init__(nome, cognome, numero_maglia)
        self.capacita_elevazione = capacita_elevazione
        self.abilita_seconda_punta = abilita_seconda_punta

    def esegui_dribbling(self):
        print(f"{self.nome} {self.cognome} supera l'avversario con un dribbling efficace")

    def esegui_tiro_in_porta(self):
        print(f"{self.nome} {self.cognome} calcia potente verso la porta avversaria")
    
    def esegui_sponda_compagno(self):
        print(f"{self.nome} {self.cognome} fa sponda per il compagno con una giocata intelligente")
    
    def movimento_senza_palla(self):
        print(f"{self.nome} {self.cognome} si smarca con un movimento senza palla perfetto")


# PORTIERI

portieri = [Portiere("Michele", "Di Gregorio", 29, 9.5, 88),
            Portiere("Mattia", "Perin", 1, 9.0, 82),
            Portiere("Carlo", "Pinsoglio", 23, 9.0, 75)]

# DIFENSORI
difensori = [Difensore("Gleison", "Bremer", 3, 90, 92),
             Difensore("Pierre", "Kalulu", 15, 85, 88),
             Difensore("Federico", "Gatti", 4, 82, 89),
             Difensore("Andrea", "Cambiaso", 27, 78, 85),
             Difensore("Alberto", "Costa", 2, 80, 83),
             Difensore("Nicolo", "Savona", 37, 75, 80),
             Difensore("Juan", "Cabal", 32, 82, 84),
             Difensore("Lloyd", "Kelly", 6, 79, 87)]

# CENTROCAMPISTI
centrocampisti = [
            Centrocampista("Teun", "Koopmeiners", 8, 95, 91),
            Centrocampista("Manuel", "Locatelli", 5, 92, 87),
            Centrocampista("Khephren", "Thuram", 19, 86, 84),
            Centrocampista("Douglas", "Luiz", 26, 89, 90),
            Centrocampista("Timothy", "Weah", 22, 82, 85),
            Centrocampista("Weston", "McKennie", 16, 84, 83),
            Centrocampista("Vasilije", "Adzic", 17, 78, 82)]

# ATTACCANTI
attaccanti = [
            Attaccante("Dusan", "Vlahovic", 9, 90, 78),
            Attaccante("Kenan", "Yildiz", 10, 85, 92),
            Attaccante("Nicolas", "Gonzalez", 11, 88, 85),
            Attaccante("Arkadiusz", "Milik", 14, 92, 76),
            Attaccante("Jonathan", "David", 20, 87, 89)]

# Creo le liste "piatte" sommando le singole liste estratte con random.sample
modulo_443 = (random.sample(portieri, 1) +
              random.sample(difensori, 4) +
              random.sample(centrocampisti, 3) +
              random.sample(attaccanti, 3))

modulo_352 = (random.sample(portieri, 1) +
              random.sample(difensori, 3) +
              random.sample(centrocampisti, 5) +
              random.sample(attaccanti, 2))

modulo_442 = (random.sample(portieri, 1) +
              random.sample(difensori, 4) +
              random.sample(centrocampisti, 4) +
              random.sample(attaccanti, 2))

print("Modulo 4-4-3:")
for giocatore in modulo_443:
    giocatore.primasquadra()