from pygame import *

init()
from Postojanni import MAP, poslednaZona, dvizenie, EKRAN, FPS, FONT35, nastojastaZona
from Cuzd import fpsint, newRender
from OsnoviKarti import kovacestvo, cjalSjat, igracyt, kymNacalo
from OsnoviKarti import ig, maglivaKarta, fovig, mygla, svetovnaKarta, energija_na_dvizene, miniKvadrati, \
    narisyvaj_pytekata, back, zona_v_maglata
from OsnoviKarti import nacalo, grad, karta1, karta2
# from ENGINE import FONT35
# from poluMojKod import Item, Container

from VsiOborudvane import *
from Oborudvane import sakk


def test():
    sakk.add(mec)
    sakk.add(mec1)
    sakk.add(bradva)
    sakk.add(t1)
    sakk.add(t2)
    sakk.add(t3)
    sakk.add(t4)
    sakk.add(t5)
    sakk.add(t6)
    sakk.add(t7)
    sakk.add(t8)
    sakk.add(t9)
    sakk.add(sapk)
    sakk.add(boot)
    sakk.add(h1)
    sakk.add(h2)
    sakk.add(h3)
    sakk.add(h4)
    sakk.add(h5)
    sakk.add(sh1)
    sakk.add(w)
    sakk.add(sh2)
    sakk.add(sh3)
    sakk.add(sh4)
    sakk.add(sh5)
    sakk.add(p1)
    sakk.add(p2)
    sakk.add(p3)
    sakk.add(p4)
    sakk.add(p5)
    sakk.add(r1)
    sakk.add(r2)
    sakk.add(r3)
    sakk.add(r4)
    sakk.add(r5)
    sakk.add(r6)
    sakk.add(r7)
    sakk.add(r8)
    sakk.add(r9)
    sakk.add(r10)
    sakk.add(hp4)
    sakk.add(hp1)
    sakk.add(hp5)
    sakk.add(hp2)
    sakk.add(hp3)
    sakk.add(dm1)
    sakk.add(dm2)
    sakk.add(dm3)
    sakk.add(dm4)
    sakk.add(dm5)
    sakk.add(testpredmet)


def camp():
    # EKRAN.blit(nacalo, (0, 0))
    nacalo.risuvaj_zonata()
    cjalSjat.ikona_markitana('svetovna')
    kovacestvo.ikona_markitana('kovane')


def kovane():
    kovacestvo.risuvaj_zonata()
    igracyt.kovane_predmeti(e)


def svetovna():
    global cisloZaPremigvane
    fovig.center = ig.center
    # maglivaKarta = svetovnaKarta.copy()
    # # fog.blit(mist, (0, 0))  # , special_flags=BLEND_MULT
    #
    # fog.blit(svetovnaKarta, fovig.topleft, fovig)
    # EKRAN.blit(fog, (0, 0))
    # #draw.rect(EKRAN, (0, 255, 0), fovig, 2)

    maglivaKarta.blit(mygla, (0, 0))

    back.blit(maglivaKarta, fovig.topleft, fovig)
    EKRAN.blit(back, (0, 0))
    EKRAN.blit(svetovnaKarta, fovig.topleft, fovig)

    if ig.collidelistall(miniKvadrati):  # kartaKvadra.colliderect(ig):
        if cisloZaPremigvane <= 30:
            draw.rect(EKRAN, (255, 0, 0), ig)
        elif cisloZaPremigvane == 60:
            cisloZaPremigvane = 0
        cisloZaPremigvane += 1
    else:
        draw.rect(EKRAN, (255, 0, 0), ig)

    if e.type == MOUSEBUTTONUP and e.button == 1:
        narisyvaj_pytekata(nacalo, mouse.get_pos())

    karta1.mini_ikonka_markirana('Pig Cave', svetovnaKarta, igracyt, ig)
    karta2.mini_ikonka_markirana('Market place', svetovnaKarta, igracyt, ig)
    grad.mini_ikonka_markirana('Westvield City', svetovnaKarta, igracyt, ig)
    nacalo.mini_ikonka_markirana('Camp', svetovnaKarta, igracyt, ig)

    if e.type == KEYUP:
        if e.key == K_w and ig.y > 21:
            ig.y -= 20
            energija_na_dvizene(poslednaZona)
        elif e.key == K_s and ig.y < 681:
            ig.y += 20
            energija_na_dvizene(poslednaZona)
        elif e.key == K_a and ig.x > 21:
            ig.x -= 20
            energija_na_dvizene(poslednaZona)
        elif e.key == K_d and ig.x < 1041:
            ig.x += 20
            energija_na_dvizene(poslednaZona)


