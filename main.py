from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# Create Black Magic
fire = Spell("Fire", 10, 500, "black")
thunder = Spell("Thunder", 10, 500, "black")
blizzard = Spell("Blizzard", 10, 500, "black")
meteor = Spell("Meteor", 20, 700, "black")
quake = Spell("Quake", 14, 640, "black")

# Create White Magic
cure = Spell("Cure", 12, 250, "white")
cura = Spell("Cura", 18, 500, "white")
curaga = Spell("Curaga", 20, 1500, "white")

# Create Some items
potion = Item("Potion", "potion", "Heals 100 HP", 100)
hipotion = Item("Hi-Potion", "potion", "Heals 300 HP", 300)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("Mega-Elixer", "elixer", "Fully restores HP/MP of all party members", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells = [fire, meteor, curaga]

player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 5}, {"item": grenade, "quantity": 5}]


print("=============")
print(bcolors.FAIL + bcolors.BOLD + "IT'S A GAME!!" + bcolors.ENDC)
print("=============")

playerName = ""
starting = True
while starting == 1:
    playerName = input("Enter Player Name: ")
    if len(playerName) > 10:
        print("ERROR: Name must be under 10 characters")
        pass
    while len(playerName) < 10:
        playerName += " "
    if len(playerName) == 10:
            starting = False


# Instantiate People
player1 = Person(playerName, 3260, 171, 65, 34, player_spells, player_items)
player2 = Person("Lulu      ", 2160, 35, 110, 34, player_spells, player_items)
player3 = Person("Cait Sith ", 5150, 105, 35, 34, player_spells, player_items)


enemy1 = Person("Imp    ", 1200, 130, 560, 320, enemy_spells, [])
enemy2 = Person("Seymour", 11200, 240, 150, 25, enemy_spells, [])
enemy3 = Person("Imp    ", 1200, 130, 560, 320, enemy_spells, [])


players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

while running:
    print("\n")
    print(bcolors.BOLD + bcolors.UNDERLINE + "NAME:                   |HP:         "
                                             "                           |MP:        "
          + bcolors.ENDC)

    for player in players:
        player.get_stats()
    print(bcolors.BOLD + bcolors.UNDERLINE + "                                      "
                                             "                                      "
          + bcolors.ENDC)
    for enemy in enemies:
        enemy.get_enemy_stats()

    print("\n\n")

# ACTIONS MENU
    for player in players:
        player.choose_action()
        choice = input(bcolors.BOLD + "-Choose an Action: " + bcolors.ENDC)
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)
            print("\n" + "~~~~~", player.name.replace(" ", ""), "attacked " + enemies[enemy].name.replace(" ", "")
                  + " for " + bcolors.OKBLUE + str(dmg),
                  bcolors.ENDC + "points of damage.")
            print(bcolors.OKBLUE + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                  + bcolors.ENDC + "\n")

            if enemies[enemy].get_hp() == 0:
                print(bcolors.FAIL + "====" + enemies[enemy].name.replace(" ", "") + " has died." + bcolors.ENDC)
                del enemies[enemy]

    # MAGIC MENU
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input(bcolors.BOLD + "-Choose a Spell: " + bcolors.ENDC)) - 1

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
                print("\n" + "~~~~~", spell.name + " healed for", bcolors.OKGREEN + str(magic_dmg), bcolors.ENDC +
                      "HP.")
                print(bcolors.OKGREEN + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                      + bcolors.ENDC + "\n")

            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)

                print("\n" + "~~~~~", spell.name + " deals", bcolors.OKBLUE + str(magic_dmg) + bcolors.ENDC +
                      " damage to", enemies[enemy].name.replace(" ", ""))
                print(bcolors.OKBLUE + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                      + bcolors.ENDC + "\n")

                if enemies[enemy].get_hp() == 0:
                    print(bcolors.FAIL + "====" +enemies[enemy].name.replace(" ", "") + " has died." + bcolors.ENDC)
                    del enemies[enemy]


    # ITEMS MENU
        elif index == 2:
            player.choose_item()
            item_choice = int(input(bcolors.BOLD + "-Choose an Item: " + bcolors.ENDC)) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\nNone left...\n" + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print("\n" + "~~~~~", player.name.replace(" ", "") + "'s " + item.name + " healed for",
                      bcolors.OKGREEN + str(item.prop) + bcolors.ENDC, "HP.")
                print(bcolors.OKGREEN + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                      + bcolors.ENDC + "\n")

            elif item.type == "elixer":

                if item.name == "Mega-Elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp

                print("\n" + "~~~~~", item.name + " fully restores" + bcolors.OKGREEN + " HP/MP" + bcolors.ENDC)
                print(bcolors.OKGREEN + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                      + bcolors.ENDC + "\n")

            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)

                print("\n" + "~~~~~",  item.name + " deals", bcolors.OKBLUE + str(item.prop) + bcolors.ENDC +
                      " damage to " + enemies[enemy].name.replace(" ", ""))
                print(bcolors.OKBLUE + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                      + bcolors.ENDC + "\n")

                if enemies[enemy].get_hp() == 0:
                    print(bcolors.FAIL + "====" + enemies[enemy].name.replace(" ", "") + " has died." + bcolors.ENDC)
                    del enemies[enemy]

    # CHECK IF BATTLE IS OVER
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    # CHECK IF PLAYER WON
    if defeated_enemies == 3:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False

    # CHECK IF ENEMY WON
    if defeated_players == 3:
        print(bcolors.FAIL + "Game Over" + bcolors.ENDC)
        running = False

    # ENEMY ATTACK PHASE
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            # Chose Attack
            target = random.randrange(0, 3)
            enemy_dmg = enemies[0].generate_damage()

            players[target].take_damage(enemy_dmg)

            print("~~~~~", enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", ""), "for" +
                  bcolors.FAIL, str(enemy_dmg), bcolors.ENDC + "damage.")
            print(bcolors.FAIL + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                  + bcolors.ENDC)

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print("~~~~~", enemy.name.replace(" ", "") + "'s " + spell.name + " heals",
                      bcolors.OKGREEN + str(magic_dmg), bcolors.ENDC + "HP.")
                print(bcolors.OKGREEN + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                      + bcolors.ENDC)

            elif spell.type == "black":
                target = random.randrange(0, 3)
                players[target].take_damage(magic_dmg)

                print("~~~~~", enemy.name.replace(" ", "") + "'s " + spell.name + " deals", bcolors.FAIL +
                      str(magic_dmg) + bcolors.ENDC, "damage to", players[target].name.replace(" ", ""))
                print(bcolors.FAIL + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                      + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(bcolors.FAIL + "====" + players[target].name.replace(" ", "") + " has died." + bcolors.ENDC)
                    del players[player]













