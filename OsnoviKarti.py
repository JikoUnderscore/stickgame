#from pygame import *
from typing import Sequence, Tuple

from ENGINE import Igrac, Predmet, KARTA
from Postojanni import FONT15, MAP, EKRAN
from pygame import Rect, image, Surface, SRCALPHA
#from cuzdKod import CircularArc

# def spisyk_ot_linii(tocki):
#     def one_line(coordinates):
#         (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
#         for i in range(2, len(coordinates)):
#             x, y = coordinates[i]
#             if (x0 - x1) * (y1 - y) != (x1 - x) * (y0 - y1):
#                 return coordinates[:i - 1]
#         return coordinates
#
#     ednaLinija = one_line(tocki)
#     drugaLinija = [x for x in tocki if x not in ednaLinija]
#     try:
#         res = [[ednaLinija[0], ednaLinija[-1]], [drugaLinija[0], drugaLinija[-1]]]
#     except IndexError:
#         res = [[ednaLinija[0], ednaLinija[-1]],[]]
#     return res
# def lineLine(x1, y1, x2, y2, x3, y3, x4, y4):
#     # calculate the distance to intersection point
#     uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
#     uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
#
#     # if uA and uB are between 0-1, lines are colliding
#     if (uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1):
#
#     # optionally, draw a circle where the lines meet
#     # intersectionX = x1 + (uA * (x2-x1))
#     # intersectionY = y1 + (uA * (y2-y1))
#         return True
#     return False


iki = image.load('data/hisks.png').convert_alpha()
leftbotomright = image.load('data/zavoj.png').convert_alpha()
leftbotomtop = image.load('data/zavoj0.png').convert_alpha()
rightbotomleft = image.load('data/zavoj2.png').convert_alpha()
rightbotomtop = image.load('data/zavoj02.png').convert_alpha()
lefttopbotom = image.load('data/zavoj3.png').convert_alpha()
lefttopright = image.load('data/zavoj03.png').convert_alpha()
righttopleft = image.load('data/zavoj4.png').convert_alpha()
righttopbotom = image.load('data/zavoj04.png').convert_alpha()
botomlefttopright = image.load('data/severjug.png').convert_alpha()
botomrighttopleft = image.load('data/severjug2.png').convert_alpha()
botomuptopup = image.load('data/pravo2.png').convert_alpha()
leftleftrightright = image.load('data/pravo.png').convert_alpha()

cjalSjat = KARTA(ikonata='data/kartanasvetyt.png', kor_x=650, kor_y=62)
kovacestvo = KARTA('data/kovacc.png', ikonata='data/kovacestvo.png', kor_x=650, kor_y=283)
igracyt = Igrac('data/stik.png', 0, 0, (100, 100))
kymNacalo = Predmet('data/obratnoVnacaloto.png', 10, 500, syobstenie='Press E to GO back to the start')

karta1 = KARTA('data/karta1/zona1.png', mini_ikonka='data/karta1/minikarta1.png', mini_x=100, mini_y=100)
karta2 = KARTA('data/karta2/zona2.png', mini_ikonka='data/karta2/minikarta2.png', mini_x=400, mini_y=100)
grad = KARTA('data/grad/grad.png', mini_ikonka='data/grad/minigrad.png', mini_x=50, mini_y=400)
nacalo = KARTA('data/mainmenu.png', mini_ikonka='data/nimiObratnoVnacaloto.png', mini_x=420,mini_y=400)

miniZoni = [karta1, karta2, grad, nacalo]
miniKvadrati = [zona.miniHitbox for zona in miniZoni]

svetovnaKarta = image.load('data/svetovnakarta.png').convert()
maglivaKarta = image.load('data/svetovnakarta.png').convert()
mygla = Surface((EKRAN.get_width(), EKRAN.get_height()), flags=SRCALPHA).convert_alpha()
mygla.fill((35, 35, 35, 30))
back = Surface((EKRAN.get_width(), EKRAN.get_height()))
back.fill((0,0,0))

pyteka = [] + miniKvadrati
igInformacija = Surface((100, 20))
igInformacija.fill((255, 255, 0))
ig = Rect((401, 401), (19, 19))
fovig = Rect(ig.topleft, (21 * 3, 21 * 3))


