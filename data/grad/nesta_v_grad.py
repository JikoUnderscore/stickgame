from ENGINE import Predmet
def syzdaj_sgradi():
    zgrada1 = Predmet('data/grad/zgrada1.png', 800, 20, (90,100), (380,740))
    zgrada2 = Predmet('data/grad/zgrada2.png', 1600, 20, (90, 100), (380,740))
    zgrada3 = Predmet('data/grad/zgrada3.png', 2200, 20,  (90, 100), (380,740))
    zgrada4 = Predmet('data/grad/zgrada4.png', 2900, 20, (90, 100), (330,790))

    return zgrada1, zgrada2, zgrada3, zgrada4
