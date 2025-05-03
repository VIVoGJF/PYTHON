from random import *
option = ("rock","paper","scissor")
cchs = choice(option)
score = 0

while True:
    
    pchs=None
    while pchs not in option:
        pchs = input("Enter choice(rock, paper,scissors):").lower()
    
    cchs = choice(option)
    print(f"Player: {pchs}")
    print(f"Computer: {cchs}")
    
    if pchs == cchs:
        print(f"Its a tie! Score= {score}")
    elif pchs == "rock" and cchs == "scissor":
        score+=1
        print(f"You win! Score= {score}")
    elif pchs == "paper" and cchs == "rock":
        score+=1
        print(f"You win! Score= {score}")
    elif pchs == "scissor" and cchs == "paper":
        score+=1
        print(f"You win! Score= {score}")
    else:
        print(f"You loose!\nFinal score: {score}")
        break
    