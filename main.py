from hercules import hercules
from monster import monster


monsters=[]
x=0
monsters.append(monster())

while (x<5):
    monsters.append(monster())
    x+=1

for obj in monsters:
    print(obj.getName(), obj.getHp(), sep =" ")









