import random
from classes.inventory import Item

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Person:
    def __init__(self, name, hp, atk, mp, dfn, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.maxmp = mp
        self.mp = mp
        self.magic = magic
        self.dfn = dfn
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + bcolors.BOLD + bcolors.OKBLUE + self.name + bcolors.ENDC)
        print(bcolors.UNDERLINE + "═══ACTIONS═══" + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.UNDERLINE + "═══MAGIC═══" + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.UNDERLINE + "═══ITEMS═══" + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ".", item["item"].name + ":", item["item"].description,
                  " (x" + str(item["quantity"]) + ")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.UNDERLINE + "═══TARGET═══" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.hp != 0:
                print("        " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input(bcolors.BOLD + "-Choose a Target: " + bcolors.ENDC)) -1
        return choice


    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "/"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 13:
            decreased_hp = 13 - len(hp_string)

            while decreased_hp > 0:
                current_hp += " "
                decreased_hp -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print(bcolors.BOLD + self.name + " " +
                current_hp + "  |" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|")


    def get_stats(self):
        hp_bar = ""
        hp_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while hp_ticks > 0:
            hp_bar += "/"
            hp_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "/"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased_hp = 9 - len(hp_string)

            while decreased_hp > 0:
                current_hp += " "
                decreased_hp -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = " "

        if len(mp_string) < 9:
            decreased_mp = 9 - len(mp_string)

            while decreased_mp > 0:
                current_mp += " "
                decreased_mp -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

        print(bcolors.BOLD + self.name + "   " +
              current_hp + "  |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC +
              "| " + current_mp + "  |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_dmg()

        pct = self.hp / self.maxhp * 100

        if self.mp < spell.cost or spell.type == "white" and pct > 50:
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg
