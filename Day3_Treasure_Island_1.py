asci_view='''   __________.
  /_/-----/_/|   __
  ( ( ' ' ( (| /'--'\
  (_( ' ' (_(|/.    .\
  / /=====/ /|  '||'
 /_//____/_/ |   ||
(o|:.....|o) |   ||
|_|:_____|_|/'  _||_
 '        '    /____\
'''
print(asci_view)
print("Welcome to treasure Island\nYour mission is to find the treasure")
f1_choice=input("choose 'left' or 'right'\n" )
if f1_choice=="left":
   print("keep going")
   f2_choice= input("choose 'swim' or 'wait'\n")
   if f2_choice=="wait":
      print("keep going")
      f3_choice=input("Choose 'red' or 'yellow' or 'blue'\n")
      if f3_choice=="yellow":
         print("You win")
      else:
         print("game over")   
         
   else:
      print("Game over")   
   
else:
   print('Game Over')