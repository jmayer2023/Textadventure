# TODO Storyline geht nur weiter wenn man entsprechenden Gegenstand im Inventar hat
# TODO Sound ?
# TODO Code verschlanken und Doppelungen als Funktionen auslagern

# Importieren benötigter Bibliotheken
import time

# Importieren eigener Funktionen
from functions import *

# Importieren eigener Klassen
from klassen import *

#START

# Startbild
schloss()

# Erstelle eine Leere Variable
klasse = ""

# Prüfe ob die Variabe nicht k, m oder d ist, dann Frage nach der Klasse
while klasse not in ["k", "m", "d"]:

    # TODO: Schleife über die möglichen Klassen laufen lassen und entsprechend hier ausgeben
    klasse = input("Welcher Zunft gehört Ihr an? Wählen Sie 'k' für Krieger, 'm' für Magier und 'd' für Dieb: ")

    # Prüfe ob die Eingabe korrekt ist
    if klasse not in ["k", "m", "d"]:
        print("Ungültige Eingabe. Bitte wählen Sie 'k', 'm' oder 'd'.")

# Bilde ein Objekt aus der entsprechenden Klasse
if klasse == "k":

    # Frage nach Namen
    name = input("Wie darf ich euch nennen, mein Herr/Meine Herrin?: ")

    # Erstelle ein Objekt aus der Klasse und benenne es entsprechend der Eingabe
    user = Krieger(name, "Krieger") 

    # Überprüfung durch Vorstellung
    user.intro()

    # Füge speziellen Gegenstand dem Inventar hinzu und zeige es an
    print("dein Inventar enthält: ")
    user.inventar("Schild")
    print(user.inventar())
if klasse == "m":
    name = input("Wie darf ich euch nennen, mein Herr/Meine Herrin?: ")
    user = Magier(name, "Magier")
    user.intro()
    print("dein Inventar enthält: ")
    user.inventar("Zauberstab")
    print(user.inventar())
if klasse == "d":
    name = input("Wie darf ich euch nennen, mein Herr/Meine Herrin?: ")
    user = Dieb(name, "Dieb")
    user.intro()
    print("dein Inventar enthält: ")
    user.inventar("Dolch")
    print(user.inventar()) 

# Fortsetzung Storyline
print("An der Tür des Schlosses angekommen stellst du dir folgende Frage:")
time.sleep(2)

# QUEST 1
quest1 = ""
while quest1 not in ["a", "e", "s"]:
    quest1 = input("Soll ich (a)nklopfen, die Tür (e)intreten oder mich um das Schloss (s)chleichen?: ")
    if quest1 not in ["a", "e", "s"]:
        print("Ungültige Eingabe. Bitte wählen Sie 'a', 'e' oder 's'.")
if quest1 == "a":
    print(f"Du klopfst fest an die Tür und schreist: 'Ich bin {name} und verlange Eintritt!'")
    time.sleep(2)
    print("mit einem lauten knarren öffnet sich die Tür.")
    time.sleep(2)
    print("Der Drache steht vor dir.")
    time.sleep(2)
    print(f"leicht verschlafen sagt der Drache: '{name}, bist du es wirklich? Ich kannte deinen Vater und half ihm im Krieg gegen die Trolle.'")

    # Einfügen einer Varibalen zur Bestimmung der Storyline am Ende
    final = "happy"
