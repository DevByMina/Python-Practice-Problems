def strListUpper(list):
    upperlist=[]
    upperword=""
    for word in list:
        for char in word:
            upperword += chr(ord(char)-32)
        upperlist.append(upperword)
        upperword=""
    return upperlist

mylist=["mina","sameh","depi","machine"]
print(strListUpper(mylist))