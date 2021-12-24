import random

class Kingdom():
    def Generate_kingdom_location(self):
        #home = {"type":"home","leve":0,"maxleve":3}
        #ferm = {"type": "ferm", "leve": 0,"maxleve":2,"drop":5}
        #forest = {"type": "forest", "occup":False}
        #stoneBlock = {"type": "stoneblock", "occup":False}
        #ore = {"type": "ore", "occup":False}
        #terra = {"type": "terra","occup":False}
        #types = []
#
        #types.append(home)
        #types.append(ferm)
        #types.append(forest)
        #types.append(stoneBlock)
        #types.append(ore)
#
        #grand = []
        #grand.append(home)
        #grand.append(ferm)
        #grand.append(stoneBlock)
        #for i in range(10):
        #    if random.randint(0,100) > 70:
        #        grand.append(types[random.randint(0,len(types)-1)])
        #    else:
        #        grand.append(terra)
        grand = {"ferm":0,
                 "home":1,
                 "forest":1,
                 "stoneBlock":1,
                 "ore":0,
                 "terra":0,
                 }
        for i in range(7):
            if random.randint(0,100) > 70:
                grand[random.choice(list(grand.keys()))] += 1
            else:
                grand["terra"] += 1
        grand.update({"market": 0,
                      "stonequarry": 0,
                      "orequarry": 0,
                      "woodcutter": 0,
                      "forge": 0})

        return grand

    def RandombBlock(self):
        grand = {"ferm": 0, "home": 1, "forest": 1, "stoneBlock": 1, "ore": 0, "terra": 0}
        return random.choice(list(grand.keys()))




kingd = Kingdom()

gr = kingd.Generate_kingdom_location()
print(gr)