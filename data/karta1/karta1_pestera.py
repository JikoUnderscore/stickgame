from ENGINE import KARTA, Predmet, ObektDrug

def obekt_syzdatel_v_pesterata():

    karta1Pestera = KARTA('data/karta1/cave1.png')
    karta1PesteraIzhod1 = Predmet('data/karta1/cave_enter.png', 0, 150, syobstenie='Press E to EXIT the cave')
    prijatel11 = ObektDrug('data/mobs/NPC0/prijatel1.png', 1080, 200)

    return karta1Pestera, karta1PesteraIzhod1, prijatel11
