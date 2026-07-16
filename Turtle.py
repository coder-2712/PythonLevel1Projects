import turtle
import random 
import math
screen = turtle.Screen()
screen.setup(1200,900)
screen.bgcolor("#0F0C38")
stars = turtle.Turtle()
stars.hideturtle()
stars.speed(0)
stars.penup()
stars.color("white")

for i in range(350):
    x = random.randint(-590,590)
    y = random.randint(-440,440)
    stars.goto(x,y)
    stars.dot(random.choice([2,2,2,3,3,4]))
for i in range(20):
    stars.goto(random.randint(-590,590),random.randint(-440,440))
    stars.dot(3,"khaki")

for i in range(20):
    stars.goto(random.randint(-590,590),random.randint(-440,440))
    stars.dot(6,"white")
for i in range(30):
    stars.goto(200,150)
    stars.write("+",align="center",font=("Arial",10,"bold"))

stars.end_fill()    
t = turtle.Turtle()
t.penup()
t.setx(-50)
t.sety(-150)
t.pendown()
t.fillcolor("#E86E3F")
t.pencolor(t.fillcolor())
t.begin_fill()
t.circle(70)
t.end_fill()
t.penup()
t.sety(-146)
t.pendown()
t.fillcolor("#F79650")
t.pencolor(t.fillcolor())
t.begin_fill()
t.circle(66)
t.end_fill()
t.penup()
t.sety(-142)
t.pendown()
t.fillcolor("#FCB752")
t.pencolor(t.fillcolor())
t.begin_fill()
t.circle(62)
t.end_fill()
t.penup()
t.sety(-138)
t.pendown()
t.fillcolor("#FDE08A")
t.pencolor(t.fillcolor())
t.begin_fill()
t.circle(58)
t.end_fill()
t.penup()
t.sety(-134)
t.pendown()
t.fillcolor("#FCF4BC")
t.pencolor(t.fillcolor())
t.begin_fill()
t.circle(54)
t.end_fill()
t.hideturtle()


rings = turtle.Turtle()
rings.hideturtle()
rings.speed(0)
rings.penup()

rings.pencolor("#3D3D5A")
rings.pensize(2)

orbit_radii = [100, 145, 195, 255, 330, 425, 540, 675]

sun_x = -50
sun_y = -80   # 10 pixels lower than before

for radius in orbit_radii:
    rings.goto(sun_x, sun_y - radius)
    rings.pendown()
    rings.circle(radius)
    rings.penup()
    rings.penup()


mercury = turtle.Turtle()
mercury.hideturtle()
mercury.speed(0)
mercury.penup()

mercury_angle = 0
mercury_radius = 100
mercury_speed = 0.25

venus = turtle.Turtle()
venus.hideturtle()
venus.speed(0)
venus.penup()

venus_angle = 45
venus_radius = 145
venus_speed = 0.18

earth = turtle.Turtle()
earth.hideturtle()
earth.speed(0)
earth.penup()

earth_angle = 120
earth_radius = 195
earth_speed = 0.14


mars = turtle.Turtle()
mars.hideturtle()
mars.speed(0)
mars.penup()

mars_angle = 180
mars_radius = 255
mars_speed = 0.11

jupiter = turtle.Turtle()
jupiter.hideturtle()
jupiter.speed(0)
jupiter.penup()

jupiter_angle = 240
jupiter_radius = 330
jupiter_speed = 0.05
saturn = turtle.Turtle()
saturn.hideturtle()
saturn.speed(0)
saturn.penup()

saturn_angle = 300
saturn_radius = 425
saturn_speed = 0.035

uranus = turtle.Turtle()
uranus.hideturtle()
uranus.speed(0)
uranus.penup()

uranus_angle = 30
uranus_radius = 540
uranus_speed = 0.025

neptune = turtle.Turtle()
neptune.hideturtle()
neptune.speed(0)
neptune.penup()

neptune_angle = 150
neptune_radius = 675
neptune_speed = 0.018

screen.tracer(0)

