from classes.game import Person, Bcolors


magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]

player = Person(460, 65, 34, magic)
enemy = Person(1200, 65, 35, magic)

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
        print("You attacked for " + str(dmg), "points of damage.")
    elif index == 1:
        print("=======Spells=========")
        player.choose_magic()
        magic_choice = int(input("Choose a Spell: ")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(Bcolors.FAIL + "\nNot enough MP.\n" + Bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(Bcolors.OKBLUE + "\n" + spell + " deals", str(magic_dmg), "points of damage." + Bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", str(enemy_dmg))

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














