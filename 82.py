from selectors import SelectSelector

user_name = input("name? ")
mood = input("payment method? (card/cash): ")
if mood == "card":
    print("processing...")
elif mood == "cash":
    print("cash accepted")
else :
    print("payment method not recognised")