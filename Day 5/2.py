def salarycalculation(grade,salary):
    if(salary>10000):
        if(grade=='A'):
            salary=salary+(salary/5)
            print(salary)
        elif(grade=='B'):
            salary=salary+(salary/10)
            print(salary)
    else:
        if(grade=='A'):
            salary=salary+(salary/7)
            print(salary)
        elif(grade=='B'):
            salary=salary+(salary/12)
            print(salary)

grade=input("Enter the grade of your employee like 'A' or 'B' :- ")
salary=int(input("Enter your employee salary:-"))
salarycalculation(grade,salary)
