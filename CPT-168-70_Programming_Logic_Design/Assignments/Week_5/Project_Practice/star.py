import turtle

star = turtle.Turtle()
star.speed(3)  

sides = 5 
length = 100
angle = 144 

# Draw the star
for x in range(sides):
    star.forward(length)
    star.right(angle) 

turtle.done()