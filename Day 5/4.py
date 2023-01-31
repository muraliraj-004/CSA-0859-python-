num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
sum=0
Product=0
print("The common divisors of number",num1,"And",num2,"are-")
for i in range(1,min(num1,num2)+1):
    if num1%i==num2%i==0:
        sum=num1+num2
        product=num1*num2

if(product%sum==0):
    print("YEAH")
else:
    print("NAH")

        
        
