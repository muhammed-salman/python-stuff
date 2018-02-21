list1=[]
list2=[]
sumlist=[]
n=int(input("How many elements in a list:"))
print("Please enter the elements of List 1: ")
for i in range(n):
    list1.append(int(input()))

print("Please enter the elements of List 2: ")
for i in range(n):
    list2.append(int(input()))

for i in range(len(list1)):
    result=list1[i]+list2[i]
    sumlist.append(result)
print(sumlist)
