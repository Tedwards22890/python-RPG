from hercules import Hercules
from monster import Monster
import time

def lost_game():
    print("The final strike bears down on you.")
    print("Your strength fades as you fall to the ground.")
    print("The last thing you remember is...")
    print("Cerberus continues to roam free to this very day")
    print("Game Over!")
    x=int(input("Do you want to try again? (y/n): "))
    if (x=="y"):
        RunGame()
    else:
        print("Thanks for playing!")


def Attack(herc, mons):
    while (herc.getHp() >=0 or mons.getHp()>=0):
        print(f"Your HP: {herc.getHp()}")
        print(f"{mons.name} hp is {mons.getHp()}")
        print(f"Press 1 for {herc.attacks[0]['name']}")
        print(f"Press 2 for {herc.attacks[1]['name']}")
        print(f"Press 3 for {herc.attacks[2]['name']}")
        choice=int(input(": "))
        if (choice == 1):
            x=(herc.getAtt()+herc.attacks[0]["damage"])
            print(f"You swing your mighty sword and do {x} damage!")
            mons.addHp(x)
        elif (choice==2):
            x=(herc.getAtt()+herc.attacks[1]["damage"])
            print(f"At blinding speed, you draw back and arrow. Your arrow soars and does {x} damage!")
            mons.addHp(x)
        elif (choice==3):
            x=(herc.getAtt()+herc.attacks[1]["damage"])
            print(f"You thrust your spear and do {x} damage!")
            mons.addHp(x)
        else:
            print("You hesitate too long! (Be sure to press 1, 2 or 3!)")
        if (mons.getHp()<=0):
            print(f"{mons.getName()} has been slain!")
            x=herc.getHp()
            return x
        else:
            print(f"{mons.getName()} {mons.randomAttack()}")
            y=mons.getAtt()
            print(f"{mons.name} deals {y}")
            herc.addHp(y)
    if (herc.getHp<=0):
        lost_game()
    else:
        print(f"{mons.getName()} has been slain!")
        time.sleep(5)


def RunGame():
    print("Welcome Hercules,\n the great hero of the greeks!")

    print("King Eurystheus, ruler of Argos, has tasked you with the great honor of capturing...")
    time.sleep(3)
    print("Cerberus!!!!!")
    time.sleep(3)
    print("The fearsome guard dog of the underworld!\nRumor has it: Hades plans to unleash this terrible beats upon the world. Only Hercules can stop Cerberus by capturing him!")
    time.sleep(2)
    print("Hercules sets out to retrieve this vicious dog!")
    time.sleep(3)
    player=Hercules()
    m1 = Monster(0)
    m2 = Monster(1)
    m3 = Monster(2)
    player_hp = Attack(player,m1)
    player.setHp(player_hp)
    print(f"As {m1.getName()} falls before the might Hercules, he takes a step forward owards the underworld.")
    print(f"As you enter the underworld, you hear a loud roaring. A {m2.getName()} steps forward, unwilling to let Hercules pass!")
    player_hp = Attack(player,m2)
    player.setHp(player_hp)
    print(f"{m2.getName()} falls to the grounds. Hercules continued on, unbothered by lesser creatures of the deep.")
    print(f"That is when the mighty {m3.getName()} comes into view. But it will not be captured without a fight!")
    Attack(player,m3)
    print("Yeah, you win")





RunGame()



