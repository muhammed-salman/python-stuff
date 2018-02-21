string=input("Please enter any string: ")
vowelsCount=0
consonant=0
spaces=0
vowels=['a','i','e','o','u']

for c in string:
    if c in vowels:
        vowelsCount+=1
    elif c==' ':
        spaces+=1
    else:
        consonant+=1

print("No of Vowels: {}, No of Spaces: {}, No of Consonants{}".format(vowelsCount,spaces,consonant))
