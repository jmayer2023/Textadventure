# Erstellen benötigter Funktionen

# Würfel 
import random

def dice():
    global augenzahl
    augenzahl = random.randint(1,6)
    return augenzahl

# Ende der Storyline
import time

def ende(final, name):
    if final == "happy":
        time.sleep(5)
        print('''
        Gemeinsam mit deinem Vater zog ich in die Schlacht gegen die Trolle.
        Ich spie Feuer und vernichtete ganze Trollarmeen, während die Ritter mutig an meiner Seite kämpften.
        Die Trolle waren machtlos gegen unsere vereinten Kräfte.
        Nach vielen blutigen Schlachten und tapferen Taten gelang es uns, die Trolle zu besiegen und das Königreich zu retten.
        Dein Vater dankte mir von ganzem Herzen und bot mir an, in seinem Königreich zu bleiben und als Beschützer des Volkes zu dienen.
            ''')
        time.sleep(5)
    if final == "Drache tot":
        time.sleep(5)
        print("Siegesbewusst kehrst du zurück ins Königreich und prahlst mit deinen Heldentaten.")
        time.sleep(2)
        print("Verwunderst stellst du fest, dass niemand deine Meinung teilt. Hast du vielleicht etwas nicht beachtet?")
        time.sleep(5)
    if final == "user tot":
        time.sleep(5)
        print(f"{name} ist verstorben, niemand wird sich seiner/ihrer erinnern.")
        time.sleep(5)

# ASCI Art
def schloss():
    print('''
                /\                                                        /\\
               |  |                                                      |  |
              /----\                  Willkommen im Haus                /----\\
             [______]                    des Drachen                   [______]
              |    |         _____                        _____         |    |
              |[]  |        [     ]                      [     ]        |  []|
              |    |       [_______][ ][ ][ ][][ ][ ][ ][_______]       |    |
              |    [ ][ ][ ]|     |  ,----------------,  |     |[ ][ ][ ]    |
              |             |     |/'    ____..____    '\|     |             |
               \  []        |     |    /'    ||    '\    |     |        []  /
                |      []   |     |   |o     ||     o|   |     |  []       |
                |           |  _  |   |     _||_     |   |  _  |           |
                |   []      | (_) |   |    (_||_)    |   | (_) |       []  |
                |           |     |   |     (||)     |   |     |           |
                |           |     |   |      ||      |   |     |           |
              /''           |     |   |o     ||     o|   |     |           ''\\
             [_____________[_______]--'------''------'--[_______]_____________]
        ''')
    
def dragon():
    print('''
               \||/
               |  @___oo
     /\  /\   / (__,,,,|
     ) /^\) ^\/ _)
     )   /^\/   _)
     )   _ /  / _)
 /\  )/\/ ||  | )_)
<  >      |(,,) )__)
 ||      /    \)___)\\
 | \____(      )___) )___
  \______(_______;;; __;;;
        ''')