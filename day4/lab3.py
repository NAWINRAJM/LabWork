'''Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.

if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERROR".'''
a=int(input("enter your age:  "))
b=input("press m for male and f for female:  ")
if b=="f":
    print("you will work in urban area")
elif b=="m" and 20<a<40:
    print("you can work anywhere")
elif b=="m" and 40<a<60:
    print("you will work in urban areas")
else:
    print("error")
    