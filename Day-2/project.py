
def spliter(total_amount,person):
    per_person = (total_amount/person)
    return per_person

def tip_cal(bill,tip,person):
    # if(tip != 10 or 12 or 15): return "Invalid Tip Amount"
    # else:
    total_tip_amount = (bill*tip)/100
    total_amount = bill+total_tip_amount
    return spliter(total_amount,person)
    

def bill_amt(bill,tip,person):
 if(bill < 0): return "Invalid"
 else : return tip_cal(bill,tip,person)
 
    

print(f"Welcome {input("Enter your name: ")} to the tip calculator!")
bill = int(input("What was the total bill? ₹"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
person = int(input("How many people to split the bill?"))
print(bill_amt(bill,tip,person))


# print("Each person should pay:")

