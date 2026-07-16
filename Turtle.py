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

# Centre of Mercury
mx = 50
my = -80
r = 12

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

venus = turtle.Turtle()
venus.hideturtle()
venus.speed(0)
venus.penup()

# Centre of Venus
vx = 95
vy = -80
r = 15
venus.goto(vx,vy-20)
venus.color("#1B1F37")
venus.begin_fill()
venus.circle(20)
venus.end_fill()

venus.goto(vx,vy-18)
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

# Shallow craters
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

earth = turtle.Turtle()
earth.hideturtle()
earth_x = 145
earth_y = -80
earth.penup()
earth.goto(earth_x, earth_y)
earth.dot(40, "#007BFF")

# tiny continents
earth.goto(earth_x - 7, earth_y + 6)
earth.dot(10, "green")

earth.goto(earth_x + 7, earth_y - 5)
earth.dot(8, "green")

earth.goto(earth_x + 3, earth_y + 3)
earth.dot(9, "green")


mars = turtle.Turtle()
mars.speed(0)
mars.hideturtle()

mars_size = 25
mars_x = 200
mars_y = -80

# Mars base
mars.penup()
mars.goto(mars_x, mars_y - mars_size)
mars.pendown()
mars.color("#b34a2e")
mars.begin_fill()
mars.circle(mars_size)
mars.end_fill()

craters = [
    (-8, 8, 5),
    (7, -4, 4),
    (-2, -10, 3),
    (10, 9, 2)
]

for x, y, size in craters:
    mars.penup()
    mars.goto(mars_x + x, mars_y + y)
    mars.pendown()
    mars.color("#6b2d1a")
    mars.dot(size)

mars.penup()
mars.goto(mars_x - 12, mars_y + 5)
mars.pendown()
mars.color("#d66b3c")
mars.dot(4)

jupiter = turtle.Turtle()
jupiter.speed(0)
jupiter.hideturtle()

jupiter_size = 45
jupiter_x = 270
jupiter_y = 0

# Jupiter base
jupiter.penup()
jupiter.goto(jupiter_x, jupiter_y - jupiter_size)
jupiter.pendown()
jupiter.color("#d9a066")
jupiter.begin_fill()
jupiter.circle(jupiter_size)
jupiter.end_fill()

bands = [
    (28, "#b86f3c", 55),
    (15, "#f1c27d", 70),
    (0, "#c47a45", 85),
    (-15, "#f1c27d", 70),
    (-28, "#b86f3c", 55)
]

for y_offset, color, length in bands:
    jupiter.penup()
    jupiter.goto(jupiter_x - length/2, jupiter_y + y_offset)
    jupiter.pendown()
    jupiter.color(color)
    jupiter.width(5)
    jupiter.forward(length)



jupiter.penup()
jupiter.goto(jupiter_x + 18, jupiter_y - 10)
jupiter.pendown()
jupiter.color("#a64b32")
jupiter.dot(14)

jupiter.penup()
jupiter.goto(jupiter_x - 20, jupiter_y + 20)
jupiter.pendown()
jupiter.color("#8b5a35")
jupiter.dot(8)



saturn = turtle.Turtle()
saturn.hideturtle()
saturn.speed(0)
saturn.penup()

sx = 375
sy = -100

# ---------- Outer ring ----------
saturn.goto(sx, sy-48)
saturn.color("#D8C07A")
saturn.begin_fill()
saturn.circle(48)
saturn.end_fill()

# ---------- Cut out middle ----------
saturn.goto(sx, sy-40)
saturn.color("#0F0C38")      # Background colour
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

uranus = turtle.Turtle()
uranus.speed(0)
uranus.hideturtle()

uranus_size = 32
uranus_x = 490
uranus_y = 0

uranus.penup()
uranus.goto(uranus_x, uranus_y - uranus_size)
uranus.pendown()
uranus.color("#A8E8E8")
uranus.begin_fill()
uranus.circle(uranus_size)
uranus.end_fill()

# Soft cloud bands
bands = [
    (12, "#BFEFEF", 38),
    (0, "#91DADA", 46),
    (-12, "#BFEFEF", 38)
]

uranus.width(4)

for y_offset, color, length in bands:
    uranus.penup()
    uranus.goto(uranus_x - length/2, uranus_y + y_offset)
    uranus.pendown()
    uranus.color(color)
    uranus.forward(length)

uranus.penup()
uranus.goto(uranus_x - 10, uranus_y + 12)
uranus.pendown()
uranus.color("#DFFFFF")
uranus.dot(8)

neptune = turtle.Turtle()
neptune.speed(0)
neptune.hideturtle()

neptune_size = 31
neptune_x = 620
neptune_y = 0

# Planet
neptune.penup()
neptune.goto(neptune_x, neptune_y - neptune_size)
neptune.pendown()
neptune.color("#2B5FD9")
neptune.begin_fill()
neptune.circle(neptune_size)
neptune.end_fill()

# Cloud bands
bands = [
    (12, "#4E84F0", 38),
    (0, "#1E46A8", 46),
    (-12, "#4E84F0", 38)
]

neptune.width(4)

for y_offset, color, length in bands:
    neptune.penup()
    neptune.goto(neptune_x - length/2, neptune_y + y_offset)
    neptune.pendown()
    neptune.color(color)
    neptune.forward(length)

# Great Dark Spot
neptune.penup()
neptune.goto(neptune_x + 10, neptune_y - 5)
neptune.pendown()
neptune.color("#173A87")
neptune.dot(10)

# Bright cloud above the storm
neptune.penup()
neptune.goto(neptune_x + 12, neptune_y + 6)
neptune.pendown()
neptune.color("#B8D8FF")
neptune.dot(5)

# Small highlight
neptune.penup()
neptune.goto(neptune_x - 10, neptune_y + 12)
neptune.pendown()
neptune.color("#CFE6FF")
neptune.dot(7)

turtle.mainloop()