def pig_cave():
    global theload
    if theload:
        global karta1PesteraVhod, kamyk, lyc, prijatel1, vrag1, vragelit, vragoficer, vragboss
        from data.karta1 import obekt_syzdatel

        print('loading')
        karta1PesteraVhod, kamyk, lyc, prijatel1, vrag1, vragelit, vragoficer, vragboss = obekt_syzdatel()
        theload = 0

    karta1.risuvaj_zonata()
    lyc.draw(EKRAN)
    karta1PesteraVhod.narisuvane()

    kymNacalo.narisuvane()

    if igracyt.hitbox.bottom > vrag1.hitbox.bottom and igracyt.hitbox.bottom > prijatel1.hitbox.bottom:
        if not prijatel1.kljuc1:
            vrag1.narisuvane()
        else:
            prijatel1.narisuvane()
        igracyt.narisuvane()
        kamyk.narisuvane()
    elif vrag1.hitbox.bottom > igracyt.hitbox.bottom > prijatel1.hitbox.bottom and igracyt.hitbox.bottom <= kamyk.hitbox.bottom:
        if prijatel1.kljuc1:
            prijatel1.narisuvane()
        igracyt.narisuvane()
        kamyk.narisuvane()
        if not prijatel1.kljuc1:
            vrag1.narisuvane()
    elif vrag1.hitbox.bottom > igracyt.hitbox.bottom > prijatel1.hitbox.bottom and igracyt.hitbox.bottom >= kamyk.hitbox.bottom:
        if prijatel1.kljuc1:
            prijatel1.narisuvane()
        kamyk.narisuvane()
        igracyt.narisuvane()
        if not prijatel1.kljuc1:
            vrag1.narisuvane()
    elif igracyt.hitbox.bottom <= vrag1.hitbox.bottom and igracyt.hitbox.bottom <= prijatel1.hitbox.bottom:
        if not prijatel1.kljuc1:
            vrag1.narisuvane()
        igracyt.narisuvane()
        kamyk.narisuvane()
        if prijatel1.kljuc1:
            prijatel1.narisuvane()

    kamyk.push(igracyt)

    if lyc.contains(igracyt.hitbox.bottomright[0], igracyt.hitbox.bottomright[1]):
        igracyt.hitbox.x -= 10
        igracyt.hitbox.y += 10
    igracyt.dvizenie(ljavo=-50, djasno=100)

    vragelit.narisuvane()
    vragelit.vrazduvane(igracyt, '1')
    vragoficer.narisuvane()
    vragoficer.vrazduvane(igracyt, '20')
    vragboss.narisuvane()
    vragboss.vrazduvane(igracyt, 'B')

    if not prijatel1.kljuc1:
        vrag1.vrazduvane(igracyt)
    else:
        prijatel1.razgovarjane(igracyt, e)

    # karta1PesteraVhod.udareno_boxx(igracyt, 'Press E to ENTER the cave')
    if karta1PesteraVhod.hitbox.colliderect(igracyt.hitbox):
        karta1PesteraVhod.naris_msgbox()
        if key.get_pressed()[K_e]:
            del karta1PesteraVhod, kamyk, lyc, prijatel1, vrag1, vragelit, vragoficer, vragboss
            for k in MAP:
                MAP[k] = False
            MAP['Pig Cave.pestera'] = True
            nastojastaZona.clear()
            nastojastaZona.append('Pig Cave.pestera')
            theload = 1
    # kymNacalo.udareno_boxx(igracyt, 'Press E to go back to start')
    if kymNacalo.hitbox.colliderect(igracyt.hitbox):
        kymNacalo.naris_msgbox()
        if key.get_pressed()[K_e]:
            del karta1PesteraVhod, kamyk, lyc, prijatel1, vrag1, vragelit, vragoficer, vragboss
            poslednaZona[0].clear()
            poslednaZona[1].clear()
            poslednaZona[0]['Pig Cave'] = True
            poslednaZona[1].append(karta1.miniHitbox.topleft)
            for k in MAP:
                MAP[k] = False
            MAP['svetovna'] = True
            nastojastaZona.clear()
            nastojastaZona.append('svetovna')
            theload = 1


