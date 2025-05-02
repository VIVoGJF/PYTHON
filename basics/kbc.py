ques=[
    ["The film 2012 was inspired by which of the following calender","Your wife's period calender","Board exam calander","Mayan calender","Mongoliya calander",3],
    ["In which year did India won the 2011 world cup","1999","2011","1982","2009",2],
    ["Are you gay","Fuck around and find out","yes","probably","i wish i was",1],
    ["Are you gay","Fuck around and find out","yes","probably","i wish i was",4],
    ["Are you gay","Fuck around and find out","yes","probably","i wish i was",2]
]
level=[1000,2000,3000,4000,1000000]
money=0
for i in range(0, len(ques)):
    q=ques[i]
    print(f"\n\nQuestion for Rs. {level[i]}:")
    print(f"{q[0]}\n")
    print(f"1. {q[1]}          2. {q[2]} ")
    print(f"3. {q[3]}          4. {q[4]} ")
    reply = int(input("Enter your answer (1-4):\n" ))
    if(reply== q[-1]):
        print(f"Correct, you won Rs.{level[i]}")
        if(i == 2):
            money = 3000
        elif(i == 4):
            money = 1000000
    else:
        print("Wrong answer!")
        break
print(f"You got a total of Rs. {money}")