def zona_v_maglata(spisyk: Sequence[Tuple[Surface, Rect]]):
    maglivaKarta.blits(spisyk, False)


zona_v_maglata([(zona.miniIkonka, zona.miniHitbox) for zona in miniZoni])


def narisyvaj_pytekata(ot_mini_zona_kvadrat, do_mini_zona_kvadrat):
    mx, my = do_mini_zona_kvadrat
    nac = list(ot_mini_zona_kvadrat.miniHitbox.topleft)
    pozoci = list((20 * (mx // 20), 20 * (my // 20)))
    print(nac, pozoci, nac == pozoci)
    while not nac == pozoci:
        plocax = [0, 0]
        plocay = [0, 0]

        if nac[0] < pozoci[0]:
            nac[0] += 20
            plocax[0] = 1
        elif nac[0] > pozoci[0]:
            nac[0] -= 20
            plocax[1] = 1

        if nac[1] < pozoci[1]:
            nac[1] += 20
            plocay[0] = 1
        elif nac[1] > pozoci[1]:
            nac[1] -= 20
            plocay[1] = 1
        # print('workin', nac)

        if plocax[0] and plocay[1]:
            if nac[0] == pozoci[0] and not nac[1] == pozoci[1]:
                ploca = leftbotomtop
            elif nac[1] == pozoci[1] and not nac[0] == pozoci[0]:
                ploca = leftbotomright
            else:
                ploca = botomlefttopright
        elif plocax[1] and plocay[0]:
            if nac[0] == pozoci[0] and not nac[1] == pozoci[1]:
                ploca = righttopbotom
            elif nac[1] == pozoci[1] and not nac[0] == pozoci[0]:
                ploca = righttopleft
            else:
                ploca = botomlefttopright
        elif plocax[1] and plocay[1]:
            if nac[0] == pozoci[0] and not nac[1] == pozoci[1]:
                ploca = rightbotomtop
            elif nac[1] == pozoci[1] and not nac[0] == pozoci[0]:
                ploca = rightbotomleft
            else:
                ploca = botomrighttopleft
        elif plocax[0] and plocay[0]:
            if nac[0] == pozoci[0] and not nac[1] == pozoci[1]:
                ploca = lefttopbotom
            elif nac[1] == pozoci[1] and not nac[0] == pozoci[0]:
                ploca = lefttopright
            else:
                ploca = botomrighttopleft
        elif plocax[0] or plocax[1]:
            ploca = leftleftrightright
        elif plocay[0] or plocay[1]:
            ploca = botomuptopup
        else:
            ploca = iki

        svetovnaKarta.blit(ploca, nac)
        #ploca.fill((35, 35, 35, 30))
        maglivaKarta.blit(ploca, nac)
        # print(ploca.get_size())
        kvt = Rect((nac[0] - 1, nac[1] - 1), ploca.get_size())
        pyteka.append(kvt)
        # p.append(kvt.center)
    print(nac, pozoci, nac == pozoci)


def energija_na_dvizene(posledna_zona):
    if igracyt.poCerenPyt <= 0:
        print('dead', posledna_zona)
        for k in MAP:
            MAP[k] = False
        MAP.update(posledna_zona[0])
        igracyt.poCerenPyt = 20
        nx, ny = posledna_zona[1][0]
        ig.x = nx+1
        ig.y = ny+1

        txt = FONT15.render(f' {igracyt.poCerenPyt:02d} ', False, (0, 0, 0), (255, 255, 255))
        igInformacija.blit(txt, (10, 0))
        back.blit(igInformacija, ((back.get_width() // 2) - igInformacija.get_width() // 2, 0))
    elif pyteka and not ig.collidelistall(pyteka):
        igracyt.poCerenPyt -= 1

        txt = FONT15.render(f' {igracyt.poCerenPyt:02d} ', False, (0, 0, 0), (255, 255, 255))
        igInformacija.blit(txt, (10, 0))
        back.blit(igInformacija, ((back.get_width() // 2) - igInformacija.get_width() // 2, 0))

