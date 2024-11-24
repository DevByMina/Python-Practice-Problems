def prime(num):
    if(num==2):
        return print("prime")
    elif(num==1):
        return print("Not Prime")
    else:
        for i in range(2,num-1,1):
            if(num%i==0):
                return print("Not Prime")
        return print("prime")
    
prime(8)