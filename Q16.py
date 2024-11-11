list1 = [1,4,5,6,7]
list2 = [3,5,7,9,9]

print("Common elements is: ",end="")
for num1 in list1:
    for num2 in list2:
        if(num1==num2):
            print(num1, " ", end="")