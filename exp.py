from functools import reduce

def celcius(T):
    return (float(5)/9)*(T-32)

temp=[36,32,55,45,40]

ftemp=map(lambda T:(float(9)/5)*T+32,temp)

print(list(ftemp))

num=[1,2,3,4,5,6,7,8,9,10]

even_num=filter(lambda x:x%2==0,num)
print(list(even_num))

def power_two(x):
    for i in range(0,100):
        if(x==2**i):
            return True
        elif(x<2**i):
            return False
power_two_num=filter(power_two,num)

print(list(power_two_num))

sum_num=reduce(lambda x,y:x+y,num)
print(sum_num)
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)

list2=map(lambda x,y:x**y/fact(y),num,list(range(0,10)))

val=reduce(lambda x,y:x+y,list(list2))
print(val)
