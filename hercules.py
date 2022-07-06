class hercules:

    hp=0
    att=0

    def __init__(self):
        self.hp=100
        self.att=5
    
    def getAtt(self):
        return self.att

    def getHp(self):
        return self.hp
    
    def addHP(self, x):
        self.hp=self.hp-x
        return self.hp
    


