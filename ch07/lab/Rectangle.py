class Rectangle:
  # Creates xy coordinates for rectangle as well as height and width 
  def __init__(self, x=0, y=0, h=0, w=0):
  
    if x < 0:
     x = 0
    if y < 0:
     y = 0
    if h < 0:
     h = 0
    if w < 0:
     w = 0
    self.x = x
    self.y = y
    self.height = h
    self.width = w
  
   
  # returns a string that combines the x and y coordinates as well as highlights the height and width for the rectangle
  def __str__(self):
   return f"(x:{self.x},y{self.y}) Height:{self.height}, Width:{self.width}"