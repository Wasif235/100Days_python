rock='''

                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a

'''
paper='''

8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88                                

'''
scissor='''
                                                                      
 ad88888ba             88                                             
d8"     "8b            ""                                             
Y8,                                                                   
`Y8aaaaa,    ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba,  
  `"""""8b, a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8  
        `8b 8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          
Y8a     a8P "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88          
 "Y88888P"   `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88     
'''
game_images=[rock, paper, scissor]
import random

choice=int(input("what do you choose? Type o for rock, 1 for paper or 2 for scissor.\n"))
computer_choice=random.randint(0,2)
if choice==0 and computer_choice==2:
  print(computer_choice)
  print(f"computer chose computer wins!")
elif choice<computer_choice:
  print(f"You lose")
elif choice==computer_choice:
  print(f"You lose")  
else:
  print("")
