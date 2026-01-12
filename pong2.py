from turtle import Turtle, Screen
import random
import time
solo_läge = False
coop_läge = False
versus_läge = False
spel_över = False  

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Ping Pong Special")
screen.tracer(0) 

pausad_boll_fart = 0
boll_start_hastighet = 0.15
boll_snabbhet = boll_start_hastighet
utrymme = 40 
boll_hastighets_ökning = 0.02
paus = False

score_1 = 0 
score_2 = 0 


pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)



linje = Turtle()
linje.speed(0)
linje.color("white")
linje.penup()
linje.hideturtle()
linje.goto(0, 300)
linje.setheading(270)
linje.pensize(2)

def rita_nät():
    linje.goto(0, 300)
    for _ in range(15):
        linje.pendown()
        linje.forward(20)
        linje.penup()
        linje.forward(20)

pongboll = Turtle()
pongboll.speed(0)
pongboll.shape("circle")
pongboll.color("white")
pongboll.penup()
pongboll.dx = boll_snabbhet
pongboll.dy = boll_snabbhet

spelar1 = Turtle()
spelar1.speed(0)
spelar1.shape("square")
spelar1.shapesize(stretch_wid=5, stretch_len=1)
spelar1.color("red")
spelar1.penup()
spelar1.setposition(350, 0)


spelar2 = Turtle()
spelar2.speed(0)
spelar2.shape("square")
spelar2.shapesize(stretch_wid=5, stretch_len=1)
spelar2.color("blue")
spelar2.penup()
spelar2.setposition(-350, 0)





def spelar1_upp():
    if not paus and versus_läge:
        y = spelar1.ycor()
        if y < 250:  
            y += utrymme
            spelar1.sety(y)

def spelar1_ner():
    if not paus and versus_läge:
        y = spelar1.ycor()
        if y > -240: 
            y -= utrymme
            spelar1.sety(y)

def spelar2_upp():
    if not paus:
        y = spelar2.ycor()
        if y < 250:
            y += utrymme
            spelar2.sety(y)

def spelar2_ner():
    if not paus:
        y = spelar2.ycor()
        if y > -240:
            y -= utrymme
            spelar2.sety(y)

def reset_boll():
    global boll_snabbhet
    pongboll.goto(0, 0)

    pongboll.dx *= -1 
   
    if pongboll.dx > 0:
        pongboll.dx = boll_start_hastighet
    else:
        pongboll.dx = -boll_start_hastighet

def nytt_spel():
    global score_1, score_2, boll_snabbhet, spel_över
    score_1 = 0
    score_2 = 0
    boll_snabbhet = boll_start_hastighet
    spel_över = False 
    
    pongboll.goto(0, 0)
    pongboll.dx = boll_snabbhet
    pongboll.dy = boll_snabbhet
    spelar1.goto(350, 0)   
    spelar2.goto(-350, 0)
    
    pen.clear()
    pen.write("RESTART", align="center", font=("Courier", 30, "bold"))
    screen.update()
    time.sleep(1)
    pen.clear()
    pen.write("READY?", align="center", font=("Courier", 30, "bold"))
    screen.update()
    time.sleep(1)
    pen.clear()
    pen.write("3", align="center", font=("Courier", 30, "bold"))
    screen.update()
    time.sleep(1)
    pen.clear()
    pen.write("2", align="center", font=("Courier", 30, "bold"))
    screen.update()
    time.sleep(1)
    pen.clear()
    pen.write("1", align="center", font=("Courier", 30, "bold"))
    screen.update()
    time.sleep(1)
    pen.clear()
    pen.write("0 / 0", align="center", font=("Courier", 30, "normal"))

def avsluta_spel():
    global spel_spelar
    spel_spelar = False
    screen.bye()

def toggle_paus():
    global paus
    if paus == True:
        paus = False
        pen.clear() 
        pen.write("{} / {}".format(score_1, score_2), align="center", font=("Courier", 30, "normal"))
    else:
        paus = True
        pen.goto(0, 0)
        pen.write("SPELET ÄR PAUSAT", align="center", font=("Courier", 30, "bold"))
        pen.goto(0, 260) 
    
