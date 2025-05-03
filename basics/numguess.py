from random import *

low = 1
high = 100
num = randint(low,high)
guess = 0

print("*******Guess The Number*******")
print(f"\nGuess a number betwwwn {low} and {high}\n")

while True:
    guess = input("Enter a number: ")
    if guess.isdigit():
        guess= int(guess)
        if guess in range(low,high):
            if guess==num:
                print(f"Yes! the number is {guess}")
                break
            elif guess>num:
                print("Too high! guess a lower number.")
            else:
                print("Too low! guess a higher number.")
        else:
            print(f"Input not in range! Enter a number within {low} and {high}")
    else:
        print(f"Invalid input! Enter a number")

print("\n*******Thankyou For Playing*******")