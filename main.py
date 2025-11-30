from cmu_graphics import *
import random
import time
#databas
app.background = fill="gray"
fraglista = ["Vilket år tillverkades sista v70 modellen",
            "Vilket land kommer Volvo ifrån?",
            "Vilken typ av bil är en Volvo XC90?",
            "Vilken Volvo-modell är en elbil: EX40 eller V70?",
            ]
# Fyra olika alternativ per fråga (ett korrekt, tre fel)
alternativ1 = ["2016", "Sverige", "SUV", "EX40"]
alternativ2 = ["2015", "Tyskland", "Sedan", "V70"]
alternativ3 = ["2017", "USA", "Kombi", "XC60"]
alternativ4 = ["2018", "Japan", "Sportbil", "XC40"]


fraglista2 = [
   "Vilken typ av motor har de flesta nya Volvobilar?",
   "Vilken typ av motor finns i Volvo XC90 T8?",
   "Hur många cylindrar har en vanlig Volvo-motor?",
   "Hur många cylindrar har en volvo 850",
   "Vilken typ av bränsle använder Volvo D3?"
]
alternativ12 = ["hybrid", "hybrid", "4", "5", "diesel"]
alternativ22 = ["bensin", "diesel", "3", "4", "bensin"]
alternativ32 = ["diesel", "el", "5", "6", "etanol"]
alternativ42 = ["el", "bensin-el", "6", "8", "gas"]


clicked = False
aktuellfraga = ""
aktuellsvar = ""
svarfraga = ""
poang = 0
katergori = ""

darkOrange = Rect(10,300,130,80,fill="darkOrange",visible=False)
orange = Rect(260,300,130,80,fill="orange",visible=False)
blue = Rect(10,200,130,80,fill="blue")
red = Rect(260,200,130,80,fill="red")
Fraga = Label("",200,100,size=15)
Kategori = Label("Välj kategori",200,100,size=20)
volvoLabel = Label("Volvo", 70,240,size=20,fill="white")
motorLabel = Label("Volvomotorer", 330,240,size=20,fill="white")
#svarslabels
svar1 = Label("",0,0,size=20,fill="white")
svar2 = Label("",0,0,size=20,fill="white")
svar3 = Label("",0,0,size=20,fill="white")
svar4 = Label("",0,0,size=20,fill="white")
#svartimer
timer = Rect(150,50,100,10,fill="gray")
#spawnafrågor

def spawn():
    global poang, aktuellsvar
    if len(fraglista) > 0:
        index = random.randint(0, len(fraglista2) - 1)
        aktuellfraga = fraglista.pop(index)
        aktuellsvar = alternativ1.pop(index)
        svar1.value = aktuellsvar
        svar2.value = alternativ2.pop(index)
        svar3.value = alternativ3.pop(index)
        svar4.value = alternativ4.pop(index)
        Fraga.value = aktuellfraga

        # random position på svaren
        positions = [(70, 240), (330, 240), (70, 340), (330, 340)]
        random.shuffle(positions)

        svar1.centerX, svar1.centerY = positions[0]
        svar2.centerX, svar2.centerY = positions[1]
        svar3.centerX, svar3.centerY = positions[2]
        svar4.centerX, svar4.centerY = positions[3]
    else:
        Fraga.value = "Dina poäng = " + str(poang)
#katergori motorfrågor
def spawn2():
    global poang, aktuellsvar
    if len(fraglista2) > 0:
        index = random.randint(0, len(fraglista2) - 1)
        aktuellfraga = fraglista2.pop(index)
        aktuellsvar = alternativ12.pop(index)
        svar1.value = aktuellsvar
        svar2.value = alternativ22.pop(index)
        svar3.value = alternativ32.pop(index)
        svar4.value = alternativ42.pop(index)
        Fraga.value = aktuellfraga

        # random position på svaren
        positions = [(70, 240), (330, 240), (70, 340), (330, 340)]
        random.shuffle(positions)

        svar1.centerX, svar1.centerY = positions[0]
        svar2.centerX, svar2.centerY = positions[1]
        svar3.centerX, svar3.centerY = positions[2]
        svar4.centerX, svar4.centerY = positions[3]
    else:
        Fraga.value = "Dina poäng = " + str(poang)


#svarafrågor

def onMousePress(mouseX, mouseY):
    global kategori, clicked, aktuellfraga, aktuellsvar, poang

    if clicked != True:
        # Blå ruta (kategori = -1)
        if 10 < mouseX < 140 and 200 < mouseY < 280:
            clicked = True
            katergori = "V"
            Kategori.visible = False
            volvoLabel.visible = False
            motorLabel.visible = False
            darkOrange.visible = True
            orange.visible = True
            spawn()

        # Röda ruta (kategori = 1)
        elif 260 < mouseX < 390 and 200 < mouseY < 280:
            clicked = True
            katergori = "M"
            Kategori.visible = False
            volvoLabel.visible = False
            motorLabel.visible = False
            darkOrange.visible = True
            orange.visible = True
            spawn2()


    elif Fraga.value not in ("Rätt","Fel"):
        # blå
        if 10 < mouseX < 140 and 200 < mouseY < 280:
            if svar1.centerX == 70 and svar1.centerY == 240:
                Fraga.value = "Rätt"
                poang += 1
            else:
                Fraga.value = "Fel" + ", rätt svar: " + aktuellsvar
                pass
        # röd
        elif 260 < mouseX < 390 and 200 < mouseY < 280:
            if svar1.centerX == 330 and svar1.centerY == 240:
                Fraga.value = "Rätt"
                poang += 1
            else:
                Fraga.value = "Fel" + ", rätt svar: " + aktuellsvar
                pass
        # gul
        elif 10 < mouseX < 140 and 300 < mouseY < 380:
            if svar1.centerX == 70 and svar1.centerY == 340:
                Fraga.value = "Rätt"
                poang += 1
            else:
                Fraga.value = "Fel" + ", rätt svar: " + aktuellsvar
            pass
        # orange
        elif 260 < mouseX < 390 and 300 < mouseY < 380:
            if svar1.centerX == 330 and svar1.centerY == 340:
                Fraga.value = "Rätt"
                poang += 1
            else:
                Fraga.value = "Fel" + ", rätt svar: " + aktuellsvar

            pass

def onStep():
    if Fraga.value in ("Rätt","Fel" + ", rätt svar: " + aktuellsvar):
        timer.fill = "blue"
        if timer.width > 2:
            timer.visible = True
            timer.width -= 2
        if timer.width == 2:
            timer.visible = False
            timer.width = 100
            if katergori == "V":
                spawn()
            else:
                spawn2()
    pass


cmu_graphics.run()

