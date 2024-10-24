import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("SNAKE GAME")
wn.bgcolor("#000087")
wn.setup(width=700, height=700)

head = turtle.Turtle()
head.shape("circle")
head.color("white")
head.penup()
head.speed(0)
head.goto(0, 0)
head.direction = "Stop"

food = turtle.Turtle()
colors = random.choice(['red', 'pink', 'green', 'brown'])
shapes = random.choice(['square', 'circle'])
food.shape(shapes)
food.color(colors)
food.penup()
food.speed(0)
food.goto(0, 100)

pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 250)
pen.speed(0)
pen.hideturtle()
pen.write("My Score: 0   High Score: 0", align="center", font=("Ariel", 26, "bold"))


def up():
    if head.direction != "down":
        head.direction = "up"

def down():
    if head.direction != "up":
        head.direction = "down"

def right():
    if head.direction != "left":
        head.direction = "right"

def left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()    
        head.sety(y + 20 )
    if head.direction == "down":
        y = head.ycor()    
        head.sety(y - 20 )
    if head.direction == "right":
        x = head.xcor()    
        head.setx(x + 20 )
    if head.direction == "left":
        x = head.xcor()    
        head.setx(x - 20 )


wn.listen()
wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(right, "d")
wn.onkeypress(left, "a")

segments = []


while True :
    wn.update()

    if(
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"
        colors = random.choice(['red', 'pink', 'green', 'brown'])
        shapes = random.choice(['square', 'circle'])
        food.shape(shapes)
        food.color(colors)
        for segment in segments:
            segment.hideturtle()
        segment.clear()   
        score = 0
        delay = 0.1
        pen.clear() 
        pen.write(
                "Score: {}  High Score: {}".format(score, high_score),
                align = "center", font = ("Ariel", 26, "bold")
            )

    if head.distance(food) < 20:
        x = random.randint(-270, 270)  
        y = random.randint(-270, 270)  
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("circle")
        new_segment.color("pink")
        new_segment.speed(0)
        new_segment.penup()
        segment.append(new_segment)
        delay -= 0.001
        score += 10

        if score > high_score :
            high_score = score

        pen.clear() 
        pen.write(
            "Score: {}  High Score: {}".format(score, high_score),
                align = "center", font = ("Ariel", 26, "bold")
        ) 

    for index in range(len(segment) - 1, 0, - 1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segment) > 0:
       x = head.xcor() 
       y = head.ycor()
       segments[0].goto(x, y) 
    move() 

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "Stop"
            colors = random.choice(['red', 'pink', 'green', 'brown'])
            shapes = random.choice(['square', 'circle'])
            food.shape(shapes)
            food.color(colors)
        for segment in segments:
            segment.hideturtle()
            segment.clear()   
            score = 0
            delay = 0.1
            pen.clear() 
            pen.write(
                "Score: {}  High Score: {}".format(score, high_score),
                align = "center", font = ("Ariel", 26, "bold")
            ) 
    time.sleep(delay)         