def solo():
    global solo_läge, menu
    if menu:   #För att se till att man inte råkar ändra läge under ett spel
        solo_läge = True
        menu = False

def coop():
    global coop_läge, menu
    if menu:  #För att se till att man inte råkar ändra läge under ett spel
        coop_läge = True
        menu = False
    

def versus():
    global versus_läge, menu
    if menu:
        versus_läge = True
        menu = False


ai_fart = 10     
svårighet = 1
def ai_lätt():
    global svårighet, solo_meny, coop_meny
    if solo_meny or coop_meny:
        svårighet = 1
        solo_meny = False
        coop_meny = False

def ai_medel():
    global svårighet, solo_meny, coop_meny
    if solo_meny or coop_meny:
        svårighet = 2
        solo_meny = False
        coop_meny = False
 
def ai_svår():
    global svårighet, solo_meny, coop_meny
    if solo_meny or coop_meny:
        svårighet = 3
        solo_meny = False
        coop_meny = False
    
    


def updatera_ai(pongboll, spelar1):
    if svårighet == 1:
        if pongboll.dx > 0: 
            chance = random.randint(1, 100)

            if chance == 1:
                boll_y = pongboll.ycor()
                ai_paddel_y = spelar1.ycor()

                
                if boll_y > ai_paddel_y:
                    
                    if ai_paddel_y < 250: 
                        spelar1.sety(ai_paddel_y + ai_fart)
                    
                elif boll_y < ai_paddel_y:
                    
                    if ai_paddel_y > -240:
                        spelar1.sety(ai_paddel_y - ai_fart)
    if svårighet == 2:
        if pongboll.dx > 0: 
            chance = random.randint(1, 50)

            if chance == 1:
                boll_y = pongboll.ycor()
                ai_paddel_y = spelar1.ycor()

                
                if boll_y > ai_paddel_y:
                    
                    if ai_paddel_y < 250: 
                        spelar1.sety(ai_paddel_y + ai_fart)
                    
                elif boll_y < ai_paddel_y:
                    
                    if ai_paddel_y > -240:
                        spelar1.sety(ai_paddel_y - ai_fart)
    if svårighet == 3:
        if pongboll.dx > 0: 
            chance = random.randint(1, 30)

            if chance == 1:
                boll_y = pongboll.ycor()
                ai_paddel_y = spelar1.ycor()

                
                if boll_y > ai_paddel_y:
                    
                    if ai_paddel_y < 250: 
                        spelar1.sety(ai_paddel_y + ai_fart)
                    
                elif boll_y < ai_paddel_y:
                    
                    if ai_paddel_y > -240:
                        spelar1.sety(ai_paddel_y - ai_fart)


screen.listen()
screen.onkeypress(solo, "v")
screen.onkeypress(coop, "c")
screen.onkeypress(versus, "b")
screen.onkeypress(ai_lätt, "1")
screen.onkeypress(ai_medel, "2")
screen.onkeypress(ai_svår, "3")
solo_meny = True
coop_meny = True
menu = True
#Menyn där man bestämmer om man ska köra själv mot en annan spelare eller om man ska köra tillsammans med en person och möta en AI eller om man ska möta en AI själv
while menu:
    pen.clear()
    pen.write("(Menu)\nSolo (V), Co-op (C), Versus (B)", align="center", font=("Courier", 30, "normal"))
    screen.update()

if solo_läge:
    while solo_meny:
        pen.clear()
        pen.write("Välj svårighets grad på din AI-motståndare (1 = Lätt, 2 = Medel, 3 = Svår)", align="center", font=("Courier", 12, "normal"))
        screen.update()

if coop_läge:
    while coop_meny:
        pen.clear()
        pen.write("Välj svårighets grad på er AI-motståndare (1 = Lätt, 2 = Medel, 3 = Svår)", align="center", font=("Courier", 12, "normal"))
        screen.update()


