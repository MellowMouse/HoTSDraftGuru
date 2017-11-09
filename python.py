#!/usr/bin/python
import argparse

class DraftGuru:

    allies = []
    enemies = []
    battlefield = ""

    battlefields = [
        "volskaya foundry", # medium, many extended fights around control points
        "hanamura", #meh. gon let them rebuild
        "haunted mines", #small, many extended fights in underground. camp clear INVALUABLE.
        "towers of doom", #big, many extended fights. high dps good for applying tower pressure. camp clear also very valuable
        "infernal shrines", #big, many minions to kill == waveclear desired
        "battlefield of eternity", # small. MANY extended fights. high dps usefull on obj
        "tomb of the spider queen", #many minions
        "sky temple", #big, extended battles / point control
        "garden of terror", # big, extended battles at night. has bosses
        "blackhearts bay", #big, extended battles around chest / point control
        "dragon shire", # medium, but lots of back and forth required during shrines
        "cursed hollow", #big, many group fights / point control
        "braxis holdout", #small, many group fights around points. many minions to kill = waveclear desired
        "warhead junction", #big, some extended fights / point control. has bosses
    ]

    hero_list = {
        "abathur": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "alarak": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "ana": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "anubarak": { "good_against": [ "genji" ], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "Cocoon invaluable against heroes with extended ults, ex. genji dragonblade. completely nullifies it.\n", "bad_notes": "" },
        "artanis": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "arthas": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "auriel": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "azmodan": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "butcher": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "brightwing": { "good_against": [], "bad_against": [], "good_battlefields": [ "warhead junction" ], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "Emerald wind strong on any map where you might need to contest boss. Can push back whole enemy team while your team finishes the boss.\n", "bad_notes": "" },
        "cassia": { "good_against": [ "illidan" ], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "Lots of blind + stutter step makes Cassia good against auto attackers. Avoidance can punish them too.\n", "bad_notes": "" },
        "chen": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "cho": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "chromie": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "dva": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "dehaka": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "diablo": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "etc": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "falstad": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "gall": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "garrosh": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "gazlowe": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "genji": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "greymane": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "guldan": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "illidan": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "Illidan is weak against opponents with blinds.\nIllidan is weak against opponents with CC's." },
        "jaina": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "johanna": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "junkrat": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "kaelthas": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "kelthuzad": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "kerrigan": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "kharazim": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "leoric": { "good_against": [ "sgt" ], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "Healing is strong against high hp tanks.\nCan dive sgt easily with ghost and force her to reposition, and can also entomb her.\n", "bad_notes": "" },
        "li-li": { "good_against": [ "butcher", "illidan" ], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "Blind is strong against all auto-attack heroes. Self healing plus blind and movespeed can help lead aggressive players on those heroes in to unfavorable situations.\n", "bad_notes": "" },
        "lt-morales": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "lucio": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "lunara": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "malfurion": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "malthael": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "medivh": { "good_against": [ "samuro", "rexxar", "kaelthas" ], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "Any hero with multiple heroes makes for good fast stacking of medivh's quest.\nProtect strong against high burst damage skills like pryroblast.\n", "bad_notes": "" },
        "muradin": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "murky": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "nazeebo": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "nova": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "probius": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "ragnaros": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "raynor": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "rehgar": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "rexxar": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "samuro": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "sgt": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "sonya": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "stitches": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "stukov": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "sylvanas": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "tassadar": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [ "tracer", "sonya", "butcher" ], "anti-synergy_with": [], "good_notes": "Good synergy with any up-front or dive heroes\n", "bad_notes": "" },
        "thrall": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "tracer": { "good_against": [ "chromie", "kelthuzad", "jaina" ], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "High mobility wrecks low mobility mages.\n", "bad_notes": "" },
        "tychus": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "tyrael": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "tyrande": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "uther": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "valeera": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "valla": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "varian": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "vikings": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "xul": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "zagara": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "zarya": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "zeratul": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" },
        "zuljin": { "good_against": [], "bad_against": [], "good_battlefields": [], "bad_battlefields": [], "synergy_with": [], "anti-synergy_with": [], "good_notes": "\n", "bad_notes": "" }
    }

    # For calculation purposes every hero should have the following qualities
    # list of heroes it is "good" against
    # list of heroes it is "bad" against
    # list of battlefields is is "good" on
    # list of battlefields it is "bad" on
    # list of heroes it has synergy with
    # list of heroes it has anti-synergy with

    def __init__(self, allies, enemies, battlefield):
        self.allies = allies
        self.enemies = enemies
        self.battlefield = battlefield

        # Also performs the lazy function:
        #     For every hero, add their name to the bad_against list of every hero that is in their "good_against"
        #     This is 100% to make up for me being lazy and not writing every hero twice in this thing. but it follows - if I A is good against B, then B is necessarily bad against A. I think.
        for hero in self.hero_list:
            for a in self.hero_list[hero]["good_against"]:
                if hero not in self.hero_list[a]["bad_against"]:
                    self.hero_list[a]["bad_against"].append(hero)

    def list_recommended_heroes(self):
        all_heroes = self.hero_list.keys()
        recommended_heroes = []

        # A hero is recommended IF
        for hero in all_heroes:

            # it is "good" against any hero on the opposing team
            for enemy in self.enemies:
                if enemy in self.hero_list[hero]["good_against"]:
                    recommended_heroes.append(hero)

            # it is "good" on the battlefield
            if self.battlefield in self.hero_list[hero]["good_battlefields"]:
                recommended_heroes.append(hero)

            # it has synergy with a hero on the allied team
            for ally in self.allies:
                if ally in self.hero_list[hero]["synergy_with"]:
                    recommended_heroes.append(hero)

        return recommended_heroes

    def list_non_recommended_heroes(self):

        all_heroes = self.hero_list.keys()
        non_recommended_heroes = []

        # A hero is non-recommended IF
        for hero in all_heroes:

            # it is "bad" against any hero on the opposing team
            for enemy in self.enemies:
                if enemy in self.hero_list[hero]["bad_against"]:
                    non_recommended_heroes.append(hero)

            # it is "bad" on the battlefield
            if self.battlefield in self.hero_list[hero]["bad_battlefields"]:
                non_recommended_heroes.append(hero)

            # it has anti-synergy with a hero on the allied team
            for ally in self.allies:
                if ally in self.hero_list[hero]["anti-synergy_with"]:
                    non_recommended_heroes.append(hero)

        return non_recommended_heroes

    def list_controversial_heroes(self):
        all_heroes = self.hero_list.keys()
        controversial_heroes = []

        good_heroes = self.list_recommended_heroes()
        bad_heroes = self.list_non_recommended_heroes()

        for hero in all_heroes:
            if hero in good_heroes and hero in bad_heroes:
                controversial_heroes.append(hero)

        return controversial_heroes


    def list_neutral_heroes(self):
        all_heroes = self.hero_list.keys()
        neutral_heroes = []

        good_heroes = self.list_recommended_heroes()
        bad_heroes = self.list_non_recommended_heroes()

        for hero in all_heroes:
            if hero not in good_heroes and hero not in bad_heroes:
                neutral_heroes.append(hero)

        return neutral_heroes

    def report(self):

        good_heroes = self.list_recommended_heroes()
        bad_heroes = self.list_non_recommended_heroes()
        controversial_heroes = self.list_controversial_heroes()
        neutral_heroes = self.list_neutral_heroes()

        for hero in controversial_heroes:
            if hero in good_heroes:
                good_heroes.remove(hero)
            if hero in bad_heroes:
                bad_heroes.remove(hero)

        print ( "PICK THESE HEROES:" )
        for hero in good_heroes:
            print ( "{}:\n{}\n".format(hero, self.hero_list[hero]["good_notes"]) )

        print ( "DONT PICK THESE HEROES:" )
        for hero in bad_heroes:
            print ( "{}:\n{}\n".format(hero, self.hero_list[hero]["bad_notes"]) )

        print ( "CONTROVERSIAL HEROES:" )
        for hero in controversial_heroes:
            print ( "{}:\n{}\n".format(hero, self.hero_list[hero]["good_notes"]) )
            print ( "{}:\n{}\n".format(hero, self.hero_list[hero]["bad_notes"]) )

        print ( "PICK THESE HEROES IF YOU LIKE THEM:" )
        for hero in neutral_heroes:
            print ( "{}".format(hero) )

