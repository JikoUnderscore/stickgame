from random import randrange
from pygame import image, Color, draw, KEYDOWN, K_1, K_2, K_q, K_0, font, Rect, transform, Surface
from Postojanni import EKRAN, FONT18, FONT35, FONT40, SRIFT

'''
Spravja se s dvubojyt mezdu dva obekta.
'subekt' e gtalvija igrac, a 'obekt' e protivnikyt

Opredelja kak i kakvo moze da pravi protivnikyt po vreme na butka.
'''
obektkor = 655, 300
obektKryvX = 200
obektKrvPromenliv = 0

subektkor = 250, 200
subektKryvX = 200
subektKrvPromenliv = 0
subektlj = 50
subektdj = 50
subektrz = 50
subektGCD = 0
jj = True

bojnoPole = image.load('data/bojnopole.png').convert()
animacijaZivot = [
    image.load('data/mobs/vrag1/animacija/HH1.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/HH2.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/HH2.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/HH3.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/HH3.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/HH3.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/HH4.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/HH4.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/HH4.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/HH5.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/HH5.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/HH5.png').convert_alpha()]
animacijaZastita = [
    image.load('data/mobs/vrag1/animacija/Z1.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/Z2.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/Z2.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/Z3.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/Z3.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/Z3.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/Z4.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/Z4.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/Z4.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/Z5.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/Z5.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/Z5.png').convert_alpha()]
animacijaSteta = [
    image.load('data/mobs/vrag1/animacija/K1.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/K2.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/K2.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/K3.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/K3.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/K3.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/K4.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/K4.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/K4.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/K5.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/K5.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/K5.png').convert_alpha()]
obektATKanimacija = [
    image.load('data/mobs/vrag1/animacija/L1.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/L2.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/L2.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/L3.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/L3.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/L3.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/L4.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/L4.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/L4.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/L5.png').convert_alpha(),
    image.load('data/mobs/vrag1/animacija/L5.png').convert_alpha(), image.load('data/mobs/vrag1/animacija/L5.png').convert_alpha()]
countATK = 0
countATKl = 0
countRazno = [0, 0, 0]
# obektAnimacijaX = 0
# obektAnimacijaE = False

cooldownIkonka = image.load('data/cdikonka.png').convert()
gcdIkonka = image.load('data/GCDikonki.png').convert_alpha()
predajse = image.load('data/ikonki/predajse.png').convert()
predajseKv = predajse.get_rect()
obektATKIsTruD = False
obektATKIsTruL = False
obektRazno = [False] * 3

tekstStetaSubekt = [False] * 4
randoSubekt = [True] * 4
korSubekt = [[]] * 4
scrollTxtSubekt = [''] * 4
scrollClrSubekt = ["red"] * 4

tekstStetaObekt = [False] * 4
randoObekt = [True] * 4
korObekt = [[]] * 4
scrollTxtObekt = [''] * 4
scrollClrObekt = ["red"] * 4
scrollSizeObekt = [1] * 4

obektZastita = False
obektZastitaStart = True

healOverTime = False
defUp = False
defStart = True
stypka = 0
pozicijaNaPoleto = [0, 0]
tresenieProdylzitelnost = 0


# bojnoPoleRect = bojnoPole.get_rect()
# obekt = obekt
# subekt = subekt


def narisuvaj_pojnoto_pole(obekt, subekt):
    global pozicijaNaPoleto, tresenieProdylzitelnost
    EKRAN.blit(bojnoPole, pozicijaNaPoleto)
    # if not obektATKIsTruD and not obektATKIsTruL:
    #     EKRAN.blit(obekt.covece, obektkor)
    # elif not obektATKIsTruL:
    #     EKRAN.blit(obekt.covece, obektkor)
    EKRAN.blit(obekt.covece, obektkor)
    EKRAN.blit(subekt.covece, subektkor)

    if tresenieProdylzitelnost > 0:
        tresenieProdylzitelnost -= 1
        if tresenieProdylzitelnost:
            pozicijaNaPoleto[1] = randrange(0, 8)
            pozicijaNaPoleto[0] = randrange(0, 8)
    else:
        pozicijaNaPoleto = [0, 0]


