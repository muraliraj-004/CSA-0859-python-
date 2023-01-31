#creating a list
list=[]
print(list)

#Addition of elements in the list
list.append(1)
list.append(2)
list.append(4)
print("\nlist after Addition of Three elements:")
print(list)

list.insert(2,12)
list.pop()

#adding elements to the list using iterator
for i in range(1,4):
    list.append(i)
print(list)

#adiition of list to list
list2=['for','sample']
list.append(list2)
print(list)
