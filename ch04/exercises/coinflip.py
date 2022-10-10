import turtle 
import random


window = turtle.Screen() 

colin = turtle.Turtle()
#blue = [0,0,255]
white = [0,0,0]
colin.color('blue')
colin.speed(0)
window.bgcolor(white)
distance = 10
angle = 90
is_in_screen = True

while is_in_screen:
 coin = random.randrange(0, 2)
 if coin == 0:
  colin.left(angle)
 else: 
  colin.right(angle)
 colin.forward(distance)

 turtlex = colin.xcor
 turtley = colin.ycor

 xrange = window.window_width()/2
 yrange = window.window_height()/2

 if abs(turtlex) > xrange or abs(turtley) > yrange:
   is_in_screen = False