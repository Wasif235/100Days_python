import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
          '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',
          '_', '`', '{', '|', '}', '~']

print("Welcome to the pypassword generator!")
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbol=int(input("How many symbols would you like?\n"))
nr_numbers=int(input("How many numbers would you like?\n"))
temp=""
for i in range(1,nr_letters+1):
   random_char=random.choice(letters)
   temp+=random_char
for i in range(1,nr_symbol+1):
   random_char=random.choice(symbol)
   temp+=random_char
for i in range(1,nr_numbers+1):
   random_char=random.choice(number)
   temp+=random_char
print(temp)
### Hard Part ###=============================================
pass_list=[]
for i in range(0,nr_letters):
   pass_list.append(random.choice(letters))
for i in range(1,nr_symbol+1):
   pass_list.append(random.choice(symbol))
for i in range(1,nr_numbers+1):
   pass_list.append(random.choice(number))  
print(str(pass_list))
random.shuffle(pass_list) 
passs=''
for char in pass_list:
   passs+=char
print(passs)           