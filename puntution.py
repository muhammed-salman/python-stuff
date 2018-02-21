puntuation='!#,.:;"`\''
string=input("Please enter any string with puntuation: ")
stringWithoutPun=""

for c in string:
    if c not in puntuation:
        stringWithoutPun += c
print("string without puntuation= "+stringWithoutPun)
