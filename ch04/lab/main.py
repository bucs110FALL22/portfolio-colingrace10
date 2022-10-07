import pygame
import math
import random

# Colors
pink = (236,117,117)
blue = (46,135,238)
black =(0,0,0)
green= (99,250,11)
white = (0,0,0)
red = (255,0,0)
blue1 = (0,0,255)

#screen setup part A

pygame.init()
surface = pygame.display.set_mode()

width = pygame.display.get_window_size()[0]
height = pygame.display.get_window_size()[1]

print(width)
print(height)
surface = pygame.display.set_mode((width, height))
surface.fill(blue)
pygame.draw.circle(surface, pink, (293, 130), (125))
pygame.draw.line(surface, black, (0, 130),(6000, 130) )
pygame.draw.line(surface, black, (293, 0),(293, 1000) )
pygame.display.update()

#part B


x = random.randrange(0, width)
y = random.randrange(0, height)
 
distance_from_center = math.hypot(x-293, y-130)
is_in_circle = distance_from_center <= 293/2

throws = 0
while throws <= 10:
 throws = throws + 1
 if is_in_circle: 
   pygame.draw.circle(surface, green, (x, y), (5))
   pygame.display.flip()
 else:
   pygame.draw.circle(surface, black, (x, y), (5))
   pygame.display.flip()
  

print(throws)
pygame.time.wait(1000)

pygame.display.flip()

pygame.display.update()

surface.fill("blue")

#Part C

surface.fill("white")

pygame.display.update()


pygame.draw.rect(surface, red, (60,60,130,130))
pygame.display.flip()

pygame.draw.rect(surface, blue1, (200,60,130,130))
pygame.display.flip()

player1 = ("Select a color using your mouse:")

