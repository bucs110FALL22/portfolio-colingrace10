import random

number = random.randrange(1, 11)

for i in range(3):
 guess_num = int(input("Pick a number:"))
 if guess_num > number:
   print("too high")
 elif guess_num < number:
   print("too low")
 else:
   print("correct")
   break 