def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if(b==0):
        return "cant divide by zero"
    else:
        return a/b
n=float(input("Enter first number"))
o=input("Enter the operator")
m=float(input("Enter second number"))
if(o=='+'):
   print(add(n,m))
elif(o=='-'):
   print(sub(n,m))
elif(o=='*'):
   print(mul(n,m))
elif(o=='/'):
   print(div(n,m))
else:
   print('not a valid operator')
