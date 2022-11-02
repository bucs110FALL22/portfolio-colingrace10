class Rectangle:
 def __init__(self, x=0, y=0, h=0, w=0):
  self.x = x
  self.y = y
  self.width = w
  self.height = h
  
  def __str__(self):
   values = f"(x:{self.x},y{self.y}) Height:{self.h}, Width:{self.w}"

   return(values)