from classes.game import Person, Bcolors


magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 35, magic)

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
        print(Bcolors.UNDERLINE + "You attacked for " + str(dmg), "points of damage. Enemy HP:", str(enemy.get_hp()) + Bcolors.ENDC)


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(Bcolors.UNDERLINE + "Enemy attacks for", str(enemy_dmg), "Player HP:", str(player.get_hp()) + Bcolors.ENDC)


#    running = False




'''
    elif index == 1:
        print("=======Spells=========")
        player.choose_magic()
        choice = input("Choose a Spell: ")
        index = int(choice) - 1
'''




