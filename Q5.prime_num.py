number= int (input("enter a number"))
for i in range (2,number):
    if number % i == 0  :
        print("not a prime number")
        break

else :
    print(number,"is a prime nummber")