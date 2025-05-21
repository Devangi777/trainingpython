def prime(n):
  c=0
  for i in range(1,n+1):
    if(n%i==0):
      c=c+1
    else:
      continue
  if(c==2):
   return True
  else:
   return False
n=int(input("Enter a number "))
print(prime(n))