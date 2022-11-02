import turtle

def main():
  window = turtle.Screen()
  
  length = (50)
  height = (100)
  rotate = (90)
  roof = (45)

  house = turtle.Turtle()
  house.penup()
  house.forward(length) 
  house.pendown()


  for i in range(2):
   house.right(rotate) 
   house.forward(height)
   house.forward(length)

main()