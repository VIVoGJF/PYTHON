from random import *
symbols = ['🍒','🍉','🍌','🔔','🍋']

def spin():
    return [choice(symbols) for i in range(3)]

def show(rs):
    print("\nSpinning.....\n")
    print("************")
    print(" | ".join(rs))
    print("************\n")

def payout(rs,bet):
    global balance
    if rs[0]==rs[1]==rs[2]:
        if rs[0]=="🍒":
            win= bet*2
            balance+=win
            print(f"You Won ${win}")
        elif rs[0]=="🍉":
            win= bet*3
            balance+=win
            print(f"You Won ${win}")
        elif rs[0]=="🍌":
            win= bet*5
            balance+=win
            print(f"You Won ${win}")
        elif rs[0]=="🔔":
            win= bet*10
            balance+=win
            print(f"You Won ${win}")
        elif rs[0]=="🍋":
            win= bet*20
            balance+=win
            print(f"You Won ${win}")
    else:
        print("Your loose!")

balance = 100
cont=False

print("*********************")
print(" Welcome To Slot Game")
print("Symbols: ", end="")
for s in symbols:
    print(s, end = " ")
print("\n*********************")


while balance>=0:
    if balance==0:
        print(f"Current balace: {balance}\nNo more funds to continue!")
        break
    
    print(f"\n\nCurrent balance: ${balance}")
    bet = input("Enter bet amount: ")

    if bet.isdigit():
        bet = int(bet)
        if bet<0:
            print("Invalid input!")
            continue
        elif bet>balance:
            print("Insufficient balance!")
            continue
        else:
            balance -= bet

    else:
        print("Invalid input!")
        continue
    
    rs = spin()
    show(rs)
    payout(rs,bet)
    
    chs=input("\nDo you want to continue?(y): ").lower()
    if chs!= "y":
        print("\n**********************")
        print("Thank Your For Palying!")
        print(f"Final Payout: ${balance}")
        print("***********************")
        break
    