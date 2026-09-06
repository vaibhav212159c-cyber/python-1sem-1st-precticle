a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

add = a + b
sub = a - b
mul = a * b

print("Addition =", add,
      "\nSubtraction =", sub,
      "\nMultiplication =", mul)
if b!=0:
    print("divition =",a/b)
else :
    print("can't divide by 0 ")