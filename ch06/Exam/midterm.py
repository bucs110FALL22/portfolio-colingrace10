import turtle
import time
window = turtle.Screen()
house = turtle.Turtle()


def main(x='blue'):

  turtle.speed(1)
  height = (75)
  length = (100)
  rotate = (90)
  

  turtle.speed(1)
  
  base_lines_drawn = 0
  
  house.penup()
  house.forward(length) 
  house.pendown()

  house.color(x)
  
  house.begin_fill()
  for i in range(2):
   house.right(rotate) 
   house.forward(height)
   base_lines_drawn = base_lines_drawn + 1
   house.right(rotate)
   house.forward(length)
   base_lines_drawn = base_lines_drawn + 1
  house.end_fill()
  
  roofs()
  doors()
  windows()
  time.sleep(2)
  house.reset()
  return(base_lines_drawn)
  
  

def roofs():

  roof = (135)
  roof_length = (70)
  rotate = (90)
  
  house.color('red')
  house.begin_fill()
  house.left(roof) 
  house.forward(roof_length)
  house.left(rotate) 
  house.forward(roof_length)
  house.end_fill()
  

def doors():

  height = (75)
  rotate = (90)
  roof2 = (45)
  door=(40)
  door_width=(20)
  door_length=(30)
  
  house.penup()
  house.left(roof2)
  house.forward(height)
  house.left(rotate)
  house.forward(door)
  house.left(rotate)
  house.pendown()
  

  house.color('yellow')
  house.begin_fill()

  for j in range(2):
    house.forward(door_length)
    house.right(rotate)
    house.forward(door_width)
    house.right(rotate)

def windows():    

  rotate = (90)
  window_height=(50)
  window_spot = (10)
  window_size = (15)
  turn_around=(180)
  window2_spot=(40)

  house.end_fill()
  house.penup()
  house.forward(window_height)
  house.left(rotate)
  house.forward(window_spot)
  house.pendown()

  house.color('green')
  house.begin_fill()
  for k in range(4):
    house.forward(window_size)
    house.right(rotate)

  house.penup()
  house.right(turn_around)
  house.forward(window2_spot)
  house.pendown()

  for j in range(4):
    house.forward(window_size)
    house.left(rotate)
  house.end_fill()
  
main(x='red')
lines=main()
print("Lines drawn for base of the house:",lines)

window.exitonclick()