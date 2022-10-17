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
