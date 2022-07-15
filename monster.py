import random
class Monster:

    def __init__(self,x):
        self.hp = 75 + random.randint(-10,10)
        self.att = (30+ random.randint(-3,3))
        self.name=self.namer(x)

    def getAtt(self):
        x=(self.att + random.randint(-5,5))
        return x

    def getHp(self):
        return self.hp
    
    def addHp(self, x):
        self.hp-=x
        return self.hp  

    def getName(self):
        return self.name

    def namer(self,x):
        names=["Nemean Lion","Lernaean Hydra","Cerberus"] 
        return names[x]
    
    def randomAttack(self):
        self.random_lists=["slashes out with its mighty claws striking Hercules' chest","bites down on Hercules' leg!","stomps on Hercules'!","rushes into Hercules' with blinding speed"]
        return random.choice(self.random_lists)

    