while True:

    mercury.clear()

    mercury_angle += mercury_speed

    mx = sun_x + mercury_radius * math.cos(math.radians(mercury_angle))
    my = sun_y + mercury_radius * math.sin(math.radians(mercury_angle))

    r = 12

    mercury.penup()
    mercury.goto(mx, my-r)
    mercury.setheading(0)

    mercury.color("#A0A0A0")
    mercury.begin_fill()
    mercury.circle(r)
    mercury.end_fill()

    mercury.goto(mx-4, my+5)
    mercury.dot(3,"#707070")

    mercury.goto(mx+5, my+2)
    mercury.dot(2,"#6A6A6A")

    mercury.goto(mx-5, my-3)
    mercury.dot(3,"#7A7A7A")

    mercury.goto(mx+3, my-6)
    mercury.dot(2,"#666666")

    mercury.goto(mx-1, my)
    mercury.dot(2,"#5F5F5F")


    venus.clear()

    venus_angle += venus_speed

    vx = sun_x + venus_radius * math.cos(math.radians(venus_angle))
    vy = sun_y + venus_radius * math.sin(math.radians(venus_angle))

    r = 15

    # Glow
    venus.penup()
    venus.goto(vx, vy-20)
    venus.color("#1B1F37")
    venus.begin_fill()
    venus.circle(20)
    venus.end_fill()

    venus.goto(vx, vy-18)
    venus.color("#343A5B")
    venus.begin_fill()
    venus.circle(18)
    venus.end_fill()

    # Planet
    venus.goto(vx, vy-r)
    venus.setheading(0)

    venus.color("#D8B86A")
    venus.begin_fill()
    venus.circle(r)
    venus.end_fill()

    # Craters
    venus.goto(vx-5, vy+7)
    venus.dot(4, "#CFA85C")

    venus.goto(vx+5, vy+3)
    venus.dot(3, "#C49A4D")

    venus.goto(vx-5, vy-2)
    venus.dot(3, "#CFA85C")

    venus.goto(vx+3, vy-4)
    venus.dot(2, "#B98E43")

    venus.goto(vx-2, vy+1)
    venus.dot(2, "#C49A4D")


    earth.clear()

    earth_angle += earth_speed

    ex = sun_x + earth_radius * math.cos(math.radians(earth_angle))
    ey = sun_y + earth_radius * math.sin(math.radians(earth_angle))

    # Planet
    earth.penup()
    earth.goto(ex, ey-20)
    earth.color("#2C5EA8")
    earth.begin_fill()
    earth.circle(20)
    earth.end_fill()

    earth.goto(ex, ey-18)
    earth.color("#3D74D8")
    earth.begin_fill()
    earth.circle(18)
    earth.end_fill()

    earth.goto(ex, ey-16)
    earth.color("#007BFF")
    earth.begin_fill()
    earth.circle(16)
    earth.end_fill()

    earth.goto(ex-7, ey+6)
    earth.dot(10, "green")

    earth.goto(ex+7, ey-5)
    earth.dot(8, "green")

    earth.goto(ex+3, ey+3)
    earth.dot(9, "green")

    # Ice caps
    earth.goto(ex, ey+13)
    earth.dot(4, "white")

    earth.goto(ex, ey-13)
    earth.dot(4, "white")

    mars.clear()

    mars_angle += mars_speed

    mars_x = sun_x + mars_radius * math.cos(math.radians(mars_angle))
    mars_y = sun_y + mars_radius * math.sin(math.radians(mars_angle))

    mars_size = 25

    mars.penup()
    mars.goto(mars_x, mars_y - mars_size)
    mars.setheading(0)
    mars.color("#b34a2e")
    mars.begin_fill()
    mars.circle(mars_size)
    mars.end_fill()

    mars.goto(mars_x-8, mars_y+8)
    mars.dot(5, "#6b2d1a")

    mars.goto(mars_x+7, mars_y-4)
    mars.dot(4, "#6b2d1a")

    mars.goto(mars_x-2, mars_y-10)
    mars.dot(3, "#6b2d1a")

    mars.goto(mars_x+10, mars_y+9)
    mars.dot(2, "#6b2d1a")

    mars.goto(mars_x-12, mars_y+5)
    mars.dot(4, "#d66b3c")

    jupiter.clear()

    jupiter_angle += jupiter_speed

    jupiter_x = sun_x + jupiter_radius * math.cos(math.radians(jupiter_angle))
    jupiter_y = sun_y + jupiter_radius * math.sin(math.radians(jupiter_angle))

    jupiter_size = 45

    # Planet
    jupiter.penup()
    jupiter.goto(jupiter_x, jupiter_y - jupiter_size)
    jupiter.setheading(0)
    jupiter.color("#d9a066")
    jupiter.begin_fill()
    jupiter.circle(jupiter_size)
    jupiter.end_fill()

    # Bands
    jupiter.width(5)

    jupiter.penup()
    jupiter.goto(jupiter_x-27, jupiter_y+28)
    jupiter.setheading(0)
    jupiter.pendown()
    jupiter.color("#b86f3c")
    jupiter.forward(55)

    jupiter.penup()
    jupiter.goto(jupiter_x-35, jupiter_y+15)
    jupiter.pendown()
    jupiter.color("#f1c27d")
    jupiter.forward(70)

    jupiter.penup()
    jupiter.goto(jupiter_x-42, jupiter_y)
    jupiter.pendown()
    jupiter.color("#c47a45")
    jupiter.forward(85)

    jupiter.penup()
    jupiter.goto(jupiter_x-35, jupiter_y-15)
    jupiter.pendown()
    jupiter.color("#f1c27d")
    jupiter.forward(70)

    jupiter.penup()
    jupiter.goto(jupiter_x-27, jupiter_y-28)
    jupiter.pendown()
    jupiter.color("#b86f3c")
    jupiter.forward(55)

    jupiter.penup()
    jupiter.goto(jupiter_x+18, jupiter_y-10)
    jupiter.dot(14, "#a64b32")

    jupiter.goto(jupiter_x-20, jupiter_y+20)
    jupiter.dot(8, "#8b5a35")

    saturn.clear()

    saturn_angle += saturn_speed

    sx = sun_x + saturn_radius * math.cos(math.radians(saturn_angle))
    sy = sun_y + saturn_radius * math.sin(math.radians(saturn_angle))

    saturn.penup()
    saturn.goto(sx, sy-48)
    saturn.setheading(0)
    saturn.color("#D8C07A")
    saturn.begin_fill()
    saturn.circle(48)
    saturn.end_fill()

    saturn.goto(sx, sy-40)
    saturn.color("#0F0C38")
    saturn.begin_fill()
    saturn.circle(40)
    saturn.end_fill()

    saturn.goto(sx, sy-30)
    saturn.color("#E8D39C")
    saturn.begin_fill()
    saturn.circle(30)
    saturn.end_fill()

    saturn.goto(sx-8, sy+8)
    saturn.dot(10, "#D3BE84")

    saturn.goto(sx+10, sy-6)
    saturn.dot(8, "#C9AF6E")

    uranus.clear()

    uranus_angle += uranus_speed

    uranus_x = sun_x + uranus_radius * math.cos(math.radians(uranus_angle))
    uranus_y = sun_y + uranus_radius * math.sin(math.radians(uranus_angle))

    uranus_size = 32

    uranus.penup()
    uranus.goto(uranus_x, uranus_y-(uranus_size+4))
    uranus.color("#5CA9B8")
    uranus.begin_fill()
    uranus.circle(uranus_size+4)
    uranus.end_fill()

    uranus.goto(uranus_x, uranus_y-uranus_size)
    uranus.color("#A8E8E8")
    uranus.begin_fill()
    uranus.circle(uranus_size)
    uranus.end_fill()

    uranus.width(4)
    uranus.penup()
    uranus.goto(uranus_x-19, uranus_y+12)
    uranus.setheading(0)
    uranus.pendown()
    uranus.color("#BFEFEF")
    uranus.forward(38)

    uranus.penup()
    uranus.goto(uranus_x-23, uranus_y)
    uranus.pendown()
    uranus.color("#91DADA")
    uranus.forward(46)

    uranus.penup()
    uranus.goto(uranus_x-19, uranus_y-12)
    uranus.pendown()
    uranus.color("#BFEFEF")
    uranus.forward(38)

    uranus.penup()
    uranus.goto(uranus_x-10, uranus_y+12)
    uranus.dot(8,"#DFFFFF")

    neptune.clear()

    neptune_angle += neptune_speed

    neptune_x = sun_x + neptune_radius * math.cos(math.radians(neptune_angle))
    neptune_y = sun_y + neptune_radius * math.sin(math.radians(neptune_angle))

    neptune_size = 31

    neptune.penup()
    neptune.goto(neptune_x, neptune_y-(neptune_size+4))
    neptune.color("#224C99")
    neptune.begin_fill()
    neptune.circle(neptune_size+4)
    neptune.end_fill()

    neptune.goto(neptune_x, neptune_y-neptune_size)
    neptune.color("#2B5FD9")
    neptune.begin_fill()
    neptune.circle(neptune_size)
    neptune.end_fill()

    neptune.width(4)
    neptune.penup()
    neptune.goto(neptune_x-19, neptune_y+12)
    neptune.setheading(0)
    neptune.pendown()
    neptune.color("#4E84F0")
    neptune.forward(38)

    neptune.penup()
    neptune.goto(neptune_x-23, neptune_y)
    neptune.pendown()
    neptune.color("#1E46A8")
    neptune.forward(46)

    neptune.penup()
    neptune.goto(neptune_x-19, neptune_y-12)
    neptune.pendown()
    neptune.color("#4E84F0")
    neptune.forward(38)

    neptune.penup()
    neptune.goto(neptune_x+10, neptune_y-5)
    neptune.dot(10, "#173A87")

    neptune.goto(neptune_x+12, neptune_y+6)
    neptune.dot(5, "#B8D8FF")

    neptune.goto(neptune_x-10, neptune_y+12)
    neptune.dot(7, "#CFE6FF")

    screen.update()
