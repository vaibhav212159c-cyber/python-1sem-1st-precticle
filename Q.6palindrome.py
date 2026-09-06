charector = int(input("enter a number :"))

original = charector
reverse=0

while charector > 0:
    digit = charector % 10 
    reverse = reverse*10+ digit 
    charector = charector //10

if reverse == original :
    print("yes it is palindrome")
else:
    print("no it's not a palindrome")


