
print("Welcome to the tip calculator.")
print("What was the total bill?")
total = input()
print("What percentage tip would you like to give? 10, 12, or 15?")
tip = input()
print("How many people to split the bill?")
people_split = input()
calculation = (float(total)/float(people_split)*((100+float(tip))/100.00))
calculation_round = round(calculation, 2)
calculation_final = "{:.2f}".format(calculation_round)
print(f"Each person should pay: {calculation_final}")