def normalen_mob(e, cd, obekt, subekt):
    global obektATKIsTruD, countATK
    _pri_kraj(subekt, obekt)
    _tocki_zivot(obekt, subekt)

    txt = FONT35.render(f"{subekt.GCD:.2f}", True, Color("red"))
    EKRAN.blit(txt, (10, 550))

    subekt.cool_down_START(cd)
    obekt.cool_down_START(cd)
    subekt.global_cool_down(cd)

    if obekt.djasnaAtakaCD == 0:
        obektATKIsTruD = True
    if obektATKIsTruD:
        countATK += 0.25
        if countATK >= len(obektATKanimacija):
            countATK = 0
            obektATKIsTruD = False
        else:

            print(countATK, len(obektATKanimacija))
            EKRAN.blit(obektATKanimacija[int(countATK)], (obektkor[0] - 200, obektkor[1] - 100))
            # print(ty.x)
        if countATK == 2:

            if randrange(1, 101) >= subekt.dodge:
                subekt.HPnstojast -= namyli_atakata(obekt.djasnaAtaka, subekt.zastita)  # obekt.djasnaAtaka

                tekstStetaSubekt[0] = True
                scrollTxtSubekt[0] = f'{namyli_atakata(obekt.djasnaAtaka, subekt.zastita)}'
                scrollClrSubekt[0] = 'red'
                print('vrag hit')
            else:
                tekstStetaSubekt[0] = True
                scrollTxtSubekt[0] = 'dodge'
                scrollClrSubekt[0] = 'white'
                print('vrag: you dodged')
            obekt.djasnaAtakaCD = 0.01

    _kontrol_nad_igracyt(e, obekt, subekt)
    _lenta_s_dejstvija(subekt)
    _scrollin_combat_text(subekt, obekt)


def elit_mob(e, cd, obekt, subekt):
    global countATK, countATKl, obektATKIsTruD, obektATKIsTruL
    _pri_kraj(subekt, obekt)
    _tocki_zivot(obekt, subekt)

    txt = FONT35.render(f"{subekt.GCD:.2f}", True, Color("red"))
    EKRAN.blit(txt, (10, 550))

    subekt.cool_down_START(cd)
    obekt.cool_down_START(cd)
    subekt.global_cool_down(cd)
    obekt.global_cool_down(cd)

    if obekt.djasnaAtakaCD == 0 and obekt.GCD == 0:
        obektATKIsTruD = True
    elif obekt.ljavaAtakaCD == 0 and obekt.GCD == 0:
        obektATKIsTruL = True

    _kontrol_nad_igracyt(e, obekt, subekt)
    _lenta_s_dejstvija(subekt)
    _scrollin_combat_text(subekt, obekt)

    if obektATKIsTruD:
        countATK += 0.25
        if countATK >= len(obektATKanimacija):
            countATK = 0
            obektATKIsTruD = False
        else:
            EKRAN.blit(obektATKanimacija[int(countATK)], (obektkor[0] - 200, obektkor[1] - 100))

        if countATK == 2:

            if randrange(1, 101) >= subekt.dodge:
                subekt.HPnstojast -= namyli_atakata(obekt.djasnaAtaka, subekt.zastita)  # obekt.djasnaAtaka

                tekstStetaSubekt[0] = True
                scrollTxtSubekt[0] = f'{namyli_atakata(obekt.djasnaAtaka, subekt.zastita)}'
                scrollClrSubekt[0] = 'red'
                print('vrag hit')
            else:
                tekstStetaSubekt[0] = True
                scrollTxtSubekt[0] = 'dodge'
                scrollClrSubekt[0] = 'white'
                print('vrag: you dodged')
            obekt.djasnaAtakaCD = 0.01
            obekt.GCD = 0.1
    elif obektATKIsTruL:
        countATKl += 0.25
        if countATKl >= len(obektATKanimacija):
            countATKl = 0
            obektATKIsTruL = False
        else:
            EKRAN.blit(obektATKanimacija[int(countATKl)], (obektkor[0] - 200, obektkor[1] - 100))

        if countATKl == 2:

            if randrange(1, 101) >= subekt.dodge:
                steta = namyli_atakata(obekt.ljavaAtaka, subekt.zastita)
                subekt.HPnstojast -= steta  # obekt.djasnaAtaka

                tekstStetaSubekt[1] = True
                scrollTxtSubekt[1] = f'{steta}'
                scrollClrSubekt[1] = 'red'
                print('vrag hit')
            else:
                tekstStetaSubekt[1] = True
                scrollTxtSubekt[1] = 'dodge'
                scrollClrSubekt[1] = 'white'
                print('vrag: you dodged')
            obekt.ljavaAtakaCD = 0.01
            obekt.GCD = 0.1


