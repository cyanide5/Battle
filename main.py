from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


# Create Black Magic
fire = Spell("Fire", 10, 500, "black")
thunder = Spell("Thunder", 10, 500, "black")
blizzard = Spell("Blizzard", 10, 500, "black")
meteor = Spell("Meteor", 20, 700, "black")
quake = Spell("Quake", 14, 640, "black")

# Create White Magic
cure = Spell("Cure", 12, 250, "white")
cura = Spell("Cura", 18, 500, "white")

# Create Some items
potion = Item("Potion", "potion", "Heals 100 HP", 100)
hipotion = Item("Hi-Potion", "potion", "Heals 300 HP", 300)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("Mega-Elixer", "elixer", "Fully restores HP/MP of all party members", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 5}, {"item": grenade, "quantity": 5}]


# Instantiate People
player1 = Person("Zucav:    ", 3260, 171, 20, player_spells, player_items)
player2 = Person("Mog:      ", 2160, 35, 70, player_spells, player_items)
player3 = Person("Cait Sith:", 5150, 105, 15, player_spells, player_items)
enemy = Person("Magus", 11200, 240, 150, [], [])

players = [player1, player2, player3]


running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "IT'S A GAME!!" + bcolors.ENDC)


while running:
    print("=====================")

    print("\n")
    print(bcolors.BOLD + bcolors.UNDERLINE + "NAME:                    |HP:         "
                                             "                                      |MP:      "
          + bcolors.ENDC)
    for player in players:
        player.get_stats()
    print(bcolors.BOLD + bcolors.UNDERLINE + "                                           "
                                             "                                           "
          + bcolors.ENDC)
    print("\n\n")

    for player in players:
        player.choose_action()
        choice = input("Choose an Action: ")
        index = int(choice) - 1

    # ACTIONS MENU
        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("\n" + "~~~~~You attacked for " + bcolors.OKBLUE + str(dmg) + bcolors.ENDC, "points of damage.")

    # MAGIC MENU
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose a Spell: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_dmg()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP.\n" + bcolors.ENDC)
                continue
            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print("\n" + "~~~~~" + spell.name + " healed for", bcolors.OKGREEN + str(magic_dmg), bcolors.ENDC +
                      "HP.")

            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print("\n" + "~~~~~" + spell.name + " deals", bcolors.OKBLUE + str(magic_dmg), bcolors.ENDC + "damage.")

    # ITEMS MENU
        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose an Item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\nNone left...\n" + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print("\n" + "~~~~~" + item.name + " healed for", bcolors.OKGREEN + str(item.prop), bcolors.ENDC +
                      "HP.")

            elif item.type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print("\n" + "~~~~~" + item.name + " fully restores" + bcolors.OKGREEN + " HP/MP" + bcolors.ENDC)

            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print("\n" + "~~~~~" + item.name + " deals", bcolors.OKBLUE + str(item.prop), bcolors.ENDC + "damage.")

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print("~~~~~Enemy attacks for", bcolors.FAIL + str(enemy_dmg) + bcolors.ENDC + " damage.")

    print("----------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC, "\n")


# End Game
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif player1.get_hp() == 0:
        print(bcolors.FAIL + player1.name + " is dead" + bcolors.ENDC)
        continue
    elif player2.get_hp() == 0:
        print(bcolors.FAIL + player1.name + " is dead" + bcolors.ENDC)
        continue
    elif player3.get_hp() == 0:
        print(bcolors.FAIL + player1.name + " is dead" + bcolors.ENDC)
        continue
















