from datetime import datetime #modules``

now = datetime.now()
current_time = int(now.strftime("%H"))

if(current_time < 12):
    greet = "Morning"
elif(current_time<16):
    greet = "Afternoon"
elif(current_time<20):
    greet = "Evening"
else:
    greet = "Night"

name = input("What's ur name? ")
# print(current_time)
print(f"Good {greet} {name}!!")

print(len(name)) #length of the string