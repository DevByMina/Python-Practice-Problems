balance=20000
print("Your available balance is : ",balance)
withdraw = int(input("please enter the amount you want to withdraw  : "))
withdrawSuccess=0
while(not(withdrawSuccess)):
    if(withdraw <=balance):
        balance=balance-withdraw
        print("Successful withdraw, you new balance is ", balance)
        withdrawSuccess=1
    else:
        print("no sufficiant balance Your available balance is : ",balance)
        withdraw = int(input("please enter the amount you want to withdraw : "))