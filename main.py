from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.inventory import Item

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]


# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create Some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("Mega-Elixer", "elixer", "Fully restores HP/MP of all party members", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [potion, hipotion, superpotion, elixer, hielixer, grenade]


# Instantiate People
player = Person(460, 65, 34, player_spells, player_items)
enemy = Person(1200, 65, 35, [], [])

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)


while running:
    print("=====================")
    player.choose_action()
    choice = input("Choose an Action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("\n" + "~~~~~You attacked for " + Bcolors.OKBLUE + str(dmg) + Bcolors.ENDC, "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose a Spell: ")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_dmg()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(Bcolors.FAIL + "\nNot enough MP.\n" + Bcolors.ENDC)
            continue
        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print("\n" + "~~~~~" + spell.name + " healed for", Bcolors.OKGREEN + str(magic_dmg), Bcolors.ENDC + "HP.")

        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print("\n" + "~~~~~" + spell.name + " deals", Bcolors.OKBLUE + str(magic_dmg), Bcolors.ENDC + "damage.")

    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose Item: ")) - 1
#need purpose
        continue


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("~~~~~Enemy attacks for", Bcolors.FAIL + str(enemy_dmg) + Bcolors.ENDC + " damage.")

    print("----------------")
    print("Enemy HP:", Bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + Bcolors.ENDC, "\n")

    print("Your HP:", Bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + Bcolors.ENDC)
    print("Your MP:", Bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + Bcolors.ENDC, "\n")




##End Game
    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN + "You Win!" + Bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Bcolors.FAIL + "You Lose!" + Bcolors.ENDC)
        running = False














