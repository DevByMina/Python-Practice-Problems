def largest_word(list):
    maxLength=0
    maxWord=""
    for word in list:
        if(len(word)>maxLength):
            maxLength=len(word)
            maxWord=word
    return maxWord

mylist=["mina","sameh","depi","Machine"]
print(largest_word(mylist))