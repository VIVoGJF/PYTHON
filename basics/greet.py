import time
hr =int(time.strftime('%H'))
if(hr>5 and hr<12 ):
    print("Good morning")
elif(hr<17):
    print("Good afternoon")
elif(hr<20):
    print("Good evening")
else:
    print("Good night")