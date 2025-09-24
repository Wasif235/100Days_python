print("Welcome to the tip calculator!")
bill=float(input("What is the total bill?\n$"))
tip=int(input("How much tip would you like to give? 10, 12 or 15\n"))
number_of_split=int(input("How many people to split the bill?\n"))
calculation=((bill)*(tip)/100)/number_of_split
print(f"Each person should pay: &{calculation}")