#convert 86400 seconds to day,hour,minutes and seconds
sec=int(input("enter seconds"))
day=sec//(60*60*2)
HRS=sec/(60*60)
min=sec/60
print(f"86400 seconds equal to{day} day and {HRS} hours and {min} minutes")

