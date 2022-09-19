import turtle
import math
import winsound

# music
winsound.PlaySound('song2.wav', winsound.SND_ASYNC)

t = turtle.Turtle()

turtle.bgcolor('black')

def updown(x,y,tut):
    tut.penup()
    tut.goto(x,y)
    tut.pendown()

def names(x,y,nam,size,col):
    w = turtle.Turtle()
    updown(x,y,w)
    w.color(col)
    style = ('Bradley Hand ITC',size, 'italic')
    w.write(nam, font=style, align='center')
    w.hideturtle()

    

def jewles(a,tut):
    tut.speed(100)
    tut.fillcolor("purple")
    tut.begin_fill()
    tut.circle(a)
    tut.end_fill()
    tut.hideturtle()

def mukut(x,y,loop):
    m= turtle.Turtle()
    m.speed(100)
    m.pencolor("gold")
    updown(x,y,m)
    m.right(180)
    m.width(3)
    for i in range(loop):
        jewles(12,m)
        m.forward(20)
        jewles(12,m)
        
def jumka(x,y):
    s = turtle.Turtle()
    s.hideturtle()
    s.pencolor("gold")
    updown(x,y,s)
    #s.fillcolor("gold")

    s.right(90)
    s.width(8)

    jewles(10,s)

    s.right(180)

    jewles(10,s)

    s.right(180)
    s.forward(10)
    s.right(90)

    jewles(10,s)

    s.penup()

    s.hideturtle()
    
        
        
        
        
names(300,-300,"|| PRATHAM CODE||",30,"GOLD")
    
        
t.speed(100)
t.color("WHITE")
t.begin_fill()
t.circle(160 )           ###face 
t.end_fill()

names(400,200,'BHALCHANDRA',30,"white")

###round sund
                
updown(-54,-15,t)                  
t.speed(100)
for i in range(80):       
    if(i<60):
        t.color("black","white")
        t.begin_fill()
        t.circle(i)
        t.left(5)
        t.end_fill()
        t.hideturtle()
        
names(-300,-10,'VAKRA-TUNDA',30,"white")

 ##stright sund 
j=-20
t.speed(100)
for i in range(30):    
    j=j+3                    
    updown(-52, j,t)               
    t.begin_fill()
    t.color("black","white")
    t.circle(60)
    t.end_fill()
    
t.begin_fill()
t.speed(100)
t.color("white","white")
t.circle(60)
t.end_fill()
t.hideturtle()


#right kaan updated

t.pencolor("white")
updown(105,280,t)
t.right(130)
t.speed(0)
t.right(145) #140
t.begin_fill()
t.color("white","white")

for i in range(39):
    t.forward(3.4) #90
    t.right(1.2) #0.8

t.right(100) #110

    # ear 2nd part
for i in range(3):
    for s in range(4):
        t.forward(9)
        t.left(15)
    for s in range(4):
        t.forward(9)
        t.right(15)
    # ear 3rd part

t.right(70)
for i in range(30):
    t.forward(5)
    t.right(3)
t.end_fill()
t.hideturtle()





# # left kaan updated

t.pencolor("white")
updown(-105,280,t)
t.left(78.6)
t.speed(100)
# t.right(145) #140
t.begin_fill()
t.color("white","white")

for i in range(39):
    t.forward(3.4) #90
    t.left(1.2) #0.8

t.left(100) #110

    # ear 2nd part
for i in range(3):
    for s in range(4):
        t.forward(9)
        t.right(15)
    for s in range(4):
        t.forward(9)
        t.left(15)
    # ear 3rd part
t.left(70)
for i in range(30):
    t.forward(5)
    t.left(3)
t.end_fill()
t.hideturtle()

w = turtle.Turtle()
updown(-400,150,w)
w.color('blue')
style = ('Bradley Hand ITC', 30, 'italic')
w.write('LAMBA-KARNA', font=style, align='center')
w.hideturtle()

 

###eye left

t.speed(100)
updown(-60,200,t)          
t.right(50)
t.pencolor('black')
t.speed(100)
for i in range(90):
    t.circle(15)
    t.lt(1)
    t.circle(15)
    t.lt(1)
    


updown(-60,195,t)         
t.left(60)
t.pendown()
t.pencolor('white')
t.speed(0)
for i in range(40):
    t.circle(9)
    t.lt(1)
    t.circle(9)
    t.lt(1)

# ###eye right



updown(60,200,t)         #move the turtle to a location
t.left(98)
t.pencolor('black')
t.speed(100)
for i in range(90):
    t.circle(15)
    t.lt(1)
    t.circle(15)
    t.lt(1)
    


updown(60,195,t)        
t.left(60)
t.pencolor('white')
t.speed(100)
for i in range(40):
    t.circle(9)
    t.lt(1)
    t.circle(9)
    t.lt(1)

# cresent moon

t.penup()                #don't draw when turtle moves
t.goto(-10,270)         #move the turtle to a location
t.pendown()
t.width(8)
t.pencolor('red')
t.right(160)
for i in range(27):
    t.forward(2)
    t.left(7)
    
t.penup()
t.goto(-10,270)         
t.pendown()
t.right(206)
for i in range(36):
    t.forward(2)
    t.left(6.1)
t.left(140)
t.forward(11)
t.hideturtle()

     ###black crecent mooon 
    
t.penup()                
t.goto(-10,270)         
t.width(4)
t.right(180)
t.pendown()

t.width(2)
t.pencolor('black')
t.right(160)

for i in range(27):
    t.forward(2)
    t.left(7)
t.penup()
t.goto(-10,270)         
t.pendown()
t.right(206)
for i in range(36):
    t.forward(2)
    t.left(6.1)

## ekdant 

y=13
radius=10
x=57
t.speed(100)
for i in range(40):
    updown(x,y,t) 
    t.begin_fill()
    t.pencolor('white')
    t.left(4)
    t.circle(radius)
    y=y-1
    radius=radius-0.17         #radius/n no of for loops 
    x=x+1
    t.end_fill
    
w = turtle.Turtle()
w.hideturtle()
updown(200,0,w)
w.color('blue')
style = ('Bradley Hand ITC',30, 'italic')
w.write('EK-DANT', font=style, align='center')
w.hideturtle()


jumka(180,240)
jumka(-180,240)

mukut(88,305,9)
mukut(76,327,8)
mukut(64,347,7)
mukut(52,370,6)

##ashirwaad
# hand
def hand(a):
    hnd.speed(1000000)
    hnd.forward(a)
    hnd.circle(6, 180)
    hnd.forward(a)
    hnd.right(180)
hnd= turtle.Turtle()
hnd.pencolor("white")
hnd.penup()
hnd.goto(-180,-115)
hnd.pendown()
hnd.left(90)
hnd.forward(35)
hand(15)
hand(40)
hand(50)
hand(40)
hand(25)
hnd.left(180)
hnd.forward(40)
hnd.circle(30.2,180)
hnd.forward(15)
hnd.penup()
hnd.goto(-210,-108)

hnd.color('red', 'yellow')
hnd.begin_fill()
for i in range (100):
    hnd.forward(math.sqrt(i)*6)
    hnd.left(170)
hnd.end_fill()
hnd.hideturtle()

avs= turtle.Turtle()
y=-130
radius=15
x=-200
avs.speed(100)
for i in range(100):    
    avs.penup()              
    avs.goto(x, y)      
    avs.pendown()
    avs.color("red","red")
    avs.circle(radius)
    y=y-1.9
    radius=radius+0.75
    x=x+2
avs.hideturtle()



names(-300,-300,'Ganpati bappa morya !!!',30,"white")

turtle.done()