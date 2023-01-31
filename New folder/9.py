#swapping
a=[]
n=int(input("enter the number of elements in a list:"))
for x in range(0,n):
    element=int(input("enter the element:"))
    a.append(element)
temp=a[0]
a[0]=a[n-2]
a[n-2]=temp
print("New list is:")
print(a)
