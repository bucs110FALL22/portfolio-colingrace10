class StringUtility:

  def __init__(self, string):
    self.string = string

  def __str__(self):
    
    return self.string
    

  def vowels(self):
    vowel = set("aeiouAEIOU")
    result = 0

    for s in self.string:
      if s in vowel:
       result = result + 1 
    if result == 4:
      return "4"
    if result == 0:
      return "0"
    if result == 1:
      return "1"
    if result == 2:
      return "4"
    if result == 3:
      return "3"
    if result > 4:
      return "many"

  def bothEnds(self):
    for j in range(len(self.string)):
      if len(self.string) > 2:
        return (self.string[j+0])+(self.string[j+1])+(self.string[j-2])+(self.string[j-1])
      if len(self.string) <= 2:
        return ""

  def fixStart(self):
     for i in self.string:
       if self.string[0] in self.string:
         return self.string.replace(self.string[0], "*" )

         
  def asciiSum(self):
    sum = 0
    for add in self.string:
      sum += ord(add)
    return sum

  def cipher(self):
     for l in (len(self.string)):
       self.string
      
     
      

