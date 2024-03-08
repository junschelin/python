from string import ascii_lowercase
aList = list(ascii_lowercase)

def lower_find(word):
    for letter in word:
        for alphabet in aList:
            if letter == alphabet:
                count += 1
             

print(aList)