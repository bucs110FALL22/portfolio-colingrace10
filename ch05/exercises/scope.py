

def multi(num,var):
  result = 0
  for j in range(num):
   result = result + var 
  return result
  

def square(num):
  result = 0
  for i in range(num):
    result = result + num
  return result

def exp(num, var):
  result = 1
  for i in range(var):
    result = result * num
  return result

def main():
  res = square(2)
  print(res)
  res = multi(2,4)
main()