def pig_cave_pestera():
    global theload
    if theload:
        global karta1Pestera, karta1PesteraIzhod1, prijatel11
        print('loading')
        from data.karta1 import obekt_syzdatel_v_pesterata
        karta1Pestera, karta1PesteraIzhod1, prijatel11 = obekt_syzdatel_v_pesterata()

        theload = 0

    karta1Pestera.risuvaj_zonata(True)
    karta1PesteraIzhod1.narisuvane()

    # print(igracyt.playerPosX, igracyt.hitbox.x, prijatel11.hitbox.x)
    if igracyt.hitbox.x >= 525 and igracyt.playerPosX >= 1080 and prijatel11.hitbox.x >= 0 or 600 >= prijatel11.hitbox.x >= 0:
        prijatel11.hitbox.x += -5
        prijatel11.spusyk_pestera(True)
    if prijatel11.hitbox.x >= 0:
        prijatel11.narisuvane()

    # print(, dvizenie[0])

    igracyt.narisuvane()
    igracyt.dvizenie(True, 1, None, 350, 100, 260)

    # karta1PesteraIzhod1.udareno_boxx(igracyt, 'Press E to EXIT the cave')
    if karta1PesteraIzhod1.hitbox.colliderect(igracyt.hitbox):
        karta1PesteraIzhod1.naris_msgbox()
        if key.get_pressed()[K_e]:
            del karta1Pestera, karta1PesteraIzhod1, prijatel11

            for k in MAP:
                MAP[k] = False
            MAP['Pig Cave'] = True
            nastojastaZona.clear()
            nastojastaZona.append('Pig Cave')
            theload = 1


def market_place():
    global theload
    if theload:
        global prodavac, raz1, raz2
        print('loading')
        from data.karta2 import npc_syzdatel
        prodavac, raz1, raz2 = npc_syzdatel()

        theload = 0

    karta2.risuvaj_zonata(True)
    kymNacalo.narisuvane()

    prodavac.narisuvane()
    raz1.narisuvane()
    raz2.narisuvane()

    igracyt.narisuvane()
    igracyt.dvizenie(True, 1, (-10, 100), 0, 20, 350)

    if igracyt.hitbox.bottom <= 410 and igracyt.hitbox.x >= 535 and igracyt.playerPosX >= 10:
        igracyt.hitbox.bottom = 410

    prodavac.hitbox.x += dvizenie[0]
    raz1.hitbox.x += dvizenie[0]
    raz2.hitbox.x += dvizenie[0]
    kymNacalo.hitbox.x += dvizenie[0]

    prodavac.razgovarjane(igracyt, e)
    raz1.razgovarjane(igracyt, e)
    raz2.razgovarjane(igracyt, e)

    # kymNacalo.udareno_boxx(igracyt, 'Press E to go bat to start')
    if kymNacalo.hitbox.colliderect(igracyt.hitbox):
        kymNacalo.naris_msgbox()
        if key.get_pressed()[K_e]:
            print('exiting')
            del prodavac, raz1, raz2
            poslednaZona[0].clear()
            poslednaZona[1].clear()
            poslednaZona[0]['Market place'] = True
            poslednaZona[1].append(karta2.miniHitbox.topleft)
            for k in MAP:
                MAP[k] = False
            MAP['svetovna'] = True
            nastojastaZona.clear()
            nastojastaZona.append('svetovna')
            theload = 1


