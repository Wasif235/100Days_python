data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brazil'
    }
]

logo='''  ___ ___ .__       .__                   .____                               
 /   |   \|__| ____ |  |__   ___________  |    |    ______  _  __ ___________ 
/    ~    \  |/ ___\|  |  \_/ __ \_  __ \ |    |   /  _ \ \/ \/ // __ \_  __ \
\    Y    /  / /_/  >   Y  \  ___/|  | \/ |    |__(  <_> )     /\  ___/|  | \/
 \___|_  /|__\___  /|___|  /\___  >__|    |_______ \____/ \/\_/  \___  >__|   
       \/   /_____/      \/     \/                \/                 \/       '''
       
       
       
vs='''             
___  ________
\  \/ /  ___/
 \   /\___ \ 
  \_//____  >
          \/ 
             '''       
import random
             


def formar_data(account):   
   account_name= account["name"]
   account_description= account["description"]
   account_country= account["country"]
   return (f"{account_name}, {account_description}, {account_country}") 


def check_answer(user_guess,a_followers,b_followers):
   if a_follower_count>b_follower_count:
      return user_guess=="a"
   else:
      return user_guess=="b"
   
   
   
print(logo)

score=0

game_should_continue=True

account_b=random.choice(data)

while game_should_continue:
   

     
   account_a=account_b 
   account_b=random.choice(data)
   if account_a==account_b:
      account_b=random.choice(data)
         
   print(f"Compare A: {formar_data(account_a)}")

   print(vs)

   print(f"Compare B: {formar_data(account_b)}")  


   guess=input("Who has more score type 'a' or 'b'").lower()
   print("\n" * 50)
   a_follower_count=account_a["follower_count"]
   b_follower_count=account_b["follower_count"]

   is_correct= check_answer(guess, a_follower_count, b_follower_count)

   if is_correct:
      score+=1
      print(f"You win, {score}")
   else:
      print(f"You lose, your score is {score}")
      game_should_continue= False
      
         

      