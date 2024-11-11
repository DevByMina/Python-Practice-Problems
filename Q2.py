import random
userNum = int(input("Enter a number: "))
rand = int(random.randrange(1,9,1))
while userNum != rand:
    userNum = int(input("Try again "))

print("Well guessed!")