def oficer_mob(e, cd, obekt, subekt, klas_na_oficera):
    global countATK, countATKl, obektZastitaStart, obektATKIsTruD, obektATKIsTruL, obektRazno, obektZastita
    _pri_kraj(subekt, obekt)
    _tocki_zivot(obekt, subekt)

    txt = FONT35.render(f"{subekt.GCD:.2f}", True, Color("red"))
    EKRAN.blit(txt, (10, 550))

    subekt.cool_down_START(cd)
    obekt.cool_down_START(cd)
    subekt.global_cool_down(cd)
    obekt.global_cool_down(cd)

    if obekt.djasnaAtakaCD == 0 and obekt.GCD == 0:
        obektATKIsTruD = True
    elif obekt.ljavaAtakaCD == 0 and obekt.GCD == 0:
        obektATKIsTruL = True

    if obekt.raznoCD == 0:
        obektRazno[0] = True

    _kontrol_nad_igracyt(e, obekt, subekt)
    _lenta_s_dejstvija(subekt)
    _scrollin_combat_text(subekt, obekt)

    if obektATKIsTruD:
        countATK += 0.25
        if countATK >= len(obektATKanimacija):
            countATK = 0
            obektATKIsTruD = False
        else:
            EKRAN.blit(obektATKanimacija[int(countATK)], (obektkor[0] - 200, obektkor[1] - 100))

        if countATK == 2:

            if randrange(1, 101) >= subekt.dodge:
                subekt.HPnstojast -= namyli_atakata(obekt.djasnaAtaka, subekt.zastita)  # obekt.djasnaAtaka

                tekstStetaSubekt[0] = True
                scrollTxtSubekt[0] = f'{namyli_atakata(obekt.djasnaAtaka, subekt.zastita)}'
                scrollClrSubekt[0] = 'red'
                print('vrag hit')
            else:
                tekstStetaSubekt[0] = True
                scrollTxtSubekt[0] = 'dodge'
                scrollClrSubekt[0] = 'white'
                print('vrag: you dodged')
            obekt.djasnaAtakaCD = 0.01
            obekt.GCD = 0.1
    elif obektATKIsTruL:
        countATKl += 0.25
        if countATKl >= len(obektATKanimacija):
            countATKl = 0
            obektATKIsTruL = False
        else:
            EKRAN.blit(obektATKanimacija[int(countATKl)], (obektkor[0] - 200, obektkor[1] - 100))

        if countATKl == 2:

            if randrange(1, 101) >= subekt.dodge:
                steta = namyli_atakata(obekt.ljavaAtaka, subekt.zastita)
                subekt.HPnstojast -= steta  # obekt.djasnaAtaka

                tekstStetaSubekt[1] = True
                scrollTxtSubekt[1] = f'{steta}'
                scrollClrSubekt[1] = 'red'
                print('vrag hit')
            else:
                tekstStetaSubekt[1] = True
                scrollTxtSubekt[1] = 'dodge'
                scrollClrSubekt[1] = 'white'
                print('vrag: you dodged')
            obekt.ljavaAtakaCD = 0.01
            obekt.GCD = 0.1

    if obektRazno[0]:
        countRazno[0] += 0.25
        if countRazno[0] >= len(animacijaZastita):
            countRazno[0] = 0
            obektRazno[0] = False
        else:
            EKRAN.blit(animacijaZastita[int(countRazno[0])], (obektkor[0] - 200, obektkor[1] - 420))

        if countRazno[0] == 2:
            print('here')
            # print(obekt.raznoCD)
            if klas_na_oficera == '-':
                subekt.HPnstojast -= obekt.specialno
                tekstStetaSubekt[2] = True
                scrollTxtSubekt[2] = f'{obekt.specialno}'
                scrollClrSubekt[2] = 'black'
            elif klas_na_oficera == '+':
                obekt.HPnstojast += obekt.specialno
                if obekt.HPnstojast > obekt.HP + int(obekt.HP * 0.15):
                    obekt.HPnstojast -= obekt.HPnstojast - (obekt.HP + int(obekt.HP * 0.15))
            elif klas_na_oficera == '0':
                obektZastita = True
            obekt.raznoCD = 0.1

    # print(obekt.zastita, subekt.zastita)
    if obektZastita:
        if obektZastitaStart:
            obekt.zastita += obekt.specialno
        obektZastitaStart = False
        draw.rect(EKRAN, (46, 255, 252), ((obektkor[0]-50, obektkor[1]-obekt.hitbox.height), (5, 300)))
        if int(obekt.raznoCD) == 4:
            obekt.zastita -= obekt.specialno
            obektZastita = False
            obektZastitaStart = True

    # print(obekt.ljavaAtakaCD, obekt.djasnaAtakaCD, obekt.GCD)


