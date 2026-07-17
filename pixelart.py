import turtle
t = turtle.Turtle()
def drawline(x0,y0,x1,y1):
    t.penup()
    t.goto(x0,y0)
    t.pendown()
    t.goto(x1,y1)
def drawrectangle(x0,y0,len,hgt):
    drawline(x0,y0,x0+len,y0)
    drawline(x0+len,y0,x0+len,y0+hgt)
    drawline(x0+len,y0+hgt,x0,y0+hgt)
    drawline(x0,y0+hgt,x0,y0)
drawline(0,0,100,100)
drawrectangle(60,60,60,60)
turtle.mainloop()