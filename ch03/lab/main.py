import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here

#race 1
leonardo.forward(random.randrange(1,101))
michelangelo.forward(random.randrange(1,101))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
turtle.delay(500)

#race 2
n = 10
i = random.randrange(1,11)
for _ in range(n):
  leonardo.forward(i)
for _ in range(n):
 michelangelo.forward(i)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

turtle.delay(500)
# PART B - complete part B here

pygame.init()
size = width, height = 1000, 700
window = pygame.display.set_mode(size)


blue = [0,0,255]
white = [0,0,0]
window.fill(white)

coords = []
num_sides = 3
side_length = 1
offset = (100)


for i in range(num_sides):
 theta = (2.0 * math.pi * (i)) / num_sides
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 coords.insert= (x,y)
pygame.draw.polygon(window,blue,[(coords)])
print(i)


#num_sides = 4
#for i in range(numsides)

window.exitonclick()
