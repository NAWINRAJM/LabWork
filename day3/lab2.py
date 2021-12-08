#2. WAP which accepts marks of four subjects and display total marks, percentage and grade
# . Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
a=float(input("Enter the marks for first subject: "))
b=float(input("Enter the marks for second subject : "))
c=float(input("Enter the marks for third subject:   "))
e=a+b+c
print("The total marks : ",e )
d=(e/300)*100
print("The percentage is: ",d)
if d>70:
    print("Distiction")
if d>60:
    print("first")
if d>40:
    print("pass")
else:
    print("fail")

      
