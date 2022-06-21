from operator import imod
import turtle
import random
import winsound

#set up the screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders")
win.bgpic("space_invaders_background.gif")
win.setup(width=800, height=700)
win.tracer(0)
 
#Register the shapes
win.register_shape("invader.gif")
win.register_shape("player.gif")
#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.goto(0,-250)
player.setheading(90)

#Score
score = 0
#Draw the score
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.shape("square")
pen.color("white")
pen.goto(-295,280)
pen.write("Score: {} ".format(score),align="left",font=("Courier",14,"bold"))


# Choose number of enemies
no_of_enemies = 5
enemies = []

for i in range(no_of_enemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(150,200)
    enemy.goto(x,y)

enemyspeed = 0.1

#Player defence system
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed = 1
#bullet state
#ready = ready to fire
#fire = bullet  is firing

bulletstate = "ready"


#move the player
player.speed = 0

def move_left():
    player.speed = -0.1
    
def move_right():
    player.speed = 0.1

def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)
#functions for bullet
def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("space_Invaders_laser.wav",winsound.SND_ASYNC)
        bulletstate = "fire"
        #move the bullet just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    if t1.distance(t2)<15:
        winsound.PlaySound("space_Invaders_explosion.wav",winsound.SND_ASYNC)
        return True
    else: 
        return False

#key bindings

win.listen()
win.onkeypress(move_left,"a")
win.onkeypress(move_right,"d")
win.onkeypress(fire_bullet,"space")


#main loop
while True:
    win.update()
    move_player()
    for enemy in enemies:
    #move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Move the enemy back and down
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            #Move all the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1
            
        
        # check for collision between bullet and enemy
        if isCollision(enemy,bullet):
            #reset the bullet
           
            bullet.hideturtle()
            bulletstate = "ready"
            # bullet.goto(0,-400)
            x = random.randint(-200,200)
            y = random.randint(150,200)
            enemy.goto(x,y)
            #update the score
            pen.clear()
            score += 10
            pen.write("Score: {} ".format(score),align="left",font=("Courier",14,"bold"))


        if isCollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game over")
            break
    
    #Move the bullet
    if bulletstate == "fire":
        
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check buller collision with border
    if bullet.ycor() > 280:
        bullet.hideturtle()
        bulletstate = "ready"

    
