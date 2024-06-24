print("Welcome to the tip calculator.")
total_bill_input = input("What was the total bill?")
people_number_input = input("How many people to split the bill?")
tip_percentual_input = input("What percentage tip would you like to give? 10, 12 or 15?")

total_bill = float(total_bill_input)
people_number = int(people_number_input)
tip_percentual = int(tip_percentual_input)

total_bill_tip = total_bill * (1 + (tip_percentual/100))
amount_per_person = total_bill_tip/people_number

print("Each person should pay: " + str(round(amount_per_person, 2)))