rows=9

#printing hollow traingle
for row in range(1,rows+1):
    for col in range(1,row+1):
        #any char of first & last rows are never blank
        #any char of first & last col are never blank
        #remaining all the char are blank
        if(row!=1 and row!=rows and col!=1 and col!=row):
            print("  ",end='')
        else:
            print("* ",end='')
    print()

#printing hollow square
for row in range(1,rows+1):
    for col in range(1,rows+1):
        #any char of first & last rows are never blank
        #any char of first & last col are never blank
        #remaining all the char are blank
        if(row!=1 and row!=rows and col!=1 and col!=rows):
            print("  ",end='')
        else:
            print("* ",end='')
    print("\r")

#printing hollow rectangle
for row in range(1,rows+1):
    for col in range(1,rows*2+1):
        #any char of first & last rows are never blank
        #any char of first & last col are never blank
        #remaining all the char are blank
        if(row!=1 and row!=rows and col!=1 and col!=rows*2):
            print("  ",end='')
        else:
            print("* ",end='')
    print("\r")
