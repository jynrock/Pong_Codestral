import turtle
import os
import time
import random  # Ajoutez cette ligne pour importer le module random

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Raquette gauche
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=6, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Raquette droite
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=6, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350, 0)

# Balle
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5 / 100 # divisé par 100 pour la rendre plus lente
ball.dy = -5 / 100 # divisé par 100 pour la rendre plus lente

# Score
score_a = 0
score_b = 0

# Affichage du score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Joueur 1: 0   Joueur 2: 0", align="center", font=("Courier", 24, "normal"))

# Fonctions de mouvement des raquettes
def paddle_left_up():
    y = paddle_left.ycor()
    if y < 250:
        y += 20
    else:
        y = 260
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    if y > -240:
        y -= 20
    else:
        y = -250
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    if y < 250:
        y += 20
    else:
        y = 260
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    if y > -240:
        y -= 20
    else:
        y = -250
    paddle_right.sety(y)

# Association des touches avec les fonctions de mouvement des raquettes
win.listen()
win.onkeypress(paddle_left_up, "w")
win.onkeypress(paddle_left_down, "s")
win.onkeypress(paddle_right_up, "Up")
win.onkeypress(paddle_right_down, "Down")

# Boucle principale du jeu
while True:
    win.update()

    # Mouvement de la balle
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Rebond sur les limites supérieure et inférieure
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Rebond sur les raquettes et mise à jour du score
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_right.ycor() + 50 > ball.ycor() > paddle_right.ycor() - 50):
        ball.color("red")
        ball.dx *= -1.1 # augmente légèrement la vitesse de la balle à chaque rebond sur une raquette
        ball.dy *= 1.1
    elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_left.ycor() + 50 > ball.ycor() > paddle_left.ycor() - 50):
        ball.color("blue")
        ball.dx *= -1.1 # augmente légèrement la vitesse de la balle à chaque rebond sur une raquette
        ball.dy *= 1.1
    elif ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write(f"Joueur 1: {score_a}   Joueur 2: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.speed(40)
        ball.goto(0, 0)
        ball.dx = (5 / 100) * (-1)**random.randint(0, 1)
        ball.dy = (5 / 100) * (-1)**random.randint(0, 1) # divisé par 10 pour la rendre plus lente et aléatoire en direction
    elif ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write(f"Joueur 1: {score_a}   Joueur 2: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.speed(40)
        ball.goto(0, 0)
        ball.dx = (5 / 100) * (-1)**random.randint(0, 1)
        ball.dy = (5 / 100) * (-1)**random.randint(0, 1) # divisé par 10 pour la rendre plus lente et aléatoire en direction