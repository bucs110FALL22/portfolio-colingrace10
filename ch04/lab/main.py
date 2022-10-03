import pygame
import pygame.math

# Colors
pink = (236,117,117)
blue = (46,135,238)
black =(0,0,0)

#screen setup


screen = pygame.display.set_mode()

width = pygame.display.get_window_size()[0]
height = pygame.display.get_window_size()[1]

surface = pygame.display.set_mode((width, height))
surface.fill(blue)
pygame.draw.circle(surface, blue, (100, 100), (100))