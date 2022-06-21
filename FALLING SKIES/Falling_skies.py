import random
import turtle
import time
from tkinter import *
from tkinter import messagebox
import winsound

score = 0
lives = 3

#Setting up the screen
win = turtle.Screen()
win.title("Falling Skies")
win.bgcolor("green")
win.bgpic("background.gif")
win.setup(width=800, height=600)
win.tracer(0)

win.register_shape("deer_left.gif")
win.register_shape("deer_right.gif")
win.register_shape("nut.gif")
win.register_shape("hunter.gif")


#Add the player
player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("deer_left.gif")
player.color("white")
player.goto(0,-250)
player.direction = "stop"

#Create a list of good_guys
good_guys = []
#Add the good_guy
for i in range(15):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.penup()
    good_guy.shape("nut.gif")
    good_guy.color("blue")
    good_guy.goto(-100,250)
    # good_guy.speed = random.randint(1,2)
    good_guys.append(good_guy)

#Create a list of bad_guys
bad_guys = []
#Add the bad_guy
for i in range(10):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.penup()
    bad_guy.shape("hunter.gif")
    bad_guy.color("red")
    bad_guy.goto(100,250)
    # bad_guy.speed = random.randint(1,2)
    bad_guys.append(bad_guy)

# Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.shape("square")
pen.color("white")
pen.goto(0,250)
pen.write("Score: {}  Lives: {}".format(score,lives),align="center",font=("Courier",18,"bold"))

#functions
def go_left():
    player.direction = "left"
    player.shape("deer_left.gif")

def go_right():
    player.direction = "right"
    player.shape("deer_right.gif")

#key bindings
win.listen()
win.onkeypress(go_left,"a")
win.onkeypress(go_right,"d")


#main loop
while True:
    win.update()
    if player.xcor() > 390 or player.xcor() < -390 :
        time.sleep(1)
        player.goto(0,-250)
        player.direction = "stop"

    #moving the player
    if player.direction == "left":
        x = player.xcor()
        x -= 0.60
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 0.60
        player.setx(x)

    #moving the good_guys
    for good_guy in good_guys:
        y = good_guy.ycor()
        # y -= good_guy.speed
        y -= 0.40
        good_guy.sety(y)

        #check if off the screen
        if y < -300:
            x = random.randint(-300,300)
            y = random.randint( 200,300)
            good_guy.goto(x,y) 

        # Check for a collision with the player
        if good_guy.distance(player)<40:
            winsound.PlaySound("success.wav", winsound.SND_ASYNC)
            x = random.randint(-300,300)
            y = random.randint(-200,300)
            good_guy.goto(x,y) 
            score += 10
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score,lives),align="center",font=("Courier",18,"bold"))

#moving the bad_guys
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        # y -= good_guy.speed
        y -= 0.40
        bad_guy.sety(y)

        #check if off the screen
        if y < -300:
            x = random.randint(-300,300)
            y = random.randint( 200,300)
            bad_guy.goto(x,y) 

        # Check for a collision with the player
        if bad_guy.distance(player)<40:
            winsound.PlaySound("big_impact.wav", winsound.SND_ASYNC)
            x = random.randint(-300,300)
            y = random.randint(-200,300)
            bad_guy.goto(x,y)
            lives -= 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score,lives),align="center",font=("Courier",18,"bold"))
            if lives == 0:
                messagebox.showinfo("showinfo", "Please restart the game")
                quit()
                

            