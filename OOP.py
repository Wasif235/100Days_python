class user:
   def __init__(self,user_id, username):
      self.id=user_id
      self.username=username
      self.followers = 0
      self.following=0
   def follow(self, user):
      user.followers+=1
      self.following+=1   
      
user_1=user("23","makato")    
user_2=user("24","makati")  
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
 