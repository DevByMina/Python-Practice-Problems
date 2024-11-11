correctWord = input("Enter a word: ")
reversedWord = ""

for i in range(len(correctWord) - 1, -1, -1):
    reversedWord += correctWord[i]

print(reversedWord)