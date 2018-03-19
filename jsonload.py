import json

dogs={
'name': 'Scobby',
'type': 'Dog'
}
'''
try:
    with open('mydata.json','w') as myfile:
        json.dump(dogs,myfile)
except:
    print("Something fishy...")
'''
try:
    with open('mydata.json') as myfile:
        dogs=json.load(myfile)
        print(str(dogs))
except:
    print("Something fishy...")
