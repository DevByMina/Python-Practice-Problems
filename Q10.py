sum=0
count=0
flag=0
while(not(flag)):
    num=int(input("enter a number(enter zero to terminate) : "))
    if(num==0):
        print("Sum is ",sum)
        print("average is ",sum/count)
        flag=1
    else:
        count+=1
        sum=sum+num