num1 = int (input("enter 1st number :"))
num2 = int (input("enter 2st number :"))
num3 = int (input("enter 3rd number :"))
numbers = [num1,num2,num3]
greatest = numbers[0]
for i in numbers :
    if i > greatest:
        greatest = i 

print("greatest number is ", greatest)