import random
class monster:

    hp=0
    att=0
    name="none"

    def namer(self):
        names=["Cerberus","Circe","Fenyx","Hyrda","Ladon","Othrus","Stymphalides"] 
        self.name= names[random.randint(0,6)]

    def __init__(self):
        self.hp = 20 + random.randint(-10,10)
        self.att = 7+ random.randint(-3,3)

    def getAtt(self):
        return self.att

    def getHp(self):
        return self.hp
    
    def addHP(self, x):
        self.hp-=x
        return self.hp  

    def getName(self):
        return self.name
    
