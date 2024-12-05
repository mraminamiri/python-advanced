class Player:
    def __init__(self,name,age,injury):
        self.name = name
        self.age = age
        self.injury = injury
    def get_status(self):
        print(self.name + ' is   ' + str(self.age) +'    years old'+ '\n Injured :'+ str(self.injury))

player1 = Player(name='John',age=23,injury=False)
player1.get_status()
player2 = Player(name='Ronaldo',age=39,injury=False)
player2.get_status()