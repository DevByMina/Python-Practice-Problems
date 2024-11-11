correctPass= input("Please enter a password to be saved : ")
print("password is saved successfully")
correct=0
incorrectFlag =0
while(not(correct)):
    incorrectFlag=0
    userPass= input("Please enter password : ")
    if(len(correctPass) != len(userPass)):
        incorrectFlag=1
    else:
        for i in range(0,len(correctPass),1):
             if(correctPass[i] != userPass[i]):
                 incorrectFlag=1
    if(incorrectFlag ==1):
        print("incorrect password entered")
    else:
        print("correct password entered")
        correct=1


