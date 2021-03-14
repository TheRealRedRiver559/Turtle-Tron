import turtle
import time
import random

#Made By RedRiver559#5916

wn = turtle.Screen()
wn.title('Turtle Tron')
wn.bgcolor('black')
wn.screensize(320,320)
wn.setup(width=320, height=320,startx=None,starty=None)
wn.tracer(0)

cyan_history = set()
magenta_history = set()
#Special Abilaties
cyan_speed = 8
magenta_speed = 8
Size = 0.5

#Y grid lines
grid_y = turtle.Turtle()
x = -320
for y_lines in range(80):
    grid_y.color('#2F4F4F')
    grid_y.penup()
    grid_y.goto(x, 320)
    grid_y.pendown()
    grid_y.goto(x, -320)
    grid_y.hideturtle()
    x += 8
#X grid lines
grid_x = turtle.Turtle()
y = -320
for x_lines in range(80):
    grid_x.color('#2F4F4F')
    grid_x.penup()
    grid_x.goto(320, y)
    grid_x.pendown()
    grid_x.goto(-320, y)
    grid_x.hideturtle()
    y += 8
#Score
Cyan_Score = 0
Magenta_Score = 0
score = turtle.Turtle()
score.pensize(2)
score.pencolor('White')
score.penup()
score.goto(0,340)
score.pendown()
score.write(f'Cyan {Cyan_Score}, Magenta {Magenta_Score}',align="center",font=("Courier", 24, "normal"))
score.hideturtle()

#Author
name = turtle.Turtle()
name.pensize(2)
name.hideturtle()
name.pencolor('White')
name.penup()
name.goto(0,320)
name.pendown()
name.write('Made By RedRiver559#5916',align='center',font=("Courier", 8, "normal"))
#Controls
info = turtle.Turtle()
info.color('white')
info.penup()
info.goto(-460,230)
info.pendown()
info.write('Cyan Controls\nW = Up\nS = Down\nA = Left\nD = Right',align='Left',font=("Courier", 12, "normal"))
info.penup()
info.home()
info.goto(500,230)
info.pendown()
info.write('Magenta Controls\n↑ = Up\n↓ = Down\n← = Left\n→ = Right',align='Right',font=("Courier", 12, "normal"))
info.hideturtle()
#border
pen = turtle.Turtle()
pen.color('White')
pen.penup()
pen.setposition(-320,-320)
pen.pendown()
pen.pensize(1)
pen.shape('square')
pen.hideturtle()
for x in range(4):
    pen.forward(640)
    pen.left(90)
    wn.update()
pen.penup()
pen.goto(0,380)
pen.pendown()
pen.pencolor('#2F4F4F')
pen.write('Turtle Tron',align="center",font=("Courier", 48, "normal"))

#Cyan Bike
cyan_bike = turtle.Turtle()
cyan_bike.color("#00FFFF")
cyan_bike.penup()
cyan_bike.sety(-224)
cyan_bike.pendown()
cyan_bike.pensize(2)
cyan_bike.shape('turtle')
cyan_bike.shapesize(stretch_wid=Size, stretch_len=Size, outline=1)

#Magenta Bike
magenta_bike = turtle.Turtle()
magenta_bike.color("#FF00FF")
magenta_bike.penup()
magenta_bike.sety(224)
magenta_bike.pendown()
magenta_bike.pensize(2)
magenta_bike.shape('turtle')
magenta_bike.shapesize(stretch_wid=Size, stretch_len=Size, outline=1)

magenta_bike.setheading(-90)
cyan_bike.setheading(90)

#Controls (Up, Down, Left, Right)
#checking if it can reverse in the opposite x or y direction 
#Cyan Bike
def Cyan_Up():
    if cyan_bike.heading() - 270 == 0:
        pass
    else:
        cyan_bike.setheading(90)
def Cyan_Down():
    if cyan_bike.heading() == 90 or 0:
        pass
    else:
        cyan_bike.setheading(-90)
def Cyan_Right():
    if cyan_bike.heading() == 180:
        pass
    else:
        cyan_bike.setheading(0)
def Cyan_Left():
    if cyan_bike.heading() == 0:
        pass
    else:
        cyan_bike.setheading(180)

#Magenta Bike
def Magenta_Up():
    if magenta_bike.heading() - 270 == 0:
        pass
    else:
        magenta_bike.setheading(90)
def Magenta_Down():
    if magenta_bike.heading() == 90 or 0:
        pass
    else:
        magenta_bike.setheading(-90)
