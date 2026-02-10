# tells u the reamaing week
def life_in_weeeks(age):
    remaining_week = (90-age)*52
    return remaining_week

age = int(input("Enter Your Age: "))
print(life_in_weeeks(age))