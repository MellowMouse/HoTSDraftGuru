class DraftGuru:


    hero_list = [
        "abathur",
        "alarak",
        "ana",
        "anubarak",
        "artanis",
        "arthas",
        "auriel",
        "azmodan",
        "brightwing",
        "cassia",
        "chen",
        "cho",
        "chromie",
        "dva",
        "dehaka",
        "diablo",
        "etc",
        "falstad",
        "gall",
        "garrosh",
        "gazlowe",
        "genji",
        "greymane",
        "guldan",
        "illidan",
        "jaina",
        "johanna",
        "junkrat",
        "kaelthas",
        "kelthuzad",
        "kerrigan",
        "kharazim",
        "leoric",
        "li-li",
        "lt-morales",
        "lucio",
        "lunara",
        "malfurion",
        "malthael",
        "medivh",
        "muradin",
        "murky",
        "nazeebo",
        "nova",
        "probius",
        "ragnaros",
        "raynor",
        "rehgar",
        "rexxar",
        "samuro",
        "sgt",
        "sonya",
        "stitches",
        "stukov",
        "sylvanas",
        "tassadar",
        "the",
        "the",
        "thrall",
        "tracer",
        "tychus",
        "tyrael",
        "tyrande",
        "uther",
        "valeera",
        "valla",
        "varian",
        "xul",
        "zagara",
        "zarya",
        "zeratul",
        "zuljin"
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