def Magenta_Right():
    if magenta_bike.heading() == 180:
        pass
    else:
        magenta_bike.setheading(0)
def Magenta_Left():
    if magenta_bike.heading() == 0:
        pass
    else:
        magenta_bike.setheading(180)
#Explosion Particles
explosion_effects = []
def Explosion(x,y):
    explosion = turtle.Turtle()
    explosion.pensize(1)
    explosion.hideturtle()
    explosion.penup()
    explosion.setposition(x,y)
    explosion.pendown()
    explosion.color('red')
    for _ in range(7):
        length = random.randint(10,30)
        if explosion.stamp() in explosion_effects:
            explosion.clearstamps()
        else:
            explosion_effects.append(explosion.stamp())
        explosion.forward(length)
        explosion.backward(length)
        explosion.left(50)
        wn.update()
    time.sleep(1)
    explosion.clear()
def cyan_win():
    #print('Cyan Wins!')
    global Cyan_Score
    Cyan_Score += 1
    score.clear()
    score.write(f'Cyan {Cyan_Score}, Magenta {Magenta_Score}',align="center",font=("Courier", 24, "normal"))
def magenta_win():
    #print('Magenta Wins!')
    global Magenta_Score
    Magenta_Score += 1
    score.clear()
    score.goto(0,340)
    score.write(f'Cyan {Cyan_Score}, Magenta {Magenta_Score}',align="center",font=("Courier", 24, "normal"))

#Resets All Coords And Historys/Lines
def Reset():
    magenta_bike.sety(224)
    magenta_bike.setx(0)
    cyan_bike.sety(-224)
    cyan_bike.setx(0)
    magenta_bike.setheading(-90)
    cyan_bike.setheading(90)
    cyan_bike.clear()
    magenta_bike.clear()
    magenta_history.clear()
    cyan_history.clear()
    wn.update()

#Keyboard Listener
wn.listen()
#Cyan
wn.onkey(Cyan_Up,'w')
wn.onkey(Cyan_Down,'s')
wn.onkey(Cyan_Right,'d')
wn.onkey(Cyan_Left,'a')
#Magenta
wn.onkey(Magenta_Up,'Up')
wn.onkey(Magenta_Down,'Down')
wn.onkey(Magenta_Right,'Right')
wn.onkey(Magenta_Left,'Left')

#Main Game Loop
while True:
    time.sleep(0.1)
    cyan_bike.forward(cyan_speed)
    magenta_bike.forward(magenta_speed)

    #Position Logging
    x_cyan, y_cyan = round(cyan_bike.xcor()), round(cyan_bike.ycor())
    x_magenta, y_magenta = round(magenta_bike.xcor()), round(magenta_bike.ycor())

    #Border Detection/ Border Scoring
    if (x_cyan, y_cyan) in magenta_history or (x_cyan, y_cyan) in cyan_history:
        #print('Maginta Wins!')
        Explosion(x_cyan,y_cyan)
        magenta_win()
        Reset()
    elif (x_magenta, y_magenta) in cyan_history or (x_magenta, y_magenta) in magenta_history:
        #print('Cyan Wins!')
        Explosion(x_magenta,y_magenta)
        cyan_win()
        Reset()
    #Border Control
    elif cyan_bike.xcor() >= 320 or cyan_bike.xcor() <= -320:
        #print('Out Of Bounds')
        Explosion(x_cyan,y_cyan)
        magenta_win()
        Reset()
    elif cyan_bike.ycor() >= 320 or cyan_bike.ycor() <= -320:
        #print('Out Of Bounds')
        Explosion(x_cyan,y_cyan)
        magenta_win()
        Reset()
    elif magenta_bike.xcor() >= 320 or magenta_bike.xcor() <= -320:
        #print('Out Of Bounds')
        Explosion(x_magenta,y_magenta)
        cyan_win()
        Reset()
    elif magenta_bike.ycor() >= 320 or magenta_bike.ycor() <= -320:
        #print('Out Of Bounds')
        Explosion(x_magenta,y_magenta)
        cyan_win()
        Reset()
    elif (x_cyan,y_cyan) == (x_magenta,y_magenta):
        #print('Tie')
        Explosion(x_magenta,y_magenta)
        Reset()
    else:
        cyan_history.add((x_cyan,y_cyan))
        magenta_history.add((x_magenta,y_magenta))
    #Adding New X/Y Coords To Sets/Historys
    #print('\nCyan Logging : ',cyan_history)
    #print('\nMagenta Logging : ',magenta_history)
    wn.update()