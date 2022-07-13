import random

class Hercules:

    def __init__(self):
        self.hp=100
        self.att=5
        self.attacks = [
            {"name":"Sword Slash","damage":random.choice([45,50,55])},
            {"name":"Arrow Show", "damage":random.choice([40,50,60])},
            {"name":"Spear Thrust","damage":random.choice([1,1,100])}            
        ]
    
    def getAtt(self):
        return self.att

    def getHp(self):
        return self.hp
    
    def addHp(self, hp):
        self.hp-=hp
    
    def setHp(self,hp):
        self.hp=hp

    
    


