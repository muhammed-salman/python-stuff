class Animal:
    def __init__(self,type):
        self.type=type

    def __str__(self):
        mydata={'name':self.name,'type':self.type}
        return str(mydata)

    def getname(self):
        return self.name

dog=Animal("Dog")

dog.name="Scobby"
print("I am a "+dog.type+" my name is "+dog.getname())
print(dog)
with open('myfile.txt','w') as myfile:
    myfile.write(str(dog))
