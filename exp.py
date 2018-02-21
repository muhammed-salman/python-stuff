matA=[]
matB=[]
mutMat=[]

noRowA=int(input("Enter the number of rows in matrix A: "))
noColA=int(input("Enter the number of cols in matrix A: "))
noColB=int(input("Enter the number of cols in matrix B: "))

for i in range(noRowA):
    matA.append([])

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
#
# for row in range(order):
#     for col in range(order):
#         sumMatA[row].append(matA[row][col]+matB[row][col])
#         subMatA[row].append(matA[row][col]-matB[row][col])
#
# print("\nSum of matrix A and B: \n")
# for row in range(order):
#     for col in range(order):
#         print("{}\t".format(sumMatA[row][col]),end='')
#     print("\n")
#
# print("\nSubtraction of matrix A and B: \n")
# for row in range(order):
#     for col in range(order):
#         print("{}\t".format(subMatA[row][col]),end='')
#     print("\n")
