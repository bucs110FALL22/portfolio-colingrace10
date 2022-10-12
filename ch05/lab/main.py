
#n= list(range(0, 101))
even = list(range(2,101 , 2))
#odd = list(range(1,101 , 2))
n = range(1,101)


#part A

n = 101

while n < 101:
 if n % 2 == 0:
  n = n / 2
  print(n)
 elif n == 1:
   break
 else:
  n = 3*n+1
  print(n)
#part B 24