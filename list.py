def find(l):
    li=list(set(l))
    length=len(li)
    if(length<2):
        return "Not a valid list"
    else: 
        li.sort()
        return li[length-2]
n=int(input("Enter the number of list elements: "))
p=[]
for i in range (0,n):
    num=int(input(f"Enter element {i+1}: "))
    p.append(num)
print(p)
print("second largest element: ",end='')
print(find(p))
    