screen.onkeypress(spelar1_upp, "Up")
screen.onkeypress(spelar1_ner, "Down")
screen.onkeypress(spelar2_upp, "w")
screen.onkeypress(spelar2_ner, "s")
screen.onkeypress(nytt_spel, "r")
screen.onkeypress(avsluta_spel, "x")
screen.onkeypress(toggle_paus, "space")






rita_nät()


pen.clear()
pen.write("READY?", align="center", font=("Courier", 30, "bold"))
screen.update()
time.sleep(1)
pen.clear()
pen.write("3", align="center", font=("Courier", 30, "bold"))
screen.update()
time.sleep(1)
pen.clear()
pen.write("2", align="center", font=("Courier", 30, "bold"))
screen.update()
time.sleep(1)
pen.clear()
pen.write("1", align="center", font=("Courier", 30, "bold"))
screen.update()
time.sleep(1)
pen.clear()
pen.write("0 / 0", align="center", font=("Courier", 30, "normal"))
while solo_läge:
    screen.update()

    if not paus: #Kollar så att spelet inte fortsätter medan spelet är pausat
        updatera_ai(pongboll, spelar1)
        
        # Kör spelmekaniken om spelet inte är över
        if not spel_över:
            pongboll.setx(pongboll.xcor() + pongboll.dx)
            pongboll.sety(pongboll.ycor() + pongboll.dy)

            #Boll i kollision med vägg
            if pongboll.ycor() > 290:
                pongboll.sety(290)
                pongboll.dy *= -1 

            if pongboll.ycor() < -290:
                pongboll.sety(-290)
                pongboll.dy *= -1

            # Poäng utdelning
            if pongboll.xcor() > 390:
                score_1 += 1 
                pen.clear()
                pen.write("{} / {}".format(score_1, score_2), align="center", font=("Courier", 30, "normal"))
                reset_boll()
                spelar1.goto(350, 0)   
                spelar2.goto(-350, 0)
                boll_snabbhet += boll_hastighets_ökning
                screen.update()
                time.sleep(1)
                
            if pongboll.xcor() < -390:
                score_2 += 1
                pen.clear()
                pen.write("{} / {}".format(score_1, score_2), align="center", font=("Courier", 30, "normal"))
                reset_boll()
                spelar1.goto(350, 0)   
                spelar2.goto(-350, 0)
                boll_snabbhet += boll_hastighets_ökning
                screen.update()
                time.sleep(1)
                
            # Kollision med paddlar
            if (340 < pongboll.xcor() < 350) and (spelar1.ycor() - 50 < pongboll.ycor() < spelar1.ycor() + 50):
                pongboll.setx(340)
                pongboll.dx *= -1.1 

            if (-350 < pongboll.xcor() < -340) and (spelar2.ycor() - 50 < pongboll.ycor() < spelar2.ycor() + 50):
                pongboll.setx(-340)
                pongboll.dx *= -1.1 

            # Kolla om någon vunnit
            if score_1 >= 3 or score_2 >= 3:
                winner = "BLUE" if score_1 >= 3 else "RED"
                pen.clear()
                pen.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
                screen.update()
                time.sleep(2)
                pen.clear()
                pen.write(f"{winner} WINS", align="center", font=("Courier", 30, "bold"))
                screen.update()
                time.sleep(2)
                pen.clear()
                pen.write("Play again? (R), else: (X)", align="center", font=("Courier", 30, "bold"))
                screen.update()
                spel_över = True 

