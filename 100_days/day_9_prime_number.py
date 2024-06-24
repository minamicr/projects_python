def prime_checker(number: int):
    prime_number = True
    for x in range(1, number):
        if x != 1 and x != number and number % x == 0:
            prime_number = False
            break

    if prime_number:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
