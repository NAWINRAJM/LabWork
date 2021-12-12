#Write a Python program to sum three given integers. However, if two or more values are equal print zero
a=int(input("enter first number:  "))
b=int(input("enter second number:  "))
c=int(input("enter third number:  "))
if a==b or a==c or b==c:
    print("Zero")
else:
    print(f'The sum of three numbers are {a+b+c}')
