num= int(input("please enter a number :"))
sum=0
while(num!=0):
    sum= sum + (num%10)
    num= int(num/10)
print("sum of the digits of your number is ",sum)