l=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    e=int(input("enter the element:"))
    l.append(e)
print("The original list is:",l)
s=0
for i in l:
    s=s+i
print("The sum of all integers present in:",l,"is",s)
