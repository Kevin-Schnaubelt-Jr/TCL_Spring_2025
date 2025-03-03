import turtle

def draw_octagon(x, y, size, color):
    """Draws an octagon at (x, y) with given size and color."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(8):
        turtle.forward(size)
        turtle.right(45)
    turtle.end_fill()

def draw_text(x, y, text, font_size, color):
    """Writes text at (x, y) with given font size and color."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor(color)
    turtle.write(text, align="center", font=("Arial", font_size, "bold"))
    turtle.pendown()

def draw_rectangle(x, y, width, height, color):
    """Draws a rectangle at (x, y) with given width, height, and color."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_diamond(x, y, size, color):
    """Draws a diamond shape at (x, y) with given size and color."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(size)
        turtle.right(60)
        turtle.forward(size)
        turtle.right(120)
    turtle.end_fill()

def draw_stop_sign():
    """Draws a STOP sign in the center of the screen."""
    draw_octagon(-50, 50, 100, "red")
    draw_text(0, 0, "STOP", 20, "white")

def draw_speed_limit_sign():
    """Draws a Speed Limit sign."""
    draw_rectangle(-200, 100, 100, 150, "white")
    draw_text(-150, 50, "SPEED", 15, "black")
    draw_text(-150, 20, "LIMIT", 15, "black")
    draw_text(-150, -10, "45", 20, "black")

def draw_pedestrian_sign():
    """Draws a Pedestrian Crossing sign."""
    draw_diamond(100, 50, 100, "yellow")
    draw_text(150, 0, "🚶", 20, "black")

def main():
    """Main function to draw all signs."""
    turtle.speed(3)
    draw_stop_sign()
    draw_speed_limit_sign()
    draw_pedestrian_sign()
    turtle.hideturtle()
    turtle.done()

main()
