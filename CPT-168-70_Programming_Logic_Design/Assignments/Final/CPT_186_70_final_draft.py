import turtle

def draw_octagon(x, y, size, fill_color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor("ivory")
    turtle.fillcolor(fill_color)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(8):
        turtle.forward(size)
        turtle.right(45)
    turtle.end_fill()

def draw_text(x, y, text, font_size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor(color)
    turtle.write(text, align="center", font=("Arial", font_size, "bold"))

def draw_rectangle(x, y, width, height, fill_color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor("black") 
    turtle.fillcolor(fill_color)    
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_diamond(x, y, size, fill_color):
    turtle.penup()
    turtle.goto(x, y)  
    turtle.pencolor("black")  
    turtle.fillcolor(fill_color) 
    turtle.setheading(45)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)  
    turtle.end_fill()
    turtle.setheading(0)

def draw_stop_sign():
    draw_octagon(x=-50, y=50, size=100, fill_color="red")
    draw_text(x=0, y=-110, text="STOP", font_size=50, color="white")

def draw_speed_limit_sign():
    draw_rectangle(x=-250, y=170, width=100, height=150, fill_color="white")
    draw_text(x=-200, y=130, text="SPEED", font_size=18, color="black")
    draw_text(x=-200, y=105, text="LIMIT", font_size=18, color="black")
    draw_text(x=-200, y=30, text="45", font_size=50, color="black")

def draw_pedestrian_sign():
    draw_diamond(x=150, y=100, size=100, fill_color="yellow")  
    draw_text(x=220, y=70, text="🚶", font_size=50, color="black") 
    draw_rectangle(x=175, y=20, width=100, height=50, fill_color="yellow")
    draw_text(x=225, y=-10, text="PED", font_size=20, color="black")
    draw_text(x=225, y=-35, text="XING", font_size=20, color="black")   


def main():
    turtle.speed(3)
    turtle.bgcolor("grey")
    turtle.pensize(3)
    draw_stop_sign()
    draw_speed_limit_sign()
    draw_pedestrian_sign()
    turtle.hideturtle()
    turtle.done()

main()
