name = input("Please, enter your name:")
salesAmount = input("Please, enter your total amount of sales for this month:")
comission = round(float(salesAmount) * (13/100), 2)
print(f"{name} your comission is {comission}")
