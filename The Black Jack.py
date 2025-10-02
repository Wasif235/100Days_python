import random
def deal_card():
   cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
   card=random.choice(cards)
   return card

def calculate_score(cards):
   
   if sum(cards)==21 and len(cards)==2:
      return 0
   if sum(cards)>21 and 11 in cards:
      cards.remove(11)
      cards.append(1)
   return sum(cards)
def compare(computer_score, user_score):
   if computer_score==user_score:
      return "Draw"
   elif computer_score==0 or computer_score==21:
      return "You lose"
   elif computer_score>21:
      return "Computer lose"
   else:
      print("You win")

user_card=[]
computer_card=[]
user_score=-1
computer_score=-1
is_game_over= False

for _ in range(2):
   user_card.append(deal_card())
   computer_card.append(deal_card())

   
while not is_game_over:
   
   user_score=calculate_score(user_card)

   computer_score=calculate_score(computer_card)   

   print(f"your card: {user_card}, card score: {user_score}")  

   print(f"computer_card: {computer_card[0]}") 

   if user_score==0 or computer_score==0 or user_score>21:
      is_game_over= True
   else:
      user_should_deal=input("Type 'y' for get another card, type 'n' to pass:'")
      if user_should_deal=="y":
         user_card.append(deal_card())
      else:
         is_game_over=True
      
while computer_score!= 0 and computer_score < 17:
   computer_card.append(deal_card())
   computer_score=calculate_score(computer_card)
   
compare(computer_score,user_score)      

   
   
   
   