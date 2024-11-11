numbers= (1, 2, 3, 4, 5, 6, 7, 8, 9)

evenNumCount =0
oddNumCount =0

for num in numbers:
    if(num%2==0):
        evenNumCount +=1
    else:
        oddNumCount +=1

print("Number of even numbers :",evenNumCount)
print("Number of odd numbers :",oddNumCount)