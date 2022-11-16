import turtle
import time
import random
w = 500
h = 500
food_size = 10
Screen = turtle.Screen()
Screen.bgcolor("Green")
Screen.title("Snake game")
Screen.setup(500, 500)
#pen = turtle.Turtle("square")
#pen.penup()

#score
score = 0
pen = turtle.Turtle()
pen.speed(0) 
pen.shape("square") 
pen.color("white") 
pen.penup() 
pen.hideturtle() 
pen.goto(0, 260) 
pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
time.sleep(3)
pen.clear()

# food
food = turtle.Turtle()
food.shape("circle")
food.color("blue")
food.shapesize(1)
food.penup()
food.goto(0, 100)
# snake
# food
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("red")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

list = []
# functions
def go_up():
    if snake.direction != "down":
        snake.direction = "up"
        if snake.direction == "up":
            y = snake.ycor()
            y += 20
            snake.sety(y)


def go_down():
    if snake.direction != "up":
        snake.direction = "down"
        if snake.direction == "down":
            y = snake.ycor()
            y -= 20
            snake.sety(y)


def go_right():
    if snake.direction != "left":
        snake.direction = "right"
        if snake.direction == "right":
            x = snake.xcor()
            x += 20
            snake.setx(x)


def go_left():
    if snake.direction != "right":
        snake.direction = "left"
        if snake.direction == "left":
            x = snake.xcor()
            x -= 20
            snake.setx(x)


"""def move():

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)"""


# keyword
Screen.listen()
Screen.onkeypress(go_up, "w")
Screen.onkeypress(go_down, "s")
Screen.onkeypress(go_right, "d")
Screen.onkeypress(go_left, "a")

while True:
    Screen.update()
    #collision with border
    if snake.xcor()>230 or snake.xcor()<-230 or snake.ycor()>230 or snake.ycor()<-230:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction ="stop"
        score = 0
      
    #collision with food
    if snake.distance(food)<20:
        x=random.randint(-200,200)
        y= random.randint(-200, 200)
        food.goto(x,y)
      
      #add snake body
        snake_body = turtle.Turtle()
        snake_body.speed(0)
        snake_body.shape("square")
        snake_body.color("black")
        snake_body.penup()
        snake_body.penup()
        list.append(snake_body)

      #increase score
        score += 1

      #update score
    pen = turtle.Turtle()
    pen.speed(0) 
    pen.shape("square") 
    pen.color("white") 
    pen.penup() 
    pen.hideturtle() 
    pen.goto(0, 260) 
    pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
    time.sleep(3)
    pen.clear()
  
