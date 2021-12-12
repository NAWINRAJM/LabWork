'''A student will not be allowed to sit in exam if his/her attendence is less than 75%.

Take following input from user

Number of classes held

Number of classes attended.

And print

percentage of class attended

Is student is allowed to sit in exam or not'''
a=int(input("Enter the number classes held:  "))
b=int(input("Enter the number classes you attended:  "))
c=b/a
d=c*100
if d>75:
    print(f"Your atendance percentage is {d}%   so you can attend exam ")
else:
    print(f"your attendace perentage is {d}%  so you cannot attend the exam ")