from turtle import *
import turtle
import random

speed(speed='fastest')

def draw(n, x, angle):
    # loop para numero de estrelas
    for i in range(n):

        colormode(255)

        # Escolher int randon
        #  0 - 255
        # tpara gerar RGB
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)

        # linha de contorno
        # e preenchimento
        pencolor(0, 0, 0)
        fillcolor(a, b, c)
        # começa a pintar as estrelas
        begin_fill()
        # loop para cada estrela
        for j in range(20):
            turtle.circle(20 * j)
            turtle.left(7)

        # completar preenchimento
        end_fill()

        # rotação na nova estrela
        
        rt(angle)

# parametros
n = 30  # numero de estrelas
x = 144  # angulo exterior de cada estrela
angle = 60  # angulo de rotação 

draw(n, x, angle)
