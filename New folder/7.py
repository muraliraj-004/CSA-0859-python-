#spliting the list
a=[]
n=int(input("enter number of elements:"))
for i in range(1,n+1):
    b=int(input("enter element:"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)
