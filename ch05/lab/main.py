import pygame

iters = {}
n = 20
upper_limit = 10 
max_so_far = 0
num_so_far = 0
display = pygame.display.set_mode()
pygame.font.init()

def func(n):
 count = 0
 while n != 1:
   if n % 2 == 0:
     n = n / 2    
     count = count + 1
   else:
     n = 3*n+1
     count = count + 1   
 return(count)


for i in range(2, upper_limit + 1):
 iters[i] = func(i)

print(iters.items)

pygame.draw.lines(display, 'blue', False, iters)
new_display = pygame.transform.flip(display, False, True)
display.blit( new_display , (0, 0) )
font = pygame.font.Font(None, 40)
msg = font.render("what you want your max to be", True, 'blue')
display.blit(rendered_message, pos)
