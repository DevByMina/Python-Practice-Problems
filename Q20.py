string= input("Enter a string: ")

reversedString=""
for char in string:
    reversedString=char+reversedString
if(string==reversedString):
    print("The string is a palindrome")
else:
    print("The string is not palindrome")