n=int(input())
k=int(input())
c=[]
for i in range(0,n):
    c.append(int(input()))

b=int(input())

shared_cost=0
for(i in range(0,n)):
    if(i!=k):
        shared_cost=shared_cost+c[i]
shared_cost=shared_cost/2
if(shared_cost==b):
    print("Bon Apptite")
else:
    print(b-shared_cost)
