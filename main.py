from cmu_graphics import *
import random
import subprocess
import sys

#databas
app.background = fill="gray"
fraglista = ["Vilket år tillverkades sista v70 modellen",
            "Vilket land kommer Volvo ifrån?",
            "Vilken typ av bil är en Volvo XC90?",
            "Vilken Volvo-modell är endast en elbil?",
            "Vad är smeknamnet på Volvo ÖV 4",
            "Vilket fordon av dessa tillverkar inte Volvo",
            "När grundades Volvo?"
            ]
# Fyra olika alternativ per fråga (ett korrekt, tre fel)
alternativ1 = ["2016", "Sverige", "SUV", "EX40","Jakob","Motorcykel","1927"]
alternativ2 = ["2015", "Tyskland", "Sedan", "V70","Erik","Lastmaskin","1932"]
alternativ3 = ["2017", "USA", "Kombi", "XC60","Hans","Grävmaskin","1937"]
alternativ4 = ["2018", "Japan", "Sportbil", "XC40","Jokke","Dumper","1924"]



fraglista2 = [
   "Vad är det vanligaste motorblock matrialet i nya motorer",
   "Hur många cylindrar har en vanlig Volvo-motor?",
   "Hur många cylindrar har en volvo 850",
   "Vilken typ av bränsle använder Volvo D3?",
    "Vilken volvo har den starkaste motorn?",
    "Hur stark var första kommerciella Volvo motorn"
]
alternativ12 = ["aluminium", "4", "5", "diesel","ES90","40–51Hk"]
alternativ22 = ["gjutjärn", "3", "4", "bensin","V90","30-37hk"]
alternativ32 = ["vismut", "5", "6", "etanol","XC60","45-58hk"]
alternativ42 = ["järn", "6", "8", "gas","EX30","54-60hk"]


clicked = False
aktuellfraga = ""
aktuellsvar = ""
svarfraga = ""
poang = 0
kategori = 0

darkOrange = Rect(10,300,130,80,fill="darkOrange",visible=False)
orange = Rect(260,300,130,80,fill="green",visible=False)
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
    global poang, aktuellsvar, clicked
    if len(fraglista) > 0:
        index = random.randint(0, len(fraglista)- 1)
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
        clicked = "retry?"
#katergori motorfrågor
def spawn2():
    global poang, aktuellsvar, clicked
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
        clicked = "retry?"


#svarafrågor

def onMousePress(mouseX, mouseY):
    global kategori, clicked, aktuellfraga, aktuellsvar, poang

    if clicked == False:
        # Blå ruta (kategori = -1)
        if 10 < mouseX < 140 and 200 < mouseY < 280:
            clicked = True
            kategori = 1
            Kategori.visible = False
            volvoLabel.visible = False
            motorLabel.visible = False
            darkOrange.visible = True
            orange.visible = True
            spawn()

        # Röda ruta (kategori = 1)
        elif 260 < mouseX < 390 and 200 < mouseY < 280:
            clicked = True
            kategori = -1
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
    if clicked == "retry?":

        #blå
        if 10 < mouseX < 140 and 200 < mouseY < 280:
            if svar1.centerX == 70 and svar1.centerY == 240:
                restart()

        # röd
        elif 260 < mouseX < 390 and 200 < mouseY < 280:
            if svar1.centerX == 330 and svar1.centerY == 240:
                Fraga.value = "Rätt"
                poang += 1

        pass

def onStep():
    global kategori
    if Fraga.value in ("Rätt","Fel" + ", rätt svar: " + aktuellsvar):
        timer.fill = "blue"
        if timer.width > 2:
            timer.visible = True
            timer.width -= 2
        if timer.width == 2:
            timer.visible = False
            timer.width = 100
            if kategori == 1:
                spawn()
            else:
                spawn2()

    pass


cmu_graphics.run()