try:
    with open('myfile2.txt') as myfile:
        print(myfile.read())
except:
    pass
    # print("Sorry I cannot find this file on your drive")

a=10
b=3
try:
    c=a/b
except ZeroDivisionError:
    b=5
    c=a/b
    print("Denominator cannot be zero")
else:
    print(c)

print(str(c+10))
