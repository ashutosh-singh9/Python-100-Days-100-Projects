print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
path = input("Type \"left\" or \"right\"\n").lower()
if(path == "left"):
    print("You've come to a lake. There is an island in the middle of the lake.")
    swim = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if(swim == "wait"):
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door = input("One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if door == "red":
            print("Burned by fire.\nGame Over.")
        elif door == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif door == "yellow":
            print("You Win!!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
        
else:
    print("Fall into a hole.\nGame Over!!")