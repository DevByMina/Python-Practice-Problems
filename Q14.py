primes= []
for num in range(1,20+1,1):
    if (num>1):
        for i in range(2,num,1):
            if(num%i == 0):
                break
            else:
                primes.append(num)
                break
print("Prime numbers in the given range is: ",primes)