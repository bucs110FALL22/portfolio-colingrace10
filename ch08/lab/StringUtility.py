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
    if len(self.string) <= 2:
        return ''
    for j in range(len(self.string)):
      if len(self.string) > 2:
        return (self.string[j+0])+(self.string[j+1])+(self.string[j-2])+(self.string[j-1])
      

  def fixStart(self):
    if len(self.string) <= 1:
      return ""
    counter = 0
    new = ""
    first=self.string[0]
    for i in range(len(self.string)):
      if first == self.string[i] and counter != 0:
        new += "*"
      else:
        counter = 1 
        new += str(self.string[i])
    return new 
            
  def asciiSum(self):
    sum = 0
    for add in self.string:
      sum += ord(add)
    return sum

  def cipher(self):
    def cipher(self):
        upper = 65
        lower = 97
        alpha = 26
        list = ""
        for j in self.s:
            if j == "":
                list = list+j
            elif j.isupper():
                list = list+chr((ord(j)+len(self.s)-upper)%alpha+upper)
            else:
                list = list+chr((ord(j)+len(self.s)-lower)%alpha+lower)
        return list

      

    
     
      

