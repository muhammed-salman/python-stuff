matA=[]
matB=[]
sumMatA=[]
subMatA=[]

order=int(input("Enter the order of matrices: "))

for i in range(order):
    matA.append([])
    matB.append([])
    sumMatA.append([])
    subMatA.append([])

print("Enter the elements of matrix A row-wise: ")

for row in range(order):
    for col in range(order):
        matA[row].append(int(input()))

print("Enter the elements of matrix B row-wise: ")

for row in range(order):
    for col in range(order):
        matB[row].append(int(input()))

for row in range(order):
    for col in range(order):
        sumMatA[row].append(matA[row][col]+matB[row][col])
        subMatA[row].append(matA[row][col]-matB[row][col])

print("\nSum of matrix A and B: \n")
for row in range(order):
    for col in range(order):
        print("{}\t".format(sumMatA[row][col]),end='')
    print("\n")

print("\nSubtraction of matrix A and B: \n")
for row in range(order):
    for col in range(order):
        print("{}\t".format(subMatA[row][col]),end='')
    print("\n")
