s=input()
n=int(input())

count=0
no_of_a=0
for c in s:
    if(c=="a"):
        count=count+1

l=len(s)
no_of_a=(n//l)*count
sublen=n%l
sub_count=0
i=0
while sublen!=0:
    if(s[i]=='a'):
        sub_count=sub_count+1
    i=i+1
    sublen=sublen-1

no_of_a=no_of_a+sub_count

print(no_of_a)
