from random import *
option = ("rock","paper","scissor")
cchs = choice(option)
score = 0
print(f"{"Player":10}|{"Computer":-10}")
while True:
    pchs = input("Enter choice(rock, paper,scissors):").lower()
    cchs = choice(option)
    print(f"{"Player":10}|{"Computer":10}")
    if pchs == cchs:
        score += 1
        print(f"You win! score: {score}")