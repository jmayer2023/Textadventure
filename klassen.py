# Erstellen benötigter Klassen

class Charakter:

    # Inventarliste
    inventarliste = []

    # Startgegenstand für alle Klassen
    inventarliste.append("Schwert")

    # Name und Klassenbezeichnung
    def __init__(self, name, klasse):

        # Zur Übergabe der gemachten Eingabe für den Namen
        self.name = name

        # Zur späteren Ausgabe der gewählten Klasse
        self.klasse = klasse

    # Inventar hinzufügen
    def inventar(self, klasse = None):
        if klasse is None:
            return self.inventarliste
        else:
            self.inventarliste.append(klasse)
        return self.inventarliste
    
    # Vorstellung
    def intro(self):
        raise NotImplementedError("Die Methode muss in der Unterklasse implementiert werden.")

class Krieger(Charakter):
    def __init__(self, name, klasse):
        super().__init__(name, "Krieger")

    def intro(self):
        print(f"{self.name} ist ein mächstiger Krieger (+2 auf deine Würfel)")
        

class Magier(Charakter):
    def __init__(self, name, klasse):
        super().__init__(name, "Magier")

    def intro(self):
        print(f"{self.name} ist ein weiser Magier (+1 auf deine Würfel)")

class Dieb(Charakter):
    def __init__(self, name, klasse):
        super().__init__(name, "Dieb")

    def intro(self):
        print(f"{self.name} ist ein verstohlener Dieb (weitere Auswahlmöglichkeiten)")
