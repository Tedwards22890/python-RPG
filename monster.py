import random
class Monster:

    hp=0
    att=0
    name="none"

    def __init__(self):
        self.hp = 20 + random.randint(-10,10)
        self.att = 7+ random.randint(-3,3)
        self.name=self.namer(0)

    def getAtt(self):
        return self.att

    def getHp(self):
        return self.hp
    
    def addHP(self, x):
        self.hp-=x
        return self.hp  

    def getName(self):
        return self.name

    def namer(self,x):
        names=["Nemean Lion","Lernaean Hydra","Cerberus"] 
        return names[x]
    
