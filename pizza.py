pizza={
    'name':['Mexican','Italian','Fresh Farm'],
    'crust': ['Thin','Thick'],
    'toppings':['Onion','Olive','Tomatto','Jalepano','Mushroom']
}

print("Welcome to Pizza Outlet")
name=input("\nPlease Enter Your Name: ")
phone=input("\nYour Phone Number: ")
order={'name':name,'phone':phone,'toppings':[]}
print("\nHelp us to build your order")
print("\nSelect Your Pizza")
i=1
for val in pizza['name']:
    print("\n"+str(i)+"."+val)
    i+=1
choice=input("Enter Your Choice: ")
order['pizza_name']=pizza['name'][int(choice)-1]
print("\nSelect Your Crust")
i=1
for val in pizza['crust']:
    print("\n"+str(i)+"."+val)
    i+=1
choice=input("Enter Your Choice: ")
order['crust']=pizza['crust'][int(choice)-1]
while choice!='q':
    print("\nChoose Your Toppings")
    i=1
    for val in pizza['toppings']:
        print("\n"+str(i)+"."+val)
        i+=1
    choice=input("Enter Your Choice (q for quit): ")
    if choice!='q':
        order['toppings'].append(pizza['toppings'][int(choice)-1])
print(order)
