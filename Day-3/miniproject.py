bill = 0

def add_cheese(cheese):
    if(cheese == "Y"):
        bill += 1
    else:
        bill += 0
    

def add_pepperoni(pepperoni):
    
    if(pepperoni=="Y"):
        bill += 2
    else: 
        bill += 0
        
    return 0

def add_size(size):
    if size == "S":
        bill += 15
        return bill
    elif size == "M":
        bill += 20
        return bill   
    elif size == "L":
        bill += 25
        return bill
    else:
        return "Invalid Size"

print("Welcome to Python Pizza Deliveries!!")
size = input("What size pizza do you want? S , M or L: ")
pepperoni = input("Do you want pepperoni on your pizza Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")

add_size(size)
add_pepperoni(pepperoni)
add_cheese(cheese)