if __name__ == '__main__':
    try:
        print("\n")

        parser = argparse.ArgumentParser()
        parser.add_argument( "-e", "--enemies", type=str, default=None, help="comma-separated list of heroes picked by the enemy team, Ex: genji,cassia,samuro,azmodan,sonya" )
        parser.add_argument( "-a", "--allies", type=str, default=None, help="comma-separated list of heroes picked by the allied team, Ex: tracer,morales,anubarak,leoric,lucio" )
        parser.add_argument( "-b", "--battlefield", type=str, choices=DraftGuru.battlefields, default=None, help="quote-enclosed name of the battlefield you are playing on, Ex: \"battlefield of eternity\"" )

        args = parser.parse_args()

        if args.allies == None or args.enemies == None or args.battlefield == None:
            print ( "You are missing parameters. Please run \"python python.rb --help\" for usage information." )

        print ( "ALLIED HEROES:\n{}\n".format(args.allies.replace(",", "\n")) )
        print ( "ENEMY HEROES:\n{}\n".format(args.enemies.replace(",", "\n")) )
        print ( "BATTLEFIELD: {}\n".format(args.battlefield ) )

        drafty = DraftGuru( args.allies.split(","), args.enemies.split(","), args.battlefield )
        drafty.report()

    except Exception as e:
        print( "Main function caught error: {}".format(e) )
