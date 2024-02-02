class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print("Your name is %s" % self.name)
        print("Your age is %s" % self.age)



#one = Person(input("What is your name? "),int(input("how old are you")))
#one.info()
#______---------------------------------------__________________----------------------------_______________________-----------

class computer:
    #constrocter fonction
    def __init__(self,ram,cpu,hard):
        self.ram = ram
        self.cpu = cpu
        self.hard = hard

    def value(self):
        return (self.ram+self.cpu)

class laptop(computer):
    def value(self):
        return(self.ram + self.cpu + self.size)




pc1 = computer(4,2,2)
print(pc1.value())


laptop1 = laptop(2,2,2)
laptop1.size=15

print(laptop1.value())



laptop2 = laptop(2,5,2)
laptop2.size=16
print(laptop2.value())

