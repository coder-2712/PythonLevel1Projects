import turtle
t = turtle.Turtle()
def drawline(x0,y0,x1,y1):
    t.penup()
    t.goto(x0,y0)
    t.pendown()
    t.goto(x1,y1)
def drawrectangle(x0,y0,len,hgt,fillcolor):
    t.fillcolor(fillcolor)
    t.begin_fill()
    drawline(x0,y0,x0+len,y0)
    drawline(x0+len,y0,x0+len,y0+hgt)
    drawline(x0+len,y0+hgt,x0,y0+hgt)
    drawline(x0,y0+hgt,x0,y0)
    t.end_fill()
def pixelcolor(jj,kk,color):
    jj
    kk
    color
xval=-230
yval=150
ncols=30
nrows=30
for jj in range(nrows):
    for kk in range(ncols):
        drawrectangle(xval,yval,15,15,"aliceblue")
        xval = xval+15
    xval=-230
    yval=yval-15
turtle.mainloop()