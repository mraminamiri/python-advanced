# elementry class :
class Person:
    def __init__(self,name,age):  # inittial VAr
        self.name = name
        self.age = age

    def get_name(self):
        print(f"your name is {self.name}")

    def info(self):
        print(f"your name is : {self.name}")
        print(f"your age is : {self.age}")


 
me = Person("mohammad amin", 25)  ##Build a model
me.info()


### intermediate class
class Computer:
    count = 0
    def __init__(self,name,ram,hard,cpu):
        Computer.count= +1
        self.name=name
        self.ram=ram
        self.hard=hard
        self.cpu=cpu


    def value(self):
        price = self.ram +self.cpu + self.hard
        print(f"your pc is {self.name} and your value pc is {price}")

    def __del__(self):
     Computer.count = -1

pc1 = Computer("apple",16,2,2)  #build a object drom class
print(pc1.value())
pc1.__del__()