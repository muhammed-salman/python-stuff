matA=[]
matB=[]
mulMat=[]

noRowA=int(input("Enter the number of rows in matrix A: "))
noColA=int(input("Enter the number of cols in matrix A: "))
noColB=int(input("Enter the number of cols in matrix B: "))

#intializing each row in matrix as empty list
for i in range(noRowA):
    matA.append([])
    mulMat.append([])

for i in range(noColB):
    matB.append([])

print("Enter the elements of matrix A row-wise: ")

for row in range(noRowA):
    for col in range(noColA):
        matA[row].append(int(input()))

print("Enter the elements of matrix B row-wise: ")

for row in range(noColA):
    for col in range(noColB):
        matB[row].append(int(input()))

#intializing resultant matrix with zeros
for row in range(noRowA):
    for col in range(noColB):
        mulMat[row].append(0)

#Multiplication of matix A and B
for row in range(noRowA):
    for col in range(noColB):
        for k in range(noColA):
            mulMat[row][col]+=matA[row][k]*matB[k][col]


print("\nMultiplication of matrix A and B: \n")
for row in range(noRowA):
    for col in range(noColB):
        print("{}\t".format(mulMat[row][col]),end='')
    print("\n")
