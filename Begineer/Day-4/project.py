# Rock paper scissor
import random as rd
rock = '''
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
'''
scissor = '''        
                     88                                                       
                     ""                                                       
                                                                              
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  
'''

paper = '''
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88                                 
'''

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
options = [rock,paper,scissor]
bot = rd.randint(0,2)

# options[user] # user ki choice
# options[bot]# ye dikhayega bot ki choice

# print(f"You choose \n{options[user]}\nBot choose\n{options[bot]}")

if user == bot:
    print(f"You choose \n{options[user]}\nBot choose\n{options[bot]}")
    print("Its a draw!")
elif user == 0 and bot == 1:
    print(f"You choose \n{options[user]}\nBot choose\n{options[bot]}")
    print("Bot wins!")
elif user == 0 and bot == 2:
    print(f"You choose \n{options[user]}\nBot choose\n{options[bot]}")
    print("You win!")
elif user == 1 and bot == 2:
    print(f"You choose \n{options[user]}\nBot choose\n{options[bot]}")
    print("Bot wins!")
elif user == 1 and bot == 0:
    print(f"You choose \n{options[user]}\nBot choose\n{options[bot]}")
    print("You win!")
elif user == 2 and bot == 0:
    print(f"You choose \n{options[user]}\nBot choose\n{options[bot]}")
    print("Bot wins!")
elif user == 2 and bot == 1:
    print(f"You choose \n{options[user]}\nBot choose\n{options[bot]}")
    print("You win!")
else:
    print("You typed an invalid number, you lose!")
