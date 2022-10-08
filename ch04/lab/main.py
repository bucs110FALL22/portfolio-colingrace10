import pygame
import math
import random
import time
# Colors
pink = (236,117,117)
blue = (46,135,238)
black =(0,0,0)
green= (99,250,11)
white = (255,255,255)
red = (255,0,0)
blue1 = (0,0,255)
green1 = (43,152,15)
yellow = (247,255,0)
  
#screen setup part A
pygame.init()
surface = pygame.display.set_mode((300, 300))
width = pygame.display.get_window_size()[0]
height = pygame.display.get_window_size()[1]
surface = pygame.display.set_mode((width, height))
surface.fill(blue)
pygame.draw.circle(surface, pink, (width/2, height/2), (width/2))
pygame.draw.line(surface, black, (width/2, 0),(width/2, height))
pygame.draw.line(surface, black, (0, height/2),(width, height/2))
#part B
for i in range(10):
 x = random.randrange(0, width)
 y = random.randrange(0, height)
 
 distance_from_center = math.hypot(x-height/2, y-width/2)
 is_in_circle = distance_from_center <= width/2
 if is_in_circle: 
   pygame.draw.circle(surface, green, (x, y), (5))
   pygame.display.flip()
 else:
   pygame.draw.circle(surface, black, (x, y), (5))
   pygame.display.flip()
  
pygame.time.wait(1000)
pygame.display.flip()
pygame.display.update()
surface.fill("blue")
#Part C
surface.fill("green1")
pygame.display.update()

pygame.display.update()

surface.fill(green1)
pygame.draw.circle(surface, white, (width/2, height/2), (width/2))
pygame.draw.line(surface, black, (width/2, 0),(width/2, height))
pygame.draw.line(surface, black, (0, height/2),(width, height/2))

red_score = 0
blue_score = 0

print("Red score", red_score)
print("Blue score", blue_score)

for i in range(10):
 x = random.randrange(0, width)
 y = random.randrange(0, height)
 distance_from_center = math.hypot(x-height/2, y-width/2)
 is_in_circle = distance_from_center <= width/2

 if is_in_circle: 
   pygame.draw.circle(surface, red, (x, y), (5))
   red_score = red_score + 1 
   print("Red player hit!")
   print("Red score:", red_score)
   pygame.display.flip()
   time.sleep(2)
 else:
   pygame.draw.circle(surface, black, (x, y), (5))
   print("Red player miss")
   print("Red score:", red_score)
   pygame.display.flip()
   time.sleep(2)

 x = random.randrange(0, width)
 y = random.randrange(0, height)
 distance_from_center = math.hypot(x-height/2, y-width/2)
 is_in_circle = distance_from_center <= width/2

 if is_in_circle: 

   pygame.draw.circle(surface, blue, (x, y), (5))
   pygame.draw.circle(surface, blue1, (x, y), (5))
   blue_score = blue_score + 1 
   print("Blue player hit!")
   print("Blue score", blue_score)
   pygame.display.flip()
   time.sleep(2)
 else:
   pygame.draw.circle(surface, yellow, (x, y), (5))
   print("Blue player miss")
   print("Blue score", blue_score)
   pygame.display.flip()
   time.sleep(2)

 if red_score > blue_score:
     print("Red Player Wins!!!")
 elif blue_score > red_score:
     print("Blue Player Wins!!!")
 else:
     print("Its a tie!!")


pygame.display.update()
pygame.time.wait(1000)