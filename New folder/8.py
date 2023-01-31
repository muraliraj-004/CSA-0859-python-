#sum of list with recursion
def sum_arr(arr,size):
    if(size==0):
        return 0
    else:
        return arr[size-1] + sum_arr(arr,size-1)
n=int(input("enter the number of elements for list:"))
a=[]
for i in range(0,n):
    element=int(input("enter element:"))
    a.append(element)
print("The list is:")
print(a)
print("sum of items in a list:")
b=sum_arr(a,n)
print(b)
    
