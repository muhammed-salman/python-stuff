n=int(input())
ar=[]
count=[]

for i in range(0,n):
	ar.append(int(input()))
	count.append(0)

for i in range(0,n):
	count[ar[i]-1]=count[ar[i]-1]+1

max=count[0]
max_type=0

for i in range(0,n):
	if(max<count[i]):
		max=count[i]
		max_type=i+1

print("\n")
print(max_type)