if quest1 == "e":
    print("du gehst ein paar Schritte zurück und nimmst Anlauf, jedoch hängt dein Erfolg von deinem Würfel ab.")
    time.sleep(2)

    # BATTLE 1 (neue Variable für jeden Kampf nötig, da er sonst in Abfragen springt, die er nicht soll. Gleicher Grund die Abfrage nicht mit ELSE enden zu lassen. vlt Problem durch eineindeutige Variablen bereits gelöst)
    augenzahl1 = dice()
    print(augenzahl1)

    # Verbesserung aufgrund gewählter Klasse
    if user.klasse == "Krieger":
        augenzahl1 += 2
        print("Deine Klasse verbessert den Würfel zu:", augenzahl1)
    if user.klasse == "Magier":
        augenzahl += 1
        print("Deine Klasse verbessert den Würfel zu:", augenzahl1)
    if augenzahl1 >= 6:
        time.sleep(2)
        print("die Tür öffnet sich unbemerkt.")
        time.sleep(2)
        print("vor dir liegt ein schlafender Drache.")
        time.sleep(2)

        # QUEST 2
        quest2 = ""
        while quest2 not in ["s", "z"]:
            quest2 = input("was möchstest du tun? Ich lege mich neben den Drachen und (s)chlafe ebenfalls ein, Ich (z)iehe meine Waffe und erschlage den Drachen: ")
            if quest2 not in ["s", "z"]:
                print("Ungültige Eingabe. Bitte wählen Sie 's' oder 'z'.")    
        if quest2  == "s":
            time.sleep(5)
            print("zZzZzZzZz")
            time.sleep(5)
            print("zZzZzZzZz")
            time.sleep(5)
            print(f"gut erholt wachst du neben dem Drachen auf. Dieser schaut dir bereits in die Augen und sagt:")
            time.sleep(2)
            print(f"'{name}, bist du es? Als du noch ein Kind warst, half ich deinem Vater im Krieg gegen die Trolle.'")
            final = "happy"
        if quest2 == "z":
            time.sleep(2)
            print("du ziehst deine Waffe und schlägst zu, jedoch hängt dein Erfolg von deinem Würfel ab:")

            # BATTLE 2
            augenzahl2 = dice()
            print(augenzahl2)
            if user.klasse == "Krieger":
                augenzahl2 += 2
                print("Deine Klasse verbessert den Würfel zu:", augenzahl2)
            if user.klasse == "Magier":
                augenzahl2 += 1
                print("Deine Klasse verbessert den Würfel zu:", augenzahl2)
            if augenzahl2 > 3:
                time.sleep(2)
                print("Erfolg, der Drache ist tot")

                # Einfügen einer Varibalen zur Bestimmung der Storyline am Ende
                final = "Drache tot"
            if augenzahl2 < 4: 
                time.sleep(2)
                print("du verfehlst den Drachen, der durch das Geräusch der Klinge auf den Boden aufwacht.")
                time.sleep(2)
                print("du bist Tod.")

                # Einfügen einer Varibalen zur Bestimmung der Storyline am Ende
                final = "user tot"             
    if augenzahl1 <= 3:
        time.sleep(2)
        print("du hast es leider nicht geschafft")
        time.sleep(2)
        print("im Inneren des Schloßes hörst du ein Geräusch was schnell lauter wird.")
        time.sleep(2)

        # QUEST 5      
        quest5 = ""
        while quest5 not in ["w", "z"]:
            quest5 = input("was möchstest du tun? (w)egrennen oder (z)iehe deine Waffe: ")
            if quest5 not in ["w", "z"]:
                print("Ungültige Eingabe. Bitte wählen Sie 'w' oder 'z'.")        
        if quest5 == "w":
            time.sleep(2)
            print("du drehst dich um und rennst so schnell du kannst los")
            time.sleep(2)
            print("leider übersiehst du dabei ein Stein, stolperst und landest im Burggraben.")
            time.sleep(2)
            print("im nächsten Moment ist der Drache über dir und verschlingt dich.")
            time.sleep(2)
            final = "user tot"
        if quest5 == "z":
            time.sleep(2)
            print("Der Drache stürmt auf dich zu, du weichst dem ersten Angriff aus und versuchst ein Hieb mit deinem Schwert.")   
            time.sleep(2)
            print("Der Erfolg hängt von deinem Würfel ab.")
            time.sleep(2)

            # BATTLE 5
            augenzahl5 = dice()
            print(augenzahl5)
            if user.klasse == "Krieger":
                augenzahl5 += 2
                print("Deine Klasse verbessert den Würfel zu:", augenzahl5)
            if user.klasse == "Magier":
                augenzahl5 += 1
                print("Deine Klasse verbessert den Würfel zu:", augenzahl5)
            if augenzahl5 > 4:
                time.sleep(2)
                print("Dein Schwert durchbohrt den Drachen.")
                final = "Drache tot"
            if augenzahl5 < 5:
                time.sleep(2)
                print("Du verfehlst den Drachen. Dieser öffnet sein Maul und es entzündet sich eine Flamme. Mit lauten Gebrüll verbrennst du am lebendigen Leib.")
                final = "user tot"
    if augenzahl1 > 3 and augenzahl1 < 6:
        time.sleep(2)
        print("mit einem lauten Knall öffnet sich die Tür")
        time.sleep(2)
        print("Ein Drache türmt sich vor dir auf.")
        time.sleep(2)

        # QUEST 3
        quest3 = ""
        while quest3 not in ["w", "v", "z"]:
            quest3 = input("was möchstest du tun? (w)egrennen, auf die Knie gehen und dich (v)erbeugen oder (z)iehe deine Waffe: ")
            if quest3 not in ["w", "v", "z"]:
                print("Ungültige Eingabe. Bitte wählen Sie 'w', 'v' oder 'z'.")        
        if quest3 == "w":
            time.sleep(2)
            print("du drehst dich um, doch im gleich Moment stürzt sich der Drache auf dich und verschlingt dich in einem Stück.")
        if quest3 == "v":
            time.sleep(2)
            print("Voller Erfurcht kauerst du auf deinen Knien.")
            time.sleep(4)
            print("Mit tiefer Stimme fragt dich der Drach nach deinem Namen.")
            time.sleep(2)
            print(f"nach kurzem überlegen antwortest du: 'Meine Name ist {name}, bitte verschone mich.'")
            time.sleep(2)
            print(f"Der Drache antwortet: '{name}, bist du es? Als du noch ein Kind warst, half ich deinem Vater im Krieg gegen die Trolle.'")
            final = "happy"
        if quest3 == "z":
            time.sleep(2)
            print("Du ziehst dein Schwert und holst aus, jedoch hängt dein Erfolg von deinem würfel ab.")
            time.sleep(2)

            # BATTLE 3
            augenzahl3 = dice()
            print(augenzahl3)
            if user.klasse == "Krieger":
                augenzahl3 += 2
                print("Deine Klasse verbessert den Würfel zu:", augenzahl3)
            if user.klasse == "Magier":
                augenzahl3 += 1
                print("Deine Klasse verbessert den Würfel zu:", augenzahl3)
            if augenzahl3 >= 6:
                print("Mit einem Schlag enthauptest du den Drachen.")
            if augenzahl3 <= 2:
                print("dein Schlag verfehlt den Drachen, trifft eine Säule und geht dir direkt ins Bein.")
                time.sleep(2)
                print("du verblutest an deiner Verletzung.")
                final = "user tot"
            if augenzahl3 < 6 and augenzahl3 >2:
                print("Du triffst den Drachen am Körper und fügst ihm großen Schmerz zu.")
                time.sleep(2)
                print("am Boden liegend keucht der Drache vor sich hin.")
                time.sleep(2)
                print(f"mit seinem letzten Atemzug wispert er: 'Ich wünschte ich hätte noch einmal den Sohn des Königs gesehen, sein name war {name}.")
                time.sleep(2)
                print("Gern hätte ich ihm die Geschichten aus dem Krieg gegen die Trolle erzählt.")
                final = "Drache tot"
