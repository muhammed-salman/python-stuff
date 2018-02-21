guests=['Alpha','Gama','Beta']
print('Following Guest are Invited for My Dinner Party');
for guest in guests:
    print("\n"+guest)
guests[1]='Sigma'
print('Following Guest are Invited for My Dinner Party');
for guest in guests:
    print("\n"+guest)
print("\nFollowing Guests are removed from list")
for i in range(len(guest)-3):
    print("\nSorry "+guests.pop()+", you are not invited for dinner.")
print('Following Guest are Still Invited for My Dinner Party');
for guest in guests:
    print("\n"+guest)

for i in range(len(guests)):
    del guests[0]
print(guests)
print("\nSorry! The Dinner Party is Cancelled.")
