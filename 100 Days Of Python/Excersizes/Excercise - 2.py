# In this excerise, we are gonna make python greet us using if/elif/else statements!

import time 

print("Hello! What is your name?! ^_^")
name = input("Enter your name: ")

timestamp = (time.strftime('%H:%M:%S'))
print("Your time now is:", timestamp)

timestamp = int(time.strftime('%H'))

if (timestamp <= 3):
    print("Good Night", name,"! ^_^")
elif (timestamp <= 12):
    print("Good Morning", name,"! ^_^")
elif (timestamp <= 17):
    print("Good Afternoon", name,"! ^_^")
elif (timestamp <= 21):
    print("Good Evening", name,"! ^_^")
else:
    print("Good Night", name,"! ^_^")

# https://docs.python.org/3/library/time.html#time.strftime