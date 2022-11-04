import Rectangle

class Surface:
  # creates the rectangles coordinates and measurements 
  def __init__(self, filename, x, y, h, w):
   self.rect = Rectangle.rectangle(x, y, h, w)
   self.image = filename
   #creates and returns the rectangle with corrdiantes
  def getRect(self):
    return self.rect