if quest1 == "s":
    time.sleep(2)
    print("du findest ein Hintereingang.")
    time.sleep(2)
    print("du schleichst dich hinein.")
    time.sleep(2)
    print("vor dir liegt ein schlafender Drache.")
    time.sleep(2)

    # QUEST 4
    quest4 = ""
    while quest4 not in ["s", "z"]:
        quest4 = input("was möchstest du tun? Ich lege mich neben den Drachen und (s)chlafe ebenfalls ein, Ich (z)iehe meine Waffe und erschlage den Drachen: ")
        if quest4 not in ["s", "z"]:
            print("Ungültige Eingabe. Bitte wählen Sie 's' oder 'z'.")    
    if quest4  == "s":
        time.sleep(5)
        print("zZzZzZzZz")
        time.sleep(5)
        print("zZzZzZzZz")
        time.sleep(5)
        print(f"gut erholt wachst du neben dem Drachen auf. Dieser schaut dir bereits in die Augen und sagt:")
        time.sleep(2)
        print(f"'{name}, bist du es? Als du noch ein Kind warst, half ich deinem Vater im Krieg gegen die Trolle.'")
        final = "happy"
    if quest4 == "z":
        time.sleep(2)
        print("du ziehst deine Waffe und schlägst zu, jedoch hängt dein Erfolg von deinem Würfel ab:")
        time.sleep(2)

        # BATTLE 4
        augenzahl4 = dice()
        print(augenzahl4)
        if user.klasse == "Krieger":
            augenzahl4 += 2
            print("Deine Klasse verbessert den Würfel zu:", augenzahl4)
        if user.klasse == "Magier":
            augenzahl4 += 1
            print("Deine Klasse verbessert den Würfel zu:", augenzahl4)
        if augenzahl4 > 3:
            time.sleep(2)
            print("Erfolg, der Drache ist tot")
            final = "Drache tot"
        if augenzahl4 < 4:
            time.sleep(2)
            print("du verfehlst den Drachen, der durch das Geräusch der Klinge auf dem Boden aufwacht.")
            time.sleep(2)
            print("voller Zorn stürzt sich der Drache auf dich.")
            time.sleep(2)
            print("du bist Tod.")
            final = "user tot"

# ENDE

# Aufrufen der Storyline entsprechend der Variablen "final"
ende(final, name)

# Gimmick
dragon()
time.sleep(2)

# Goodbye
print(f"{name}, ich hoffe dir gefiel das Spiel als {user.klasse}, probier doch mal eine andere Klasse aus.")
time.sleep(2)
print("bis zum nächsten Mal.")


