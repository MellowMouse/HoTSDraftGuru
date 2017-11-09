class DraftGuru:

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

    hero_list = [
        "abathur" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "alarak" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "ana" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "anubarak" = { "good_against" = [ "genji" ], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "Cocoon invaluable against heroes with extended ults, ex. genji dragonblade. completely nullifies it." },
        "artanis" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "arthas" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "auriel" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "azmodan" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "butcher" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "brightwing" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [ "warhead junction" ], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "Emerald wind strong on any map where you might need to contest boss. Can push back whole enemy team while your team finishes the boss." },
        "cassia" = { "good_against" = [ "illdan" ], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "Lots of blind + stutter step makes Cassia good against auto attackers. Avoidance can punish them too." },
        "chen" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "cho" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "chromie" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "dva" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "dehaka" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "diablo" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "etc" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "falstad" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "gall" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "garrosh" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "gazlowe" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "genji" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "greymane" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "guldan" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "illidan" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "jaina" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "johanna" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "junkrat" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "kaelthas" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "kelthuzad" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "kerrigan" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "kharazim" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "leoric" = { "good_against" = [ "sgt" ], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "Healing is strong against high hp tanks.\nCan dive sgt easily with ghost and force her to reposition, and can also entomb her." },
        "li-li" = { "good_against" = [ "butcher", "illidan" ], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "Blind is strong against all auto-attack heroes. Self healing plus blind and movespeed can help lead aggressive players on those heroes in to unfavorable situations." },
        "lt-morales" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "lucio" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "lunara" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "malfurion" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "malthael" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "medivh" = { "good_against" = [ "samuro", "rexxar", "kaelthas" ], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "Any hero with multiple heroes makes for good fast stacking of medivh's quest.\nProtect strong against high burst damage skills like pryroblast." },
        "muradin" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "murky" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "nazeebo" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "nova" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "probius" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "ragnaros" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "raynor" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "rehgar" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "rexxar" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "samuro" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "sgt" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "sonya" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "stitches" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "stukov" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "sylvanas" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "tassadar" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [ "tracer", "sonya", "butcher" ], "anti-synergy_with" = [], "Notes" = "Good synergy with any up-front or dive heroes" },
        "thrall" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "tracer" = { "good_against" = [ "chromie", "kelthuzad", "jaina" ], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "High mobility wrecks low mobility mages." },
        "tychus" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "tyrael" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "tyrande" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "uther" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "valeera" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "valla" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "varian" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "vikings" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "xul" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "zagara" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "zarya" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "zeratul" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" },
        "zuljin" = { "good_against" = [], "bad_against" = [], "good_battlefields" = [], "bad_battlefields" = [], "synergy_with" = [], "anti-synergy_with" = [], "Notes" = "" }
    ]

    # For calculation purposes every hero should have the following qualities
    # list of heroes it is "good" against
    # list of heroes it is "bad" against
    # list of battlefields is is "good" on
    # list of battlefields it is "bad" on
    # list of heroes it has synergy with
    # list of heroes it has anti-synergy with

    def __init__(self):
        print("This is the init function.")
        # Calculate the scores for all heroes in hero_list OR at least initialize the internal qualities of each hero such that their scores can be calculated in the list_* methods
        # Also performs the lazy function:
        #     If a for a hero, add their name to the bad_against list of every hero that is in their "good_against"
        #     This is 100% to make up for me being lazy and not writing every hero twice in this thing. but it follows - if I A is good against B, then B is necessarily bad against A. I think.

    def list_recommended_heroes(self):
        print("These heroes are recommended")
        # a hero is recommended IF
        # it is not "bad" against any heroes on the opposing team
        # AND
        # it is not "bad" on the battlefield
        # AND
        # it does not have anti-synergy with any allied hero
        #
        # From the remaining heroes, a hero is recommended IF
        # it is "good" against any hero on the opposing team
        # OR
        # it is "good" on the battlefield
        # OR
        # it has synergy with a hero on the allied team

    def list_non_recommended_heroes(self):
        print("These heroes are not recommended")
        # a hero is non-recommended IF
        # it is not "good" against any heroes on the opposing team
        # AND
        # it is not "good" on the battlefield
        # AND
        # it does not have synergy with any allied hero
        #
        # From the remaining heroes, a hero is non-recommended IF
        # it is "bad" against any hero on the opposing team
        # OR
        # it is "bad" on the battlefield
        # OR
        # it has anti-synergy with a hero on the allied team

    def list_controversial_heroes(self):
        print("These heroes are controversial")
        # a hero is controversial if
        # ( it is "good" against any hero on the opposing team OR it is "good" on the battlefield OR it has synergy with a hero on the allied team )
        # AND
        # ( it is "bad" against any hero on the opposing team OR it is "bad" on the battlefield OR it has anti-synergy with a hero on the allied team)

    def list_neutral_heroes(self):
        print("These heroes are neutral")
        # it has no good/bad relationship with any of the heroes selected so far AND it has no good/bad relationship with the battlefield

