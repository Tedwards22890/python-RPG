import random

class Hercules:

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

    def attack(self):
        self.attacks = [
            {"name":"Sword Slash","damage":random.choice([45,50,55])},
            
        ]

            "1) Sword Slash": [45,50,55], 
            "2) Arrow Shot": [40,45,60],   
            "3) Power Punch": [35,40,70],  
            "4) Spear Thrust": [1,1,100]   
        
        print(attacks.keys())
        choice = input(f"Please choose an attack from {attacks}")
        x= random.choice(list(attacks["1) Sword Slash"]))
        return x
        
    
    
    