def bos_mob(e, cd, obekt, subekt):
    global obektZastitaStart, obektZastita, obektATKIsTruD, countATK, obektATKIsTruL, countATKl, obektRazno
    _pri_kraj(subekt, obekt)
    _tocki_zivot(obekt, subekt)

    txt = FONT35.render(f"{subekt.GCD:.2f}", True, Color("red"))
    EKRAN.blit(txt, (10, 550))

    subekt.cool_down_START(cd)
    obekt.cool_down_START(cd)
    subekt.global_cool_down(cd)
    obekt.global_cool_down(cd)

    print(obekt.zastita)
    if obekt.djasnaAtakaCD == 0 and obekt.GCD == 0:
        obektATKIsTruD = True
    elif obekt.ljavaAtakaCD == 0 and obekt.GCD == 0:
        obektATKIsTruL = True
    if obekt.raznoCD == 0:
        obektRazno[0] = True
    if f'{obekt.raznoCD:.2f}' == '4.01' or f'{obekt.raznoCD:.2f}' == '4.00':
        obektRazno[1] = True
    if f'{obekt.raznoCD:.2f}' == '8.01' or f'{obekt.raznoCD:.2f}' == '8.00':
        obektRazno[2] = True

    _kontrol_nad_igracyt(e, obekt, subekt)
    _lenta_s_dejstvija(subekt)
    _scrollin_combat_text(subekt, obekt)

    if obektATKIsTruD:
        countATK += 0.25
        if countATK >= len(obektATKanimacija):
            countATK = 0
            obektATKIsTruD = False
        else:
            EKRAN.blit(obektATKanimacija[int(countATK)], (obektkor[0] - 200, obektkor[1] - 100))

        if countATK == 2:
            if randrange(1, 101) >= subekt.dodge:
                subekt.HPnstojast -= namyli_atakata(obekt.djasnaAtaka, subekt.zastita)
                tekstStetaSubekt[0] = True
                scrollTxtSubekt[0] = f'{namyli_atakata(obekt.djasnaAtaka, subekt.zastita)}'
                scrollClrSubekt[0] = 'red'
                print('vrag hit')
            else:
                tekstStetaSubekt[0] = True
                scrollTxtSubekt[0] = 'dodge'
                scrollClrSubekt[0] = 'white'
                print('vrag: you dodged')
            obekt.djasnaAtakaCD = 0.01
            obekt.GCD = 0.1
            # obektATKIsTruD = False
    elif obektATKIsTruL:
        countATKl += 0.25
        if countATKl >= len(obektATKanimacija):
            countATKl = 0
            obektATKIsTruL = False
        else:
            EKRAN.blit(obektATKanimacija[int(countATKl)], (obektkor[0] - 200, obektkor[1] - 100))

        if countATKl == 2:

            if randrange(1, 101) >= subekt.dodge:
                steta = namyli_atakata(obekt.ljavaAtaka, subekt.zastita)
                subekt.HPnstojast -= steta
                tekstStetaSubekt[1] = True
                scrollTxtSubekt[1] = f'{steta}'
                scrollClrSubekt[1] = 'red'
                print('vrag hit')
            else:
                tekstStetaSubekt[1] = True
                scrollTxtSubekt[1] = 'dodge'
                scrollClrSubekt[1] = 'white'
                print('vrag: you dodged')
            obekt.ljavaAtakaCD = 0.01
            obekt.GCD = 0.1
            # obektATKIsTruL = False

    # print(f'{obekt.raznoCD:.2f}')
    if obektRazno[0]:
        countRazno[0] += 0.25
        if countRazno[0] >= len(animacijaSteta):
            countRazno[0] = 0
            obektRazno[0] = False
        else:
            EKRAN.blit(animacijaSteta[int(countRazno[0])], (obektkor[0] - 200, obektkor[1] - 420))

        if countRazno[0] == 2:
            subekt.HPnstojast -= obekt.specialno
            tekstStetaSubekt[2] = True
            scrollTxtSubekt[2] = f'{obekt.specialno}'
            scrollClrSubekt[2] = 'black'
            obekt.raznoCD = 0.1
    if obektRazno[1]:
        countRazno[1] += 0.25
        if countRazno[1] >= len(animacijaZivot):
            countRazno[1] = 0
            obektRazno[1] = False
        else:
            EKRAN.blit(animacijaZivot[int(countRazno[1])], (obektkor[0] - 200, obektkor[1] - 420))

        if countRazno[1] == 2:
            obekt.HPnstojast += obekt.specialno
            if obekt.HPnstojast > obekt.HP + int(obekt.HP * 0.15):
                obekt.HPnstojast -= obekt.HPnstojast - (obekt.HP + int(obekt.HP * 0.15))
    if obektRazno[2]:
        countRazno[2] += 0.25
        if countRazno[2] >= len(animacijaZastita):
            countRazno[2] = 0
            obektRazno[2] = False
        else:
            EKRAN.blit(animacijaZastita[int(countRazno[2])], (obektkor[0] - 200, obektkor[1] - 420))

        if countRazno[2] == 2:
            obektZastita = True

    # print(obekt.zastita, subekt.zastita)
    if obektZastita:
        if obektZastitaStart:
            obekt.zastita += obekt.specialno
        obektZastitaStart = False
        draw.rect(EKRAN, (46, 255, 252), ((obektkor[0]-50, obektkor[1]-obekt.hitbox.height), (5, 300)))
        if int(obekt.raznoCD) == 4:
            obekt.zastita -= obekt.specialno
            obektZastita = False
            obektZastitaStart = True


