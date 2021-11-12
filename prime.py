import math
num = int( input(" enter a number:"))
print (round( math.sqrt(num), 0))

if num == 2:
    print(num , " is a prime number")
else :
    if num % 2 == 0 :
        print (num , "is not a prime number ")
    else :
        isprime = True
    for i in range(3,int(round( math.sqrt(num), 0))):
        if num % i == 0 :
            print ( num , "is not a prime number ")
            isprime = False
        break
        

    if isprime == True:
            print(num , " is a prime number")
