import turtle
import time 

def drawEqShape(myturtle, sidelength=0, numsides=0):
 
 if myturtle:
   for i in range(numsides):
     myturtle.forward(sidelength)
     myturtle.left(360/numsides)
     
leo = turtle.Turtle()     
numsides = int(input("Sides:"))
sidelength = int(input("Length:"))
drawEqShape(leo, sidelength, numsides)

time.sleep(2)