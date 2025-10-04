MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit=0
def is_resource_sufficient(order_ingredients):
   for items in order_ingredients:
      if order_ingredients[items]>=resources[items]:
         print(f"sorry there is not enough {items}")
         return False
   return True   
         
def process_coins():
   print("Insert your coins")
   total=int(input("how many quartes:?")) * 0.25
   total+=int(input("how many dimes:?")) * 0.1
   total+=int(input("how many nickles:?")) * 0.05
   total+=int(input("how many pennies:?")) * 0.01
   return total
def is_transaction_successful(money_recieved, drink_cost):
   if money_recieved>drink_cost:
      change=round(money_recieved-drink_cost,2 )
      print(f"Here is your change: {change}")
      global profit
      profit+= drink_cost
      return True
   else:
      print( "Sorry not enough money")
      return False
def make_coffee(drink_name,other_ingredients):
   for item in other_ingredients:
      resources[item]-= other_ingredients[item]
   print(f"Here is you coffee{drink_name}")   
is_on=True
while is_on:
      choice=input("What would you like? 'espresso/ latte/ cappuccino/ off'\n")
      if choice=="off":
         is_on=False
      elif choice== "report":  
         print(f"Water={resources['water']}ml")
         print(f"Milk={resources['milk']}ml")
         print(f"Coffee={resources['coffee']}ml") 
         print(f"Money: ${profit}")
      else:
         drink=MENU[choice]
         print(drink)
         if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
               make_coffee(choice, drink["ingredients"])