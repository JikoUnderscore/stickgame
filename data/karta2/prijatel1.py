from ENGINE import ObektDrug
from Oborudvane import Item

def npc_syzdatel():
    #import pympler.asizeof as razmer

    kupiMec1 = Item('Sword', 'Golden Sword', 50, 'data/ikonki/sabja.png',9,attack=9, HP=9, dodge=9,cooldown=5)
    kupiMec2 = Item('Sword', 'Silver Sword', 50, 'data/ikonki/sabja.png',9, attack=5, HP=5, dodge=5, cooldown=7)
    kupiMec3 = Item('Sword', 'Bronze Sword', 50, 'data/ikonki/sabja.png',9, attack=3, HP=3, dodge=3, cooldown=9)

    prodavac = ObektDrug('data/mobs/NPC0/prijatel1.png', 700, 240, 'data/mobs/NPC0/prodavacrazgovor.json', ime="Joe the Salesman")
    prodavac.neiskam = ('golden sword', 'silver sword', 'bronze sword')
    prodavac.sak['golden sword'] = kupiMec1
    prodavac.sak['silver sword'] = kupiMec2
    prodavac.sak['bronze sword'] = kupiMec3
    prodavac.ime = "Joe the Salesman"

    raz1 = ObektDrug('data/mobs/NPC1/prijatelNPC1.png', 1000, 300, 'data/mobs/NPC1/nepop_vid1.json', ime="talk-a-lot selse man")
    raz2 = ObektDrug('data/mobs/NPC2/prijatelNPC2.png', 1500, 400, 'data/mobs/NPC2/nepopp_vid2.json', ime="TEST vid 2")

   # print(razmer.asizesof(kupiMec1, kupiMec2, kupiMec3))
   # print(razmer.asizeof(kupiMec1, kupiMec2, kupiMec3))

    return prodavac, raz1, raz2
