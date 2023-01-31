string="I am Murali Raj"
words=string.split()
list1=list(words)
list2=[]
for i in list1[: : -1]:
    list2.append(i)
print(list2)
print("Converting to string")
strcov=" "
for x in list2:
    strcov+=' ' +x
print(strcov)
