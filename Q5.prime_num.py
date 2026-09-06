number= int (input("enter a number :"))
if number <= 1:
    print(number, "is not a prime number")
else:

    for i in range(2, int(number ** 0.5) + 1): 
        if number % i == 0  :
            print(number,"is not a prime number")
            break

    else :
        print(number,"is a prime nummber")