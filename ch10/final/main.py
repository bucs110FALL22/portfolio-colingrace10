
class base:
  def __init__(self, x, y, c): 
    self.x = x
    self.y = y
    self.color = c
  def second(self):
     self.x = self.x
     self.y = self.y
     self.color = self.color
    
  def first(self):
     self.x = self.x
     self.y = self.y
     self.color = self.color
  def third(self):
     self.x = self.x
     self.y = self.y
     self.color = self.color

  def home(self):
     self.x = self.x
     self.y = self.y
     self.color = self.color

    
class hit:
   def __init__(self, d, p, b):
     self.distance = d
     self.points = p
     self.base = b
   def single(self):
     self.distance = 100
     self.points = 0
     self.base = 1
   def double(self):
     self.distance = 250
     self.points = 0
     self.base = 2
   def triple(self):
     self.distance = 300
     self.points = 0
     self.base = 3
   def homerun(self):
     self.distance = 350
     self.points = 1
     self.base = 4
   
class player:
  def __init__(self, t, s, x, y):
    self.team = t
    self.speed = s
    self.x = x
    self.y = y