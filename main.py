import turtle
from random import randint
turtle.tracer(0)
turtle.hideturtle()
turtle.penup()
turtle.setpos(0, -300)
turtle.setheading(90)
turtle.pendown()
turtle.pensize(12)
turtle.pencolor("#4d2b0f")

dl = 10
itr = 7
angle = 30 - randint(-15, 15)

def buildTree(itr):
    axiom = "10"
    tempAx = ""
    for j in range(itr):
        ln = len(axiom)
        for i in range(ln):
            if axiom[i] == "[":
                tempAx += "["
            elif axiom[i] == "]":
                tempAx += "]"
            elif axiom[i] == "+":
                tempAx += "+"
            elif axiom[i] == "-":
                tempAx += "-"
            elif axiom[i] == "2":
                tempAx += "2"
            elif axiom[i] == "1":
                tempAx += "12"
            else:
                tempAx += "1[+0-0][-0+0]"
        axiom = tempAx
        tempAx = ""
    print(axiom)
    return axiom
def makeTree(itr):
    stek = []
    angleC = 20
    angleLimits = 10
    axiom = buildTree(itr)
    for ch in axiom:
        dl = randint(7, 10)
        angle = angleC - randint(-angleLimits, angleLimits)
        if ch == "0":
            chose = randint(1, 5)
            if chose == 1:
                turtle.pencolor("#ffd200")
            elif chose == 2:
                turtle.pencolor("#9c5708") #578363
            elif chose == 3:
                turtle.pencolor("#f47b20") #7d8363
            elif chose == 4:
                turtle.pencolor("#f79762")
            else:
                turtle.pencolor("#f05133")
            turtle.pensize(2)
            turtle.forward(2)
            turtle.pencolor("#4d2b0f") #8b5a2b
        elif ch == "1":
            turtle.forward(dl)
        elif ch == "2":
            turtle.forward(dl)
            #turtle.forward(randint(1, dl*2))
        elif ch == "+":
            turtle.left(angle)
        elif ch == "-":
            turtle.right(angle)
        elif ch == "[":
            lcl_width = turtle.pensize()
            lcl_width *= randint(80, 85)/100
            turtle.pensize(lcl_width)
            stek.append(lcl_width)
            stek.append(turtle.xcor())
            stek.append(turtle.ycor())
            stek.append(turtle.heading())
        else:
            turtle.penup()
            turtle.setheading(stek.pop())
            turtle.sety(stek.pop())
            turtle.setx(stek.pop())
            turtle.pensize(stek.pop())
            turtle.pendown()


makeTree(itr)

turtle.exitonclick()