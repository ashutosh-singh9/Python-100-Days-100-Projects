def encrypt(value,shift):
    ency = " "
    
    for i in range(len(value)):
        original = letters.index(value[i])
        # print(letters[original])
        ency_val = original+shift  
        if ency_val > len(letters):
            ency_val = ency_val - len(letters)
        ency += letters[ency_val]
    print(ency)

def decrypt( value,shift):
    decy = " "
    
    for i in range(len(value)):
        original = letters.index(value[i])
        # print(letters[original])
        decy_val = original-shift  
        if decy_val <=0 :
            decy_val = 26 + decy_val
        decy += letters[decy_val]
    print(decy)




letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z']
value = input("Enter the Message!!: ")
shift = int(input("Enter the shift amount"))
decrypt(value,shift)

