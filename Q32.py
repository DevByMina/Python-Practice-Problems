def charCount(string):
    frequency = {}

    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    return frequency

string="Embedded System"
print(charCount(string))