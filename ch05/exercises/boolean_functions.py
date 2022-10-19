def percentage_to_letter(score=0):
 score = float(input("Grade: "))
 if score >= 90: 
  return"A"
 elif score >= 80 and score < 90:
  return"B" 
 elif score >= 70 and score < 80:
  return"C"
 elif score >= 60 and score < 70:
  return"D"
 else: 
  return"F"

grade = percentage_to_letter()
print(grade)
def passing_grade():
 letter = ("A","B","C","D","F")
 if letter in ("ABC"):
   return(True)
 else: 
   return(False)

pas = passing_grade()
print = (pas)

for j in range(2, upper_limit + 1):
 iters[i] = func(i)
 if max_value_so_far < max_value:
  max_value = func(i)
  max_value_so_far = i

 iters2[max_value] = max_value_so_far
 coords =(max_value, max_value_so_far)
 coords = [iters.items()]
 new_display = pygame.Surface(display.get_size())
 pygame.draw.lines(new_display, green, False, coords)
 new_display = pygame.transform.flip(new_display, False, 
 True)
 display.blit(new_display, (0, 0))
 pygame.display.update()
 font = pygame.font.Font(None, 20)
 msg = font.render("max value", False, white)
 display.blit(msg, (0, 0))
 pygame.display.update()
 pygame.time.wait(1000)