def westvield_city():
    global theload
    if theload:
        global zgrada1, zgrada2, zgrada3, zgrada4
        print('loading')
        from data.grad import syzdaj_sgradi
        zgrada1, zgrada2, zgrada3, zgrada4 = syzdaj_sgradi()
        theload = 0

    grad.risuvaj_zonata(True)
    zgrada1.narisuvane()
    zgrada2.narisuvane()
    zgrada3.narisuvane()
    zgrada4.narisuvane()

    igracyt.narisuvane()
    igracyt.dvizenie(True, 4, gore=520, djasno=50)

    zgrada1.auto_boxx(igracyt)

    zgrada1.hitbox.x += dvizenie[0]
    zgrada2.hitbox.x += dvizenie[0]
    zgrada3.hitbox.x += dvizenie[0]
    zgrada4.hitbox.x += dvizenie[0]
    kymNacalo.hitbox.x += dvizenie[0]
    kymNacalo.narisuvane()
    if kymNacalo.hitbox.colliderect(igracyt.hitbox):
        kymNacalo.naris_msgbox()
        if key.get_pressed()[K_e]:
            del zgrada1, zgrada2, zgrada3, zgrada4
            poslednaZona[0].clear()
            poslednaZona[1].clear()
            poslednaZona[0]['Westvield City'] = True
            poslednaZona[1].append(grad.miniHitbox.topleft)
            for k in MAP:
                MAP[k] = False
            MAP['svetovna'] = True
            nastojastaZona.clear()
            nastojastaZona.append('svetovna')
            theload = 1


mpaFuncs = {
    'Camp': camp,
    'svetovna': svetovna,
    'kovane': kovane,
    'Pig Cave': pig_cave,
    'Pig Cave.pestera': pig_cave_pestera,
    'Market place': market_place,
    'Westvield City': westvield_city
}