def _pri_kraj(subekt, obekt):
    global tresenieProdylzitelnost, tekstStetaSubekt, randoSubekt, korSubekt, scrollTxtSubekt, scrollClrSubekt, tekstStetaObekt, randoObekt, korObekt, \
        scrollTxtObekt, scrollTxtObekt, scrollClrObekt, scrollSizeObekt, obektZastita, obektZastitaStart, healOverTime, defUp, defStart, stypka, obektKryvX, \
        subektkor, subektKryvX, subektlj, subektdj, subektrz, subektGCD, jj, countATK, countATKl, obektATKIsTruD, obektATKIsTruL, obektRazno

    if obekt.HPnstojast <= 0 or subekt.HPnstojast <= 0:
        # jj = 1
        if subekt.HPnstojast <= 0:
            print(f'{obekt.ime} wins')
        else:
            print('IGTACYT wins')
        # subekt.vel = 5
        obekt.HPnstojast = obekt.HP
        subekt.HPnstojast = subekt.HP

        obekt.boj = False
        tresenieProdylzitelnost = 0

        subekt.ljavaAtakaCD = 0
        subekt.djasnaAtakaCD = 0
        obekt.djasnaAtakaCD = 0
        obekt.ljavaAtakaCD = 0
        obekt.GCD = 0
        subekt.GCD = 0

        tekstStetaSubekt = [False] * 4
        randoSubekt = [True] * 4
        korSubekt = [[]] * 4
        scrollTxtSubekt = [''] * 4
        scrollClrSubekt = ["red"] * 4

        tekstStetaObekt = [False] * 4
        randoObekt = [True] * 4
        korObekt = [[]] * 4
        scrollTxtObekt = [''] * 4
        scrollClrObekt = ["red"] * 4
        scrollSizeObekt = [1] * 4

        ###
        if obektZastita:
            obekt.zastita -= obekt.specialno
        obektZastita = False
        obektZastitaStart = True

        healOverTime = False
        defUp = False
        defStart = True
        stypka = 0
        # obektkor = 555, 310
        obektKryvX = 200
        # obektKrvPromenliv = 100

        subektkor = 150, 200
        subektKryvX = 200
        # subektKrvPromenliv = 100
        subektlj = 50
        subektdj = 50
        subektrz = 50
        subektGCD = 0
        jj = True

        countATK = 0
        countATKl = 0
        obektATKIsTruD = False
        obektATKIsTruL = False
        obektRazno = [False] * 3
        return


def _kontrol_nad_igracyt(e, obekt, subekt):
    global stypka, defStart, defStart, healOverTime, defUp, tresenieProdylzitelnost
    if e.type == KEYDOWN and subekt.GCD == 0:
        # subekt.GCD = 0.1

        if e.key == K_1 and subekt.ljavaAtakaCD == 0 and subekt.ljavaAtakaMAX > 0:
            if randrange(1, 101) <= subekt.hitChance:
                if randrange(1, 101) <= subekt.crit:
                    print('crit atacka')
                    tresenieProdylzitelnost = 50
                    steta = namyli_atakata(((subekt.ljavaAtaka + subekt.atkBonusl) * max(subekt.critMultiplier)), obekt.zastita)
                    obekt.HPnstojast -= steta
                    tekstStetaObekt[0] = True
                    scrollTxtObekt[0] = f'CRIT {steta}'
                    scrollClrObekt[0] = 'green'
                    scrollSizeObekt[0] = 2
                else:
                    print('standarta ataka')
                    steta = namyli_atakata((subekt.ljavaAtaka + subekt.atkBonusl), obekt.zastita)
                    obekt.HPnstojast -= steta
                    tekstStetaObekt[0] = True
                    scrollTxtObekt[0] = f'{steta}'
                    scrollClrObekt[0] = 'red'
            else:
                print('miss')
                tekstStetaObekt[0] = True
                scrollTxtObekt[0] = 'Miss'
                scrollClrObekt[0] = 'white'
            subekt.ljavaAtakaCD = 0.01
            subekt.GCD = 0.1
        if e.key == K_2 and subekt.djasnaAtakaCD == 0 and subekt.djasnaAtakaMAX > 0:
            if randrange(1, 101) <= subekt.hitChance:
                if randrange(1, 101) <= subekt.crit:
                    print('crit atacka')
                    tresenieProdylzitelnost = 50
                    steta = namyli_atakata(((subekt.djasnaAtaka + subekt.atkBonusd) * max(subekt.critMultiplier)), obekt.zastita)
                    obekt.HPnstojast -= steta
                    tekstStetaObekt[1] = True
                    scrollTxtObekt[1] = f'CRIT {steta}'
                    scrollClrObekt[1] = 'green'
                    scrollSizeObekt[1] = 2
                else:
                    print('silna ataka')
                    steta = namyli_atakata((subekt.djasnaAtaka + subekt.atkBonusd), obekt.zastita)
                    obekt.HPnstojast -= steta
                    tekstStetaObekt[1] = True
                    scrollTxtObekt[1] = f'{steta}'
                    scrollClrObekt[1] = 'red'
            else:
                print('miss')
                tekstStetaObekt[1] = True
                scrollTxtObekt[1] = 'Miss'
                scrollClrObekt[1] = 'white'
            subekt.djasnaAtakaCD = 0.01
            subekt.GCD = 0.1
        if e.key == K_q and subekt.raznoCD == 0 and subekt._raznoto:
            print('razno')
            if subekt._raznoto[0].HP != 0:
                subekt.HPnstojast += subekt._raznoto[0].HP
                if subekt._raznoto[0].damage != 0:
                    obekt.HPnstojast -= subekt._raznoto[0].damage
                    tekstStetaObekt[2] = True
                    scrollTxtObekt[2] = f'{subekt._raznoto[0].damage}'
                    scrollClrObekt[2] = 'black'
                if subekt.HPnstojast > subekt.HP:
                    subekt.HPnstojast -= subekt.HPnstojast - subekt.HP
            elif subekt._raznoto[0].heal_per_second != 0:
                healOverTime = True
            elif subekt._raznoto[0].def_per_secod != 0:
                defUp = True

                # obekt.HPnstojast -=
            subekt.GCD = 0.1
            subekt.raznoCD = 0.01
        if e.key == K_0:
            subekt.HPnstojast = 0

    # print(subekt.zastita)
    if healOverTime:
        if int(subekt.raznoCD) == subekt._raznoto[0].heal_per_second[1]:
            healOverTime = False
            stypka = 0
        elif int(subekt.raznoCD) == subekt._raznoto[0].heal_per_second[1] - subekt._raznoto[0].heal_per_second[1] + stypka:
            subekt.HPnstojast += subekt._raznoto[0].heal_per_second[0]
            if subekt.HPnstojast > subekt.HP:
                subekt.HPnstojast -= subekt.HPnstojast - subekt.HP
            if int(subekt.raznoCD) <= subekt._raznoto[0].heal_per_second[1]:
                stypka += 1
    elif defUp:
        if defStart:
            subekt.zastita += subekt._raznoto[0].def_per_secod[0]
        defStart = False
        draw.rect(EKRAN, (46, 255, 252), ((350, 150), (5, 300)))
        if int(subekt.raznoCD) == subekt._raznoto[0].def_per_secod[1]:
            defUp = False
            defStart = True
            subekt.zastita -= subekt._raznoto[0].def_per_secod[0]


