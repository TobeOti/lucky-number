#LUCKY NUMBER

import random
name = input("What is your name, traveller: ")
lucky_number = int(input("Pick a number between 1 and 100: "))

number_pool = random.randint(1, 100)

for i in range(3):
    if lucky_number == number_pool:
        print(f"Congratulations {name}, you've won!!")
    else:
        print("Better luck next time.")
