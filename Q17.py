num = int(input("please enter a number to calculate its factorial: "))
factorial = 1
if(num==0 or num==1):
    factorial=1
else:
    for i in range(num,1,-1):
        factorial *= i

print("factorial of ",num," equals",factorial)