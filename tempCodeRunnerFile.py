from random import *

symbols = ['🍒','🍉','🍌','🔔','🍋']

def spin():
    return [choice(symbols) for i in range(3)]

def show(rs):
    print("*********************")
    for s in rs:
        print(s, sep = "|")
    print("\n*********************")

def payout():
    pass

balance = 100
exit="n"

print("*********************")
print(" Welcome To Slot Game")
print("Symbols: ", end="")
for s in symbols:
    print(s, end = " ")
print("\n*********************")


while exit == "n" :
    print(f"\n\nCurrent balance: ${balance}")
    bet = input("Enter bet amount: ")

    if bet.isdigit():
        bet = int(bet)
        if bet<0:
            print("Invalid input!")
        elif bet>balance:
            print("Insufficient balance!")
        else:
            balance -= bet

    else:
        print("Invalid input!")
    
    rs = spin()
    show(rs)