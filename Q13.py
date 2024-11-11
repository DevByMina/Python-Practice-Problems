words= str(input("Please enter a word: "))
count=0
for word in words:
    if(word=='a'or word=='e'or word=='o'or word=='i' or word=='u'):
        count +=1
print(count)