if __name__ == '__main__':
    theload = 1
    # nacalo = image.load('data/mainmenu.png').convert()
    CLOCK = time.Clock()
    cisloZaPremigvane = 0
    run = True

    while run:
        CLOCK.tick(FPS)
        e = event.poll()
        if e.type == QUIT:
            run = not run
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                test()

        if MAP[nastojastaZona[0]]:
            mpaFuncs[nastojastaZona[0]]()

        # if MAP['Camp']:
        #     #EKRAN.blit(nacalo, (0, 0))
        #     nacalo.risuvaj_zonata()
        #     cjalSjat.ikona_markitana('svetovna')
        #     kovacestvo.ikona_markitana('kovane')
        # elif MAP['kovane']:
        #     kovacestvo.risuvaj_zonata()
        #     igracyt.kovane_predmeti(e)
        # elif MAP['svetovna']:
        #     fovig.center = ig.center
        #     #maglivaKarta = svetovnaKarta.copy()
        #     # # fog.blit(mist, (0, 0))  # , special_flags=BLEND_MULT
        #     #
        #     # fog.blit(svetovnaKarta, fovig.topleft, fovig)
        #     # EKRAN.blit(fog, (0, 0))
        #     # #draw.rect(EKRAN, (0, 255, 0), fovig, 2)
        #
        #     maglivaKarta.blit(mygla, (0, 0))
        #
        #     back.blit(maglivaKarta, fovig.topleft, fovig)
        #     EKRAN.blit(back, (0,0))
        #     EKRAN.blit(svetovnaKarta, fovig.topleft, fovig)
        #
        #
        #     if ig.collidelistall(miniKvadrati):  #kartaKvadra.colliderect(ig):
        #         if cisloZaPremigvane <= 30:
        #             draw.rect(EKRAN, (255, 0, 0), ig)
        #         elif cisloZaPremigvane == 60:
        #             cisloZaPremigvane = 0
        #         cisloZaPremigvane += 1
        #     else:
        #         draw.rect(EKRAN, (255, 0, 0), ig)
        #
        #     if e.type == MOUSEBUTTONUP and e.button == 1:
        #         narisyvaj_pytekata(nacalo, mouse.get_pos())
        #
        #
        #
        #
        #     karta1.mini_ikonka_markirana('Pig Cave', svetovnaKarta, igracyt, ig)
        #     karta2.mini_ikonka_markirana('Market place', svetovnaKarta, igracyt, ig)
        #     grad.mini_ikonka_markirana('Westvield City', svetovnaKarta, igracyt, ig)
        #     nacalo.mini_ikonka_markirana('Camp', svetovnaKarta, igracyt, ig)
        #
        #     if e.type == KEYUP:
        #         if e.key == K_w and ig.y > 21:
        #             ig.y -= 20
        #             energija_na_dvizene(poslednaZona)
        #         elif e.key == K_s and ig.y < 681:
        #             ig.y += 20
        #             energija_na_dvizene(poslednaZona)
        #         elif e.key == K_a and ig.x > 21:
        #             ig.x -= 20
        #             energija_na_dvizene(poslednaZona)
        #         elif e.key == K_d and ig.x < 1041:
        #             ig.x += 20
        #             energija_na_dvizene(poslednaZona)
        # elif MAP['Pig Cave']:
        #     if theload:
        #         from data.karta1 import obekt_syzdatel
        #
        #         print('loading')
        #         karta1PesteraVhod, kamyk, lyc, prijatel1, vrag1, vragelit, vragoficer, vragboss = obekt_syzdatel()
        #         theload = 0
        #
        #     karta1.risuvaj_zonata()
        #     lyc.draw(EKRAN)
        #     karta1PesteraVhod.narisuvane()
        #
        #     kymNacalo.narisuvane()
        #
        #
        #
        #
        #     if igracyt.hitbox.bottom > vrag1.hitbox.bottom and igracyt.hitbox.bottom > prijatel1.hitbox.bottom:
        #         if not prijatel1.kljuc1:
        #             vrag1.narisuvane()
        #         else:
        #             prijatel1.narisuvane()
        #         igracyt.narisuvane()
        #         kamyk.narisuvane()
        #     elif igracyt.hitbox.bottom < vrag1.hitbox.bottom and igracyt.hitbox.bottom > prijatel1.hitbox.bottom and igracyt.hitbox.bottom <= kamyk.hitbox.bottom:
        #         if prijatel1.kljuc1:
        #             prijatel1.narisuvane()
        #         igracyt.narisuvane()
        #         kamyk.narisuvane()
        #         if not prijatel1.kljuc1:
        #             vrag1.narisuvane()
        #     elif igracyt.hitbox.bottom < vrag1.hitbox.bottom and igracyt.hitbox.bottom > prijatel1.hitbox.bottom and igracyt.hitbox.bottom >= kamyk.hitbox.bottom:
        #         if prijatel1.kljuc1:
        #             prijatel1.narisuvane()
        #         kamyk.narisuvane()
        #         igracyt.narisuvane()
        #         if not prijatel1.kljuc1:
        #             vrag1.narisuvane()
        #     elif igracyt.hitbox.bottom <= vrag1.hitbox.bottom and igracyt.hitbox.bottom <= prijatel1.hitbox.bottom:
        #         if not prijatel1.kljuc1:
        #             vrag1.narisuvane()
        #         igracyt.narisuvane()
        #         kamyk.narisuvane()
        #         if prijatel1.kljuc1:
        #             prijatel1.narisuvane()
        #
        #     kamyk.push(igracyt)
        #
        #     if lyc.contains(igracyt.hitbox.bottomright[0], igracyt.hitbox.bottomright[1]):
        #         igracyt.hitbox.x -= 10
        #         igracyt.hitbox.y += 10
        #     igracyt.dvizenie(ljavo=-50, djasno=100)
        #
        #     vragelit.narisuvane()
        #     vragelit.vrazduvane(igracyt, '1')
        #     vragoficer.narisuvane()
        #     vragoficer.vrazduvane(igracyt, '20')
        #     vragboss.narisuvane()
        #     vragboss.vrazduvane(igracyt, 'B')
        #
        #     if not prijatel1.kljuc1:
        #         vrag1.vrazduvane(igracyt)
        #     else:
        #         prijatel1.razgovarjane(igracyt, e)
        #
        #     # karta1PesteraVhod.udareno_boxx(igracyt, 'Press E to ENTER the cave')
        #     if karta1PesteraVhod.hitbox.colliderect(igracyt.hitbox):
        #         karta1PesteraVhod.naris_msgbox()
        #         if key.get_pressed()[K_e]:
        #             del karta1PesteraVhod, kamyk, lyc, prijatel1, vrag1, vragelit, vragoficer, vragboss
        #             for k in MAP:
        #                 MAP[k] = False
        #             MAP['Pig Cave.pestera'] = True
        #             theload = 1
        #     # kymNacalo.udareno_boxx(igracyt, 'Press E to go back to start')
        #     if kymNacalo.hitbox.colliderect(igracyt.hitbox):
        #         kymNacalo.naris_msgbox()
        #         if key.get_pressed()[K_e]:
        #             del karta1PesteraVhod, kamyk, lyc, prijatel1, vrag1, vragelit, vragoficer, vragboss
        #             poslednaZona[0].clear()
        #             poslednaZona[1].clear()
        #             poslednaZona[0]['Pig Cave'] = True
        #             poslednaZona[1].append(karta1.miniHitbox.topleft)
        #             for k in MAP:
        #                 MAP[k] = False
        #             MAP['svetovna'] = True
        #             theload = 1
        # elif MAP['Pig Cave.pestera']:
        #     if theload:
        #         print('loading')
        #         from data.karta1 import obekt_syzdatel_v_pesterata
        #         karta1Pestera, karta1PesteraIzhod1, prijatel11 = obekt_syzdatel_v_pesterata()
        #
        #         theload = 0
        #
        #     karta1Pestera.risuvaj_zonata(True)
        #     karta1PesteraIzhod1.narisuvane()
        #
        #
        #     #print(igracyt.playerPosX, igracyt.hitbox.x, prijatel11.hitbox.x)
        #     if (igracyt.hitbox.x >= 525 and igracyt.playerPosX >= 1080 and prijatel11.hitbox.x >= 0 or
        #             prijatel11.hitbox.x <= 600 and prijatel11.hitbox.x >= 0):
        #         prijatel11.hitbox.x += -5
        #         prijatel11.spusyk_pestera(True)
        #     if prijatel11.hitbox.x >= 0:
        #         prijatel11.narisuvane()
        #
        #     # print(, dvizenie[0])
        #
        #     igracyt.narisuvane()
        #     igracyt.dvizenie(True, 1, None, 350, 100, 260)
        #
        #     # karta1PesteraIzhod1.udareno_boxx(igracyt, 'Press E to EXIT the cave')
        #     if karta1PesteraIzhod1.hitbox.colliderect(igracyt.hitbox):
        #         karta1PesteraIzhod1.naris_msgbox()
        #         if key.get_pressed()[K_e]:
        #             del karta1Pestera, karta1PesteraIzhod1, prijatel11
        #
        #             for k in MAP:
        #                 MAP[k] = False
        #             MAP['Pig Cave'] = True
        #             theload = 1
        # elif MAP['Market place']:
        #     if theload:
        #         print('loading')
        #
        #         from data.karta2 import npc_syzdatel
        #         prodavac, raz1, raz2 = npc_syzdatel()
        #         theload = 0
        #
        #     karta2.risuvaj_zonata(True)
        #     kymNacalo.narisuvane()
        #
        #     prodavac.narisuvane()
        #     raz1.narisuvane()
        #     raz2.narisuvane()
        #
        #     igracyt.narisuvane()
        #     igracyt.dvizenie(True, 1, (-10, 100), 0, 20, 350)
        #
        #
        #     if igracyt.hitbox.bottom <= 410 and igracyt.hitbox.x >= 535 and igracyt.playerPosX >= 10:
        #         igracyt.hitbox.bottom = 410
        #
        #
        #
        #     prodavac.hitbox.x += dvizenie[0]
        #     raz1.hitbox.x += dvizenie[0]
        #     raz2.hitbox.x += dvizenie[0]
        #     kymNacalo.hitbox.x += dvizenie[0]
        #
        #     prodavac.razgovarjane(igracyt, e)
        #     raz1.razgovarjane(igracyt, e)
        #     raz2.razgovarjane(igracyt, e)
        #
        #     # kymNacalo.udareno_boxx(igracyt, 'Press E to go bat to start')
        #     if kymNacalo.hitbox.colliderect(igracyt.hitbox):
        #         kymNacalo.naris_msgbox()
        #         if key.get_pressed()[K_e]:
        #             print('exiting')
        #             del prodavac
        #             poslednaZona[0].clear()
        #             poslednaZona[1].clear()
        #             poslednaZona[0]['Market place'] = True
        #             poslednaZona[1].append(karta2.miniHitbox.topleft)
        #             for k in MAP:
        #                 MAP[k] = False
        #             MAP['svetovna'] = True
        #             theload = 1
        # elif MAP['Westvield City']:
        #     if theload:
        #         print('loading')
        #         from data.grad import syzdaj_sgradi
        #         zgrada1, zgrada2, zgrada3, zgrada4 = syzdaj_sgradi()
        #         theload = 0
        #
        #     grad.risuvaj_zonata(True)
        #     zgrada1.narisuvane()
        #     zgrada2.narisuvane()
        #     zgrada3.narisuvane()
        #     zgrada4.narisuvane()
        #
        #     igracyt.narisuvane()
        #     igracyt.dvizenie(True, 4, gore=520, djasno=50)
        #
        #     zgrada1.auto_boxx(igracyt)
        #
        #
        #     zgrada1.hitbox.x += dvizenie[0]
        #     zgrada2.hitbox.x += dvizenie[0]
        #     zgrada3.hitbox.x += dvizenie[0]
        #     zgrada4.hitbox.x += dvizenie[0]
        #     kymNacalo.hitbox.x += dvizenie[0]
        #     kymNacalo.narisuvane()
        #     if kymNacalo.hitbox.colliderect(igracyt.hitbox):
        #         kymNacalo.naris_msgbox()
        #         if key.get_pressed()[K_e]:
        #             del zgrada1, zgrada2, zgrada3, zgrada4
        #             poslednaZona[0].clear()
        #             poslednaZona[1].clear()
        #             poslednaZona[0]['Westvield City'] = True
        #             poslednaZona[1].append(grad.miniHitbox.topleft)
        #             for k in MAP:
        #                 MAP[k] = False
        #             MAP['svetovna'] = True
        #             theload = 1

        igracyt.bagaz_v_ranicata(e)
        # print(igracyt._y_move)
        fpsint(CLOCK.get_fps(), EKRAN)
        display.flip()
        # print('vrag1' in locals())
        # print("Uncollectable garbage:", gc.garbage, 'colected', gc.collect())
    quit()
