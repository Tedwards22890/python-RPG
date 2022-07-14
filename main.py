from hercules import Hercules
from monster import Monster
import time

def lost_game():
    print("The final strike bears down on you.")
    print("Your strength fades as you fall to the ground.")
    print("The last thing you remember is...")
    print("Cerberus continues to roam free to this very day")
    print("Game Over!")
    print("Try again...")
    quit()


def Attack(herc, mons):
    time.sleep(3)
    while (herc.getHp() >=0 and mons.getHp()>=0):
        print()
        print(f"Your HP: {herc.getHp()}")
        print(f"{mons.name} hp is {mons.getHp()}")
        print(f"Press 1 for {herc.attack_list(0,'name')}")
        print(f"Press 2 for {herc.attack_list(1,'name')}")
        print(f"Press 3 for {herc.attack_list(2,'name')}")
        choice=input(": ")
        if (choice == "1"):
            x=(herc.getAtt()+herc.attack_list(0,'damage'))
            print(f"You swing your mighty sword and do {x} damage!")
            mons.addHp(x)
        elif (choice=="2"):
            x=(herc.getAtt()+herc.attack_list(1,'damage'))
            print(f"At blinding speed, you draw back an arrow. Your arrow soars and does {x} damage!")
            mons.addHp(x)
        elif (choice=="3"):
            x=(herc.getAtt()+herc.attack_list(2,'damage'))
            print(f"You thrust your spear and do {x} damage!")
            mons.addHp(x)
        else:
            print("Hercules hesitatde too long! (Be sure to press 1, 2 or 3!)")
        time.sleep(3)
        if (mons.getHp()<=0):
            print(f"{mons.getName()} has been slain!")
            x=herc.getHp()
            return x
        else:
            print(f"{mons.getName()} {mons.randomAttack()}")
            y=mons.getAtt()
            print(f"{mons.name} deals {y}")
            herc.addHp(y)
        time.sleep(3)
    if (herc.getHp()<=0):
        lost_game()
    else:
        print(f"{mons.getName()} has been slain!")
        time.sleep(5)


def RunGame():
    print("Welcome Hercules,\n the great hero of the greeks!")
    time.sleep(5)
    print("King Eurystheus, ruler of Argos, has tasked you with the great honor of capturing...")
    time.sleep(3)
    print("Cerberus!!!!!")
    time.sleep(3)
    print("The fearsome guard dog of the underworld!")
    time.sleep(1)
    print("Rumor has it: Hades plans to unleash this terrible beast upon the world. Only Hercules can stop Cerberus by capturing him!")
    time.sleep(2)
    print("Hercules sets out to retrieve this vicious dog!")
    time.sleep(2)
    player=Hercules()
    m1 = Monster(0)
    m2 = Monster(1)
    m3 = Monster(2)
    print("As Hercules leaves the kingdom of Argos and heads into the forest he hears a great rumbling noise.")
    time.sleep(3)
    print("Before his very eyes a giant lion appears from behind a large hill.")
    time.sleep(3)
    print("The lion roars, issuing a challenge. Hercules must fight!")
    player_hp = Attack(player,m1)
    player.setHp(player_hp)
    print(f"As {m1.getName()} falls before the might Hercules, he takes a step forward towards the underworld.")
    time.sleep(3)
    print(f"As you enter the underworld, you hear a loud roaring. A {m2.getName()} steps forward, unwilling to let Hercules pass!")
    player_hp = Attack(player,m2)
    player.setHp(player_hp)
    print(f"{m2.getName()} falls to the grounds. Hercules continued on, unbothered by lesser creatures of the deep.")
    time.sleep(3)
    print(f"That is when the mighty {m3.getName()} comes into view. But it will not be captured without a fight!")
    Attack(player,m3)
    print(f"As the mighty {m3.getName()} falls before Hercules, he wipes his brow.")
    time.sleep(2)
    print(f"Hercules picks up {m3.getName()} and begins his long trek home.")
    time.sleep(2)
    print(f"Having slain all creatures before him, Hercules returns to Argo to meet king Eurystheus.")
    time.sleep(2)
    print(f"The people of Argo are once again safe... until Hades begin hatching another plot.")
    time.sleep(7)
    print()
    print()
    print()
    print(f"Credits\nProducer: Travis Edwards\nLead Programmer: Travis Edwards\nDirector: Travis Edwards\nGame Tester: Mary Grace Gascon")
    time.sleep(3)
    print("Special thanks to:\nDevCodeCamp\nW3Schools\nMary Grace Gascon")
    time.sleep(3)
    print("Thanks for playing...")
    time.sleep(7)
    print("Until next time!")





RunGame()