def _scrollin_combat_text(subekt, obekt):
    # subekt
    if tekstStetaObekt[0]:
        if randoObekt[0]:
            x, y = randrange(obektkor[0], obektkor[0] + 100), randrange(obektkor[1], obektkor[1] + 100)
            korObekt[0].append(x)
            korObekt[0].append(y)
        randoObekt[0] = False
        txt = font.Font(SRIFT, 40 * scrollSizeObekt[0]).render(scrollTxtObekt[0], True, Color(scrollClrObekt[0]))

        EKRAN.blit(txt, (korObekt[0][0], korObekt[0][1] - subekt.ljavaAtakaCD * 150))
        if subekt.ljavaAtakaCD >= 1:
            tekstStetaObekt[0] = False
            randoObekt[0] = True
            korObekt[0] = []
            scrollSizeObekt[0] = 1
    if tekstStetaObekt[1]:
        if randoObekt[1]:
            x, y = randrange(obektkor[0], obektkor[0] + 100), randrange(obektkor[1], obektkor[1] + 100)
            korObekt[1].append(x)
            korObekt[1].append(y)
        randoObekt[1] = False
        txt2 = font.Font(SRIFT, 40 * scrollSizeObekt[1]).render(scrollTxtObekt[1], True, Color(scrollClrObekt[1]))

        EKRAN.blit(txt2, (korObekt[1][0], korObekt[1][1] - subekt.djasnaAtakaCD * 150))
        if subekt.djasnaAtakaCD >= 1:
            tekstStetaObekt[1] = False
            randoObekt[1] = True
            korObekt[1] = []
            scrollSizeObekt[1] = 1
    if tekstStetaObekt[2]:
        if randoObekt[2]:
            x, y = randrange(obektkor[0], obektkor[0] + 100), randrange(obektkor[1], obektkor[1] + 100)
            korObekt[2].append(x)
            korObekt[2].append(y)
        randoObekt[2] = False
        txt2 = font.Font(SRIFT, 40 * scrollSizeObekt[2]).render(scrollTxtObekt[2], True, Color(scrollClrObekt[2]))

        EKRAN.blit(txt2, (korObekt[2][0], korObekt[2][1] - subekt.raznoCD * 150))
        if subekt.raznoCD >= 1:
            tekstStetaObekt[2] = False
            randoObekt[2] = True
            korObekt[2] = []
            scrollSizeObekt[2] = 1

    # obekt
    if tekstStetaSubekt[0]:
        if randoSubekt[0]:
            x, y = randrange(subektkor[0] - 50, subektkor[0]), randrange(subektkor[1], subektkor[1] + 50)
            korSubekt[0].append(x)
            korSubekt[0].append(y)
        randoSubekt[0] = False
        txt = FONT40.render(scrollTxtSubekt[0], True, Color(scrollClrSubekt[0]))

        EKRAN.blit(txt, (korSubekt[0][0], korSubekt[0][1] - obekt.djasnaAtakaCD * 150))
        if obekt.djasnaAtakaCD >= 1:
            tekstStetaSubekt[0] = False
            randoSubekt[0] = True
            korSubekt[0] = []
    if tekstStetaSubekt[1]:
        if randoSubekt[1]:
            x, y = randrange(subektkor[0] - 50, subektkor[0]), randrange(subektkor[1], subektkor[1] + 50)
            korSubekt[1].append(x)
            korSubekt[1].append(y)
        randoSubekt[1] = False
        txt = FONT40.render(scrollTxtSubekt[1], True, Color(scrollClrSubekt[1]))

        EKRAN.blit(txt, (korSubekt[1][0], korSubekt[1][1] - obekt.ljavaAtakaCD * 150))
        if obekt.ljavaAtakaCD >= 1:
            tekstStetaSubekt[1] = False
            randoSubekt[1] = True
            korSubekt[1] = []
    if tekstStetaSubekt[2]:
        if randoSubekt[2]:
            x, y = randrange(subektkor[0] - 50, subektkor[0]), randrange(subektkor[1], subektkor[1] + 50)
            korSubekt[2].append(x)
            korSubekt[2].append(y)
        randoSubekt[2] = False
        txt = FONT40.render(scrollTxtSubekt[2], True, Color(scrollClrSubekt[2]))

        EKRAN.blit(txt, (korSubekt[2][0], korSubekt[2][1] - obekt.raznoCD * 150))
        if obekt.raznoCD >= 1:
            tekstStetaSubekt[2] = False
            randoSubekt[2] = True
            korSubekt[2] = []


