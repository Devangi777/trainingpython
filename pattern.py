n=int(input("Enter the number of rows "))
c=1
a=1
for i in range(n,0, -1):
    for j in range(i,0,-1):
        print(" ",end='')
    for k in range(0,c):
        print("*",end='')
    if(c>1):
        for l in range(0,a):
            print("*",end='')
        a=a+1
    c=c+1
    print()


