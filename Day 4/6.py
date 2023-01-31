def delchar(a,b):
    if len(b)!=1:
        return a
    else:
        return a.replace(b,"")
a="good evening"
print(a)
b=input("enter the character to be removed:")
print(delchar(a,b))

a="take care"
print(a)
b=input("enter the character to be removed:")
print(delchar(a,b))

a="123456s"
print(a)
b=input("enter the character to be removed:")
print(delchar(a,b))

a="red rose"
print(a)
b=input("enter the character to be removed:")
print(delchar(a,b))

a="flower"
print(a)
b=input("enter the character to be removed:")
print(delchar(a,b))
