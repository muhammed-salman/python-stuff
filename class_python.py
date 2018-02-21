class Animal:
    def __init__(self,type):
        self.type=type

    def __str__(self):
        return "I am a Animal Class Object"

    def getname(self):
        return self.name

dog=Animal("Dog")

dog.name="Scobby"
print("I am a "+dog.type+" my name is "+dog.getname())
print(dog)
