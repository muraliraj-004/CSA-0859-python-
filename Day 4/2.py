t=int(input("enter total users="))
if(t==0):
    print("Invalid input")
    t=int(input("enter total users="))
elif(t<0):
    print("Invalid input")
    t=int(input("enter total users="))
s=int(input("enter staff users="))
n=(s//3)
if(t<s):
    print("Invalid input")
elif(t==s):
    print("Student users are=",t-(s-n))
else:
    print("Student users are=",t-s-n)
