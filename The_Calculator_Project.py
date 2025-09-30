def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div
}

def calculator():
    first_number = float(input("Enter first number: "))

    continue_cal = True
    while continue_cal:
        sign = input("Choose your sign '+', '-', '*', '/': ")
        next_number = float(input("Enter next number: "))

        calculated_value = operation[sign](first_number, next_number)
        print(f"Result: {first_number} {sign} {next_number} = {calculated_value}")

        user = input('Do you want to continue with this result? (y/n): ')
        if user.lower() == "n":
            print("\n"*20)
            continue_cal = False
        else:
            first_number = calculated_value   # update for next round

calculator()
