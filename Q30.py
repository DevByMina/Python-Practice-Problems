def MinMax(list):
    max=list[0]
    min=list[0]
    for num in list:
        if(num>max):
            max=num
        if(num<min):
            min=num
    print("Max number in the list is ",max)
    print("Min number in the list is ",min)

mylist=[1,5,18,29,-1,55]
MinMax(mylist)