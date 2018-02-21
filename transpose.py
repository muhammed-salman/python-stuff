matA=[
    [1,2,3,7],
    [4,5,6,9]
]
matTransA=[]
for i in range(len(matA[0])):
    matTransA.append([])

for row in range(len(matA)):
    for col in range(len(matA[0])):
        matTransA[col].append(matA[row][col])

for row in range(len(matTransA)):
    for col in range(len(matTransA[0])):
        print("{}\t".format(matTransA[row][col]),end='')
    print("\n")
