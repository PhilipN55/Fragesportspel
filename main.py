from cmu_graphics import *
import random
import time
#databas
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
svarlista2 = ["hybrid","hybrid","4","5","diesel"]


clicked = False
aktuellfraga = ""
aktuellsvar = ""
svarfraga = ""


yellow = Rect(10,300,130,80,fill="yellow",visible=False)
orange = Rect(260,300,130,80,fill="orange",visible=False)
blue = Rect(10,200,130,80,fill="blue")
red = Rect(260,200,130,80,fill="red")
Fraga = Label("",200,100,size=20)
Kategori = Label("Välj kategori",200,100,size=30)
volvoLabel = Label("Volvo", 70,240)
motorLabel = Label("Volvomotorer", 330,240)
#svarslabels
svar1 = Label("",0,0)
svar2 = Label("",0,0)
svar3 = Label("",0,0)
svar4 = Label("",0,0)
#svartimer
timer = Rect(150,50,100,10,fill="white")
#spawnafrågor

def spawn():
    index = random.randint(0, len(fraglista) - 1)
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

#svarafrågor

def onMousePress(mouseX, mouseY):
    global kategori, clicked, aktuellfraga, aktuellsvar

    if clicked != True:
        # Blå ruta (kategori = -1)
        if 10 < mouseX < 140 and 200 < mouseY < 280:
            clicked = True
            Kategori.visible = False
            volvoLabel.visible = False
            motorLabel.visible = False
            yellow.visible = True
            orange.visible = True
            spawn()



        # Röda ruta (kategori = 1)
        elif 260 < mouseX < 390 and 200 < mouseY < 280:
            clicked = True
            Kategori.visible = False
            volvoLabel.visible = False
            motorLabel.visible = False
            yellow.visible = True
            orange.visible = True
            index = random.randint(0, len(fraglista2) - 1)
            aktuellfraga = fraglista2.pop(index)
            aktuellsvar = svarlista2.pop(index)
            Fraga.value = aktuellfraga

    elif Fraga.value not in ("Rätt","Fel"):
        # blå
        if 10 < mouseX < 140 and 200 < mouseY < 280:
            if svar1.centerX == 70 and svar1.centerY == 240:
                Fraga.value = "Rätt"

            else:
                Fraga.value = "Fel"
                pass
        # röd
        elif 260 < mouseX < 390 and 200 < mouseY < 280:
            if svar1.centerX == 330 and svar1.centerY == 240:
                Fraga.value = "Rätt"

            else:
                Fraga.value = "Fel"
                pass
        # gul
        elif 10 < mouseX < 140 and 300 < mouseY < 380:
            if svar1.centerX == 70 and svar1.centerY == 340:
                Fraga.value = "Rätt"

            else:
                Fraga.value = "Fel"
            pass
        # orange
        elif 260 < mouseX < 390 and 300 < mouseY < 380:
            if svar1.centerX == 330 and svar1.centerY == 340:
                Fraga.value = "Rätt"

            else:
                Fraga.value = "Fel"

            pass

def onStep():
    if Fraga.value in ("Rätt","Fel"):
        timer.fill = "blue"
        if timer.width > 2:
            timer.visible = True
            timer.width -= 2
        if timer.width == 2:
            timer.visible = False
            timer.width = 100
            spawn()

    pass


cmu_graphics.run()
#databas