while coop_läge:
    screen.update()

    if not paus: #Kollar så att spelet inte fortsätter medan spelet är pausat
        updatera_ai(pongboll, spelar1)
            
        # Kör bara spelmekaniken om spelet inte är över
        if not spel_över:
            pongboll.setx(pongboll.xcor() + pongboll.dx)
            pongboll.sety(pongboll.ycor() + pongboll.dy)

            # Kollision med väggar
            if pongboll.ycor() > 290:
                pongboll.sety(290)
                pongboll.dy *= -1 

            if pongboll.ycor() < -290:
                pongboll.sety(-290)
                pongboll.dy *= -1

            # Poäng utdelning
            if pongboll.xcor() > 390:
                score_1 += 1 
                pen.clear()
                pen.write("{} / {}".format(score_1, score_2), align="center", font=("Courier", 30, "normal"))
                reset_boll()
                spelar1.goto(350, 0)   
                spelar2.goto(-350, 0)
                boll_snabbhet += boll_hastighets_ökning
                screen.update()
                time.sleep(1)
                
            if pongboll.xcor() < -390:
                score_2 += 1
                pen.clear()
                pen.write("{} / {}".format(score_1, score_2), align="center", font=("Courier", 30, "normal"))
                reset_boll()
                spelar1.goto(350, 0)   
                spelar2.goto(-350, 0)
                boll_snabbhet += boll_hastighets_ökning
                screen.update()
                time.sleep(1)
                
            # Kollision med paddlar
            if (340 < pongboll.xcor() < 350) and (spelar1.ycor() - 50 < pongboll.ycor() < spelar1.ycor() + 50):
                pongboll.setx(340)
                pongboll.dx *= -1.1 

            if (-350 < pongboll.xcor() < -340) and (spelar2.ycor() - 50 < pongboll.ycor() < spelar2.ycor() + 50):
                pongboll.setx(-340)
                pongboll.dx *= -1.1 

            # Kolla om någon vunnit
            if score_1 >= 3 or score_2 >= 3:
                winner = "BLUE" if score_2 >= 3 else "RED"
                pen.clear()
                pen.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
                screen.update()
                time.sleep(2)
                pen.clear()
                pen.write(f"{winner} WINS", align="center", font=("Courier", 30, "bold"))
                screen.update()
                time.sleep(2)
                pen.clear()
                pen.write("Play again? (R), else: (X)", align="center", font=("Courier", 30, "bold"))
                screen.update()
                spel_över = True 


while versus_läge:
    screen.update()

    if not paus: #Kollar så att spelet inte fortsätter medan spelet är pausat   
        # Kör bara spelmekaniken om spelet inte är över
        if not spel_över:
            pongboll.setx(pongboll.xcor() + pongboll.dx)
            pongboll.sety(pongboll.ycor() + pongboll.dy)

            # Kollision med väggar
            if pongboll.ycor() > 290:
                pongboll.sety(290)
                pongboll.dy *= -1 

            if pongboll.ycor() < -290:
                pongboll.sety(-290)
                pongboll.dy *= -1

            # Poäng utdelning
            if pongboll.xcor() > 390:
                score_1 += 1 
                pen.clear()
                pen.write("{} / {}".format(score_1, score_2), align="center", font=("Courier", 30, "normal"))
                reset_boll()
                spelar1.goto(350, 0)   
                spelar2.goto(-350, 0)
                boll_snabbhet += boll_hastighets_ökning
                screen.update()
                time.sleep(1)
                
            if pongboll.xcor() < -390:
                score_2 += 1
                pen.clear()
                pen.write("{} / {}".format(score_1, score_2), align="center", font=("Courier", 30, "normal"))
                reset_boll()
                spelar1.goto(350, 0)   
                spelar2.goto(-350, 0)
                boll_snabbhet += boll_hastighets_ökning
                screen.update()
                time.sleep(1)
                
            # Kollision med paddlar
            if (340 < pongboll.xcor() < 350) and (spelar1.ycor() - 50 < pongboll.ycor() < spelar1.ycor() + 50):
                pongboll.setx(340)
                pongboll.dx *= -1.1 

            if (-350 < pongboll.xcor() < -340) and (spelar2.ycor() - 50 < pongboll.ycor() < spelar2.ycor() + 50):
                pongboll.setx(-340)
                pongboll.dx *= -1.1 

            # Kolla om någon vunnit
            if score_1 >= 3 or score_2 >= 3:
                winner = "BLUE" if score_2 >= 3 else "RED"
                pen.clear()
                pen.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
                screen.update()
                time.sleep(2)
                pen.clear()
                pen.write(f"{winner} WINS", align="center", font=("Courier", 30, "bold"))
                screen.update()
                time.sleep(2)
                pen.clear()
                pen.write("Play again? (R), else: (X)", align="center", font=("Courier", 30, "bold"))
                screen.update()
                spel_över = True