def _lenta_s_dejstvija(subekt):
    global subektrz, subektdj, subektlj, subektGCD
    dejst1 = subekt.oryzieIkonka
    dejst2 = subekt.oryzieIkonka
    raznoq = subekt.raznoIkonka
    znackae = subekt.znackaIkonka
    if subekt._ljavoOryzie:
        dejst1 = subekt._ljavoOryzie[0].ikonka
    if subekt._djasnoOryzie:
        dejst2 = subekt._djasnoOryzie[0].ikonka
    if subekt._raznoto:
        raznoq = subekt._raznoto[0].ikonka
    if subekt._znackata:
        znackae = subekt._znackata[0].ikonka

    # print(abs(subekt.ljavaAtakaCD))
    dvizX, dvizY = EKRAN.get_width() / 4, EKRAN.get_height() - 150

    EKRAN.blit(dejst1, (dvizX, dvizY))
    EKRAN.blit(dejst2, (dvizX + 60, dvizY))
    EKRAN.blit(raznoq, (dvizX + 60 * 2, dvizY))
    EKRAN.blit(znackae, (dvizX + 60 * 3, dvizY))

    EKRAN.blit(predajse, (dvizX + 60 * 6, dvizY))

    if subekt.GCD != 0:
        # print('d', subekt.GCD)
        subektGCD = int(250 - (250 * (subekt.GCD / subekt.GCDmax)))
        # print(subektGCD)
        gcdIkonka.set_alpha(subektGCD)
    else:
        gcdIkonka.set_alpha(0)

    if subekt.ljavaAtakaCD != 0:
        subektlj = int(50 - (50 * (subekt.ljavaAtakaCD / subekt.ljavaAtakaMAX)))
        k1 = Rect((dvizX, dvizY), (subektlj, 50))
        cooldownIkonka.set_alpha(200)
        EKRAN.blit(transform.scale(cooldownIkonka, (subektlj, 50)), k1)
    if subekt.djasnaAtakaCD != 0:
        subektdj = int(50 - (50 * (subekt.djasnaAtakaCD / subekt.djasnaAtakaMAX)))
        k2 = Rect((dvizX + 60, dvizY), (subektdj, 50))
        cooldownIkonka.set_alpha(200)
        EKRAN.blit(transform.scale(cooldownIkonka, (subektdj, 50)), k2)
    if subekt.raznoCD != 0:
        subektrz = int(50 - (50 * (subekt.raznoCD / subekt.raznoCDMAX)))
        k3 = Rect((dvizX + 120, dvizY), (subektrz, 50))
        cooldownIkonka.set_alpha(200)
        EKRAN.blit(transform.scale(cooldownIkonka, (subektrz, 50)), k3)
    # draw.rect(EKRAN, (11, 158, 126), ((dvizX, dvizY), (4 * 50 + 4 * 10, subektGCD)))
    EKRAN.blit(gcdIkonka, (dvizX, dvizY))


def _tocki_zivot(obekt, subekt):
    global jj, subektKrvPromenliv, obektKrvPromenliv, obektKryvX, subektKryvX
    obektKryvX = obekt.HPnstojast / (obekt.HP / 200)
    subektKryvX = subekt.HPnstojast / (subekt.HP / 200)
    # print(obektKrvPromenliv, jj)

    # print(jj, obekt.boj)
    if jj and obekt.boj:
        temps = [subekt.HPnstojast].copy()
        subektKrvPromenliv = temps[0]
        temps2 = [obekt.HPnstojast].copy()
        obektKrvPromenliv = temps2[0]
        # print(subektKrvPromenliv, obektKrvPromenliv)
        jj = False
        return

    prahodnaDylzinaSubect = 0
    prahodnaDylzinaObekt = 0
    prehodenCvjatSubekt = (0, 0, 255)
    prehodenCvjatObekt = (0, 0, 255)

    if subektKrvPromenliv < subekt.HPnstojast:
        subektKrvPromenliv += 0.2
        prahodnaDylzinaSubect = int(-(subekt.HPnstojast - subektKrvPromenliv) / (subekt.HP / 200))
        prehodenCvjatSubekt = (0, 255, 0)
    if subektKrvPromenliv > subekt.HPnstojast:
        subektKrvPromenliv -= 0.2
        prahodnaDylzinaSubect = int(-(subekt.HPnstojast - subektKrvPromenliv) / (subekt.HP / 200))
        prehodenCvjatSubekt = (255, 255, 0)

    # subekt
    graniciZivotSubekt = Surface((207, 27))
    graniciZivotSubekt.fill((255, 255, 255))
    nastKryv = Rect((3, 3), (subektKryvX, 20))
    fixedKv = Rect((3, 3), (200, 20))
    draw.rect(graniciZivotSubekt, (255, 0, 0), fixedKv)  # cervenija von na tockite zivot
    draw.rect(graniciZivotSubekt, (0, 255, 0), nastKryv)  # zelenija cjavt na tockite zivot, kojto namaljava
    ljNastojasto = FONT18.render(f'{subekt.HPnstojast}', False, (0, 0, 0))
    djMaksimalno = FONT18.render(f'{subekt.HP}', False, (0, 0, 0))
    draw.rect(graniciZivotSubekt, prehodenCvjatSubekt,
              (nastKryv.right, nastKryv.y, prahodnaDylzinaSubect, 20))  # zyltata/zelenata lenta na promjanata v tockite zivot
    graniciZivotSubekt.blit(ljNastojasto, (fixedKv.left + 5, fixedKv.y - 4))
    graniciZivotSubekt.blit(djMaksimalno, (fixedKv.right - 30, fixedKv.y - 4))
    EKRAN.blit(graniciZivotSubekt, (subektkor[0] - 10, subektkor[1] + 230))

    if obektKrvPromenliv < obekt.HPnstojast:
        obektKrvPromenliv += 0.2
        prahodnaDylzinaObekt = int(-(obekt.HPnstojast - obektKrvPromenliv) / (obekt.HP / 200))
        prehodenCvjatObekt = (0, 255, 0)
    if obektKrvPromenliv > obekt.HPnstojast:
        obektKrvPromenliv -= 0.2
        prahodnaDylzinaObekt = int(-(obekt.HPnstojast - obektKrvPromenliv) / (obekt.HP / 200))
        prehodenCvjatObekt = (255, 255, 0)

    # obekt
    graniciZivotObekt = Surface((207, 27))
    graniciZivotObekt.fill((255, 255, 255))
    nastKryv1 = Rect((3, 3), (obektKryvX, 20))
    fixedKv1 = Rect((3, 3), (200, 20))
    draw.rect(graniciZivotObekt, (255, 0, 0), fixedKv1)  # cervenija von na tockite zivot
    draw.rect(graniciZivotObekt, (0, 255, 0), nastKryv1)  # zelenija cjavt na tockite zivot, kojto namaljava
    nastojasto = FONT18.render(f'{obekt.HPnstojast}', False, (0, 0, 0))
    maksimalno = FONT18.render(f'{obekt.HP}', False, (0, 0, 0))
    draw.rect(graniciZivotObekt, prehodenCvjatObekt,
              (nastKryv1.right, nastKryv1.y, prahodnaDylzinaObekt, 20))  # zyltata/zelenata lenta na promjanata v tockite zivot
    graniciZivotObekt.blit(nastojasto, (fixedKv1.left + 5, fixedKv1.y - 4))
    graniciZivotObekt.blit(maksimalno, (fixedKv1.right - 30, fixedKv1.y - 4))
    EKRAN.blit(graniciZivotObekt, (obektkor[0] - 10, obektkor[1] + 130))


def namyli_atakata(ataka, zastita):
    if ataka - zastita <= 0:
        return 1
    return ataka - zastita
