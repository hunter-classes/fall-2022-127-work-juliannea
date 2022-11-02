import turtle

def ngon(t,numsides,angle,x,y,w,color,sidelen):
    
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    
    for i in range (numsides):
    t.forward(sidelen)
        t.right(angle)
        
wn = turtle.Screen()
## Triangle Shape 
triangle = turtle.Turtle()

ngon(triangle,3,120,0,0,1,"green",50)

##Hexagon Shape

hexagon = turtle.Turtle()

ngon(hexagon,6,60,100,100,1,"blue",100)

##ngon shape 

octagon = turtle.Turtle ()

ngon(octagon,8,45,-50,-50,1,"purple",120)

turtle.exitonclick()
