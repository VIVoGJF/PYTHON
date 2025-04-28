def fibo(num):
    if(num<=1):
        return num
    else:
        return (fibo(num-1)+fibo(num-2))
    
num=int(input("Enter num: "))
if(num<=0):
    print("invalid input")
else:
    print("the first",num,"numbers of fibonacci serise are:")
    for i in range(num):
        print(fibo(i), end=" ")
