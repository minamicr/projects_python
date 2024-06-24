year = int(input("Which year do you want to check? "))

div_by_four = (year % 4) == 0
div_by_hundred = (year % 100) == 0
div_by_four_hundred = (year % 400) == 0

if div_by_four and not div_by_hundred:
    print("Leap year.")
elif div_by_four and div_by_hundred and div_by_four_hundred:
    print("Leap year.")
else:
    print("Not leap year.")
