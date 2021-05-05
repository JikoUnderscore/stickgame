from random import randrange
from pygame import image, Color, draw, KEYDOWN, K_1, K_2, K_q, K_0, font, Rect, transform, Surface
from Postojanni import EKRAN, FONT18, FONT35, FONT40, SRIFT

'''
Spravja se s dvubojyt mezdu dva obekta.
'subekt' e gtalvija igrac, a 'obekt' e protivnikyt

Opredelja kak i kakvo moze da pravi protivnikyt po vreme na butka.
'''


class Combats:
    obektkor = 655, 300
    obektKrvPromenliv = 0

    subektKrvPromenliv = 0

    bojnoPole = image.load('data/bojnopole.png').convert()
    animacijaZivot = [
        image.load('data/mobs/vrag1/animacija/HH1.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/HH2.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/HH2.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/HH3.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/HH3.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/HH3.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/HH4.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/HH4.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/HH4.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/HH5.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/HH5.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/HH5.png').convert_alpha()]
    animacijaZastita = [
        image.load('data/mobs/vrag1/animacija/Z1.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/Z2.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/Z2.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/Z3.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/Z3.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/Z3.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/Z4.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/Z4.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/Z4.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/Z5.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/Z5.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/Z5.png').convert_alpha()]
    animacijaSteta = [
        image.load('data/mobs/vrag1/animacija/K1.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/K2.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/K2.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/K3.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/K3.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/K3.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/K4.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/K4.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/K4.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/K5.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/K5.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/K5.png').convert_alpha()]
    obektATKanimacija = [
        image.load('data/mobs/vrag1/animacija/L1.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/L2.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/L2.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/L3.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/L3.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/L3.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/L4.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/L4.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/L4.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/L5.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/L5.png').convert_alpha(),
        image.load('data/mobs/vrag1/animacija/L5.png').convert_alpha()]
    countRazno = [0, 0, 0]
    # obektAnimacijaX = 0
    # obektAnimacijaE = False

    cooldownIkonka = image.load('data/cdikonka.png').convert()
    gcdIkonka = image.load('data/GCDikonki.png').convert_alpha()
    predajse = image.load('data/ikonki/predajse.png').convert()
    predajseKv = predajse.get_rect()

    pozicijaNaPoleto = [0, 0]

    # cls.bojnoPoleRect = cls.bojnoPole.get_rect()
    # obekt = obekt
    # subekt = subekt

    @classmethod
    def syzdaj_promenlivi(cls):
        cls.tresenieProdylzitelnost = 0

        cls.tekstStetaSubekt = [False] * 4
        cls.randoSubekt = [True] * 4
        cls.korSubekt = [[]] * 4
        cls.scrollTxtSubekt = [''] * 4
        cls.scrollClrSubekt = ["red"] * 4

        cls.tekstStetaObekt = [False] * 4
        cls.randoObekt = [True] * 4
        cls.korObekt = [[]] * 4
        cls.scrollTxtObekt = [''] * 4
        cls.scrollClrObekt = ["red"] * 4
        cls.scrollSizeObekt = [1] * 4

        cls.obektZastita = False
        cls.obektZastitaStart = True

        cls.healOverTime = False
        cls.defUp = False
        cls.defStart = True
        cls.stypka = 0
        # cls.obektkor = 555, 310
        cls.obektKryvX = 200
        # cls.obektKrvPromenliv = 100

        cls.subektkor = 250, 200
        cls.subektKryvX = 200
        # cls.subektKrvPromenliv = 100
        cls.subektlj = 50
        cls.subektdj = 50
        cls.subektrz = 50
        cls.subektGCD = 0
        cls.jj = True

        cls.countATK = 0
        cls.countATKl = 0
        cls.obektATKIsTruD = False
        cls.obektATKIsTruL = False
        cls.obektRazno = [False] * 3

    @classmethod
    def narisuvaj_pojnoto_pole(cls, obekt, subekt):
        # global cls.pozicijaNaPoleto, cls.tresenieProdylzitelnost
        EKRAN.blit(cls.bojnoPole, cls.pozicijaNaPoleto)
        # if not cls.obektATKIsTruD and not cls.obektATKIsTruL:
        #     EKRAN.blit(obekt.covece, cls.obektkor)
        # elif not cls.obektATKIsTruL:
        #     EKRAN.blit(obekt.covece, cls.obektkor)
        EKRAN.blit(obekt.covece, cls.obektkor)
        EKRAN.blit(subekt.covece, cls.subektkor)

        if cls.tresenieProdylzitelnost > 0:
            cls.tresenieProdylzitelnost -= 1
            if cls.tresenieProdylzitelnost:
                cls.pozicijaNaPoleto[1] = randrange(0, 8)
                cls.pozicijaNaPoleto[0] = randrange(0, 8)
        else:
            cls.pozicijaNaPoleto = [0, 0]

    @classmethod
    def normalen_mob(cls, e, cd, obekt, subekt):
        # global cls.obektATKIsTruD, cls.countATK
        cls._pri_kraj(subekt, obekt)
        cls._tocki_zivot(obekt, subekt)

        txt = FONT35.render(f"{subekt.GCD:.2f}", True, Color("red"))
        EKRAN.blit(txt, (10, 550))

        subekt.cool_down_START(cd)
        obekt.cool_down_START(cd)
        subekt.global_cool_down(cd)

        if obekt.djasnaAtakaCD == 0:
            cls.obektATKIsTruD = True
        if cls.obektATKIsTruD:
            cls.countATK += 0.25
            if cls.countATK >= len(cls.obektATKanimacija):
                cls.countATK = 0
                cls.obektATKIsTruD = False
            else:

                print(cls.countATK, len(cls.obektATKanimacija))
                EKRAN.blit(cls.obektATKanimacija[int(cls.countATK)], (cls.obektkor[0] - 200, cls.obektkor[1] - 100))
                # print(ty.x)
            if cls.countATK == 2:

                if randrange(1, 101) >= subekt.dodge:
                    subekt.HPnstojast -= cls.namyli_atakata(obekt.djasnaAtaka, subekt.zastita)  # obekt.djasnaAtaka

                    cls.tekstStetaSubekt[0] = True
                    cls.scrollTxtSubekt[0] = f'{cls.namyli_atakata(obekt.djasnaAtaka, subekt.zastita)}'
                    cls.scrollClrSubekt[0] = 'red'
                    print('vrag hit')
                else:
                    cls.tekstStetaSubekt[0] = True
                    cls.scrollTxtSubekt[0] = 'dodge'
                    cls.scrollClrSubekt[0] = 'white'
                    print('vrag: you dodged')
                obekt.djasnaAtakaCD = 0.01

        cls._kontrol_nad_igracyt(e, obekt, subekt)
        cls._lenta_s_dejstvija(subekt)
        cls._scrollin_combat_text(subekt, obekt)

    @classmethod
    def elit_mob(cls, e, cd, obekt, subekt):
        # global cls.countATK, cls.countATKl, cls.obektATKIsTruD, cls.obektATKIsTruL
        cls._pri_kraj(subekt, obekt)
        cls._tocki_zivot(obekt, subekt)

        txt = FONT35.render(f"{subekt.GCD:.2f}", True, Color("red"))
        EKRAN.blit(txt, (10, 550))

        subekt.cool_down_START(cd)
        obekt.cool_down_START(cd)
        subekt.global_cool_down(cd)
        obekt.global_cool_down(cd)

        if obekt.djasnaAtakaCD == 0 and obekt.GCD == 0:
            cls.obektATKIsTruD = True
        elif obekt.ljavaAtakaCD == 0 and obekt.GCD == 0:
            cls.obektATKIsTruL = True

        cls._kontrol_nad_igracyt(e, obekt, subekt)
        cls._lenta_s_dejstvija(subekt)
        cls._scrollin_combat_text(subekt, obekt)

        if cls.obektATKIsTruD:
            cls.countATK += 0.25
            if cls.countATK >= len(cls.obektATKanimacija):
                cls.countATK = 0
                cls.obektATKIsTruD = False
            else:
                EKRAN.blit(cls.obektATKanimacija[int(cls.countATK)], (cls.obektkor[0] - 200, cls.obektkor[1] - 100))

            if cls.countATK == 2:

                if randrange(1, 101) >= subekt.dodge:
                    subekt.HPnstojast -= cls.namyli_atakata(obekt.djasnaAtaka, subekt.zastita)  # obekt.djasnaAtaka

                    cls.tekstStetaSubekt[0] = True
                    cls.scrollTxtSubekt[0] = f'{cls.namyli_atakata(obekt.djasnaAtaka, subekt.zastita)}'
                    cls.scrollClrSubekt[0] = 'red'
                    print('vrag hit')
                else:
                    cls.tekstStetaSubekt[0] = True
                    cls.scrollTxtSubekt[0] = 'dodge'
                    cls.scrollClrSubekt[0] = 'white'
                    print('vrag: you dodged')
                obekt.djasnaAtakaCD = 0.01
                obekt.GCD = 0.1
        elif cls.obektATKIsTruL:
            cls.countATKl += 0.25
            if cls.countATKl >= len(cls.obektATKanimacija):
                cls.countATKl = 0
                cls.obektATKIsTruL = False
            else:
                EKRAN.blit(cls.obektATKanimacija[int(cls.countATKl)], (cls.obektkor[0] - 200, cls.obektkor[1] - 100))

            if cls.countATKl == 2:

                if randrange(1, 101) >= subekt.dodge:
                    steta = cls.namyli_atakata(obekt.ljavaAtaka, subekt.zastita)
                    subekt.HPnstojast -= steta  # obekt.djasnaAtaka

                    cls.tekstStetaSubekt[1] = True
                    cls.scrollTxtSubekt[1] = f'{steta}'
                    cls.scrollClrSubekt[1] = 'red'
                    print('vrag hit')
                else:
                    cls.tekstStetaSubekt[1] = True
                    cls.scrollTxtSubekt[1] = 'dodge'
                    cls.scrollClrSubekt[1] = 'white'
                    print('vrag: you dodged')
                obekt.ljavaAtakaCD = 0.01
                obekt.GCD = 0.1

    @classmethod
    def oficer_mob(cls, e, cd, obekt, subekt, klas_na_oficera):
        # global cls.countATK, cls.countATKl, cls.obektZastitaStart, cls.obektATKIsTruD, cls.obektATKIsTruL, cls.obektRazno, cls.obektZastita
        cls._pri_kraj(subekt, obekt)
        cls._tocki_zivot(obekt, subekt)

        txt = FONT35.render(f"{subekt.GCD:.2f}", True, Color("red"))
        EKRAN.blit(txt, (10, 550))

        subekt.cool_down_START(cd)
        obekt.cool_down_START(cd)
        subekt.global_cool_down(cd)
        obekt.global_cool_down(cd)

        if obekt.djasnaAtakaCD == 0 and obekt.GCD == 0:
            cls.obektATKIsTruD = True
        elif obekt.ljavaAtakaCD == 0 and obekt.GCD == 0:
            cls.obektATKIsTruL = True

        if obekt.raznoCD == 0:
            cls.obektRazno[0] = True

        cls._kontrol_nad_igracyt(e, obekt, subekt)
        cls._lenta_s_dejstvija(subekt)
        cls._scrollin_combat_text(subekt, obekt)

        if cls.obektATKIsTruD:
            cls.countATK += 0.25
            if cls.countATK >= len(cls.obektATKanimacija):
                cls.countATK = 0
                cls.obektATKIsTruD = False
            else:
                EKRAN.blit(cls.obektATKanimacija[int(cls.countATK)], (cls.obektkor[0] - 200, cls.obektkor[1] - 100))

            if cls.countATK == 2:

                if randrange(1, 101) >= subekt.dodge:
                    subekt.HPnstojast -= cls.namyli_atakata(obekt.djasnaAtaka, subekt.zastita)  # obekt.djasnaAtaka

                    cls.tekstStetaSubekt[0] = True
                    cls.scrollTxtSubekt[0] = f'{cls.namyli_atakata(obekt.djasnaAtaka, subekt.zastita)}'
                    cls.scrollClrSubekt[0] = 'red'
                    print('vrag hit')
                else:
                    cls.tekstStetaSubekt[0] = True
                    cls.scrollTxtSubekt[0] = 'dodge'
                    cls.scrollClrSubekt[0] = 'white'
                    print('vrag: you dodged')
                obekt.djasnaAtakaCD = 0.01
                obekt.GCD = 0.1
        elif cls.obektATKIsTruL:
            cls.countATKl += 0.25
            if cls.countATKl >= len(cls.obektATKanimacija):
                cls.countATKl = 0
                cls.obektATKIsTruL = False
            else:
                EKRAN.blit(cls.obektATKanimacija[int(cls.countATKl)], (cls.obektkor[0] - 200, cls.obektkor[1] - 100))

            if cls.countATKl == 2:

                if randrange(1, 101) >= subekt.dodge:
                    steta = cls.namyli_atakata(obekt.ljavaAtaka, subekt.zastita)
                    subekt.HPnstojast -= steta  # obekt.djasnaAtaka

                    cls.tekstStetaSubekt[1] = True
                    cls.scrollTxtSubekt[1] = f'{steta}'
                    cls.scrollClrSubekt[1] = 'red'
                    print('vrag hit')
                else:
                    cls.tekstStetaSubekt[1] = True
                    cls.scrollTxtSubekt[1] = 'dodge'
                    cls.scrollClrSubekt[1] = 'white'
                    print('vrag: you dodged')
                obekt.ljavaAtakaCD = 0.01
                obekt.GCD = 0.1

        if cls.obektRazno[0]:
            cls.countRazno[0] += 0.25
            if cls.countRazno[0] >= len(cls.animacijaZastita):
                cls.countRazno[0] = 0
                cls.obektRazno[0] = False
            else:
                EKRAN.blit(cls.animacijaZastita[int(cls.countRazno[0])], (cls.obektkor[0] - 200, cls.obektkor[1] - 420))

            if cls.countRazno[0] == 2:
                print('here')
                # print(obekt.raznoCD)
                if klas_na_oficera == '-':
                    subekt.HPnstojast -= obekt.specialno
                    cls.tekstStetaSubekt[2] = True
                    cls.scrollTxtSubekt[2] = f'{obekt.specialno}'
                    cls.scrollClrSubekt[2] = 'black'
                elif klas_na_oficera == '+':
                    obekt.HPnstojast += obekt.specialno
                    if obekt.HPnstojast > obekt.HP + int(obekt.HP * 0.15):
                        obekt.HPnstojast -= obekt.HPnstojast - (obekt.HP + int(obekt.HP * 0.15))
                elif klas_na_oficera == '0':
                    cls.obektZastita = True
                obekt.raznoCD = 0.1

        # print(obekt.zastita, subekt.zastita)
        if cls.obektZastita:
            if cls.obektZastitaStart:
                obekt.zastita += obekt.specialno
            cls.obektZastitaStart = False
            draw.rect(EKRAN, (46, 255, 252), ((cls.obektkor[0] - 50, cls.obektkor[1] - obekt.hitbox.height), (5, 300)))
            if int(obekt.raznoCD) == 4:
                obekt.zastita -= obekt.specialno
                cls.obektZastita = False
                cls.obektZastitaStart = True

        # print(obekt.ljavaAtakaCD, obekt.djasnaAtakaCD, obekt.GCD)

    @classmethod
    def bos_mob(cls, e, cd, obekt, subekt):
        # global cls.obektZastitaStart, cls.obektZastita, cls.obektATKIsTruD, cls.countATK, cls.obektATKIsTruL, cls.countATKl, cls.obektRazno
        cls._pri_kraj(subekt, obekt)
        cls._tocki_zivot(obekt, subekt)

        txt = FONT35.render(f"{subekt.GCD:.2f}", True, Color("red"))
        EKRAN.blit(txt, (10, 550))

        subekt.cool_down_START(cd)
        obekt.cool_down_START(cd)
        subekt.global_cool_down(cd)
        obekt.global_cool_down(cd)

        print(obekt.zastita)
        if obekt.djasnaAtakaCD == 0 and obekt.GCD == 0:
            cls.obektATKIsTruD = True
        elif obekt.ljavaAtakaCD == 0 and obekt.GCD == 0:
            cls.obektATKIsTruL = True
        if obekt.raznoCD == 0:
            cls.obektRazno[0] = True
        if f'{obekt.raznoCD:.2f}' == '4.01' or f'{obekt.raznoCD:.2f}' == '4.00':
            cls.obektRazno[1] = True
        if f'{obekt.raznoCD:.2f}' == '8.01' or f'{obekt.raznoCD:.2f}' == '8.00':
            cls.obektRazno[2] = True

        cls._kontrol_nad_igracyt(e, obekt, subekt)
        cls._lenta_s_dejstvija(subekt)
        cls._scrollin_combat_text(subekt, obekt)

        if cls.obektATKIsTruD:
            cls.countATK += 0.25
            if cls.countATK >= len(cls.obektATKanimacija):
                cls.countATK = 0
                cls.obektATKIsTruD = False
            else:
                EKRAN.blit(cls.obektATKanimacija[int(cls.countATK)], (cls.obektkor[0] - 200, cls.obektkor[1] - 100))

            if cls.countATK == 2:
                if randrange(1, 101) >= subekt.dodge:
                    subekt.HPnstojast -= cls.namyli_atakata(obekt.djasnaAtaka, subekt.zastita)
                    cls.tekstStetaSubekt[0] = True
                    cls.scrollTxtSubekt[0] = f'{cls.namyli_atakata(obekt.djasnaAtaka, subekt.zastita)}'
                    cls.scrollClrSubekt[0] = 'red'
                    print('vrag hit')
                else:
                    cls.tekstStetaSubekt[0] = True
                    cls.scrollTxtSubekt[0] = 'dodge'
                    cls.scrollClrSubekt[0] = 'white'
                    print('vrag: you dodged')
                obekt.djasnaAtakaCD = 0.01
                obekt.GCD = 0.1
                # cls.obektATKIsTruD = False
        elif cls.obektATKIsTruL:
            cls.countATKl += 0.25
            if cls.countATKl >= len(cls.obektATKanimacija):
                cls.countATKl = 0
                cls.obektATKIsTruL = False
            else:
                EKRAN.blit(cls.obektATKanimacija[int(cls.countATKl)], (cls.obektkor[0] - 200, cls.obektkor[1] - 100))

            if cls.countATKl == 2:

                if randrange(1, 101) >= subekt.dodge:
                    steta = cls.namyli_atakata(obekt.ljavaAtaka, subekt.zastita)
                    subekt.HPnstojast -= steta
                    cls.tekstStetaSubekt[1] = True
                    cls.scrollTxtSubekt[1] = f'{steta}'
                    cls.scrollClrSubekt[1] = 'red'
                    print('vrag hit')
                else:
                    cls.tekstStetaSubekt[1] = True
                    cls.scrollTxtSubekt[1] = 'dodge'
                    cls.scrollClrSubekt[1] = 'white'
                    print('vrag: you dodged')
                obekt.ljavaAtakaCD = 0.01
                obekt.GCD = 0.1
                # cls.obektATKIsTruL = False

        # print(f'{obekt.raznoCD:.2f}')
        if cls.obektRazno[0]:
            cls.countRazno[0] += 0.25
            if cls.countRazno[0] >= len(cls.animacijaSteta):
                cls.countRazno[0] = 0
                cls.obektRazno[0] = False
            else:
                EKRAN.blit(cls.animacijaSteta[int(cls.countRazno[0])], (cls.obektkor[0] - 200, cls.obektkor[1] - 420))

            if cls.countRazno[0] == 2:
                subekt.HPnstojast -= obekt.specialno
                cls.tekstStetaSubekt[2] = True
                cls.scrollTxtSubekt[2] = f'{obekt.specialno}'
                cls.scrollClrSubekt[2] = 'black'
                obekt.raznoCD = 0.1
        if cls.obektRazno[1]:
            cls.countRazno[1] += 0.25
            if cls.countRazno[1] >= len(cls.animacijaZivot):
                cls.countRazno[1] = 0
                cls.obektRazno[1] = False
            else:
                EKRAN.blit(cls.animacijaZivot[int(cls.countRazno[1])], (cls.obektkor[0] - 200, cls.obektkor[1] - 420))

            if cls.countRazno[1] == 2:
                obekt.HPnstojast += obekt.specialno
                if obekt.HPnstojast > obekt.HP + int(obekt.HP * 0.15):
                    obekt.HPnstojast -= obekt.HPnstojast - (obekt.HP + int(obekt.HP * 0.15))
        if cls.obektRazno[2]:
            cls.countRazno[2] += 0.25
            if cls.countRazno[2] >= len(cls.animacijaZastita):
                cls.countRazno[2] = 0
                cls.obektRazno[2] = False
            else:
                EKRAN.blit(cls.animacijaZastita[int(cls.countRazno[2])], (cls.obektkor[0] - 200, cls.obektkor[1] - 420))

            if cls.countRazno[2] == 2:
                cls.obektZastita = True

        # print(obekt.zastita, subekt.zastita)
        if cls.obektZastita:
            if cls.obektZastitaStart:
                obekt.zastita += obekt.specialno
            cls.obektZastitaStart = False
            draw.rect(EKRAN, (46, 255, 252), ((cls.obektkor[0] - 50, cls.obektkor[1] - obekt.hitbox.height), (5, 300)))
            if int(obekt.raznoCD) == 4:
                obekt.zastita -= obekt.specialno
                cls.obektZastita = False
                cls.obektZastitaStart = True

    @classmethod
    def _pri_kraj(cls, subekt, obekt):
        # global cls.tresenieProdylzitelnost, cls.tekstStetaSubekt, cls.randoSubekt, cls.korSubekt, cls.scrollTxtSubekt, cls.scrollClrSubekt, cls.tekstStetaObekt, cls.randoObekt, cls.korObekt, \
        #    cls.scrollTxtObekt, cls.scrollTxtObekt, cls.scrollClrObekt, cls.scrollSizeObekt, cls.obektZastita, cls.obektZastitaStart, cls.healOverTime, cls.defUp, cls.defStart, cls.stypka, cls.obektKryvX, \
        #    cls.subektkor, cls.subektKryvX, cls.subektlj, cls.subektdj, cls.subektrz, cls.subektGCD, cls.jj, cls.countATK, cls.countATKl, cls.obektATKIsTruD, cls.obektATKIsTruL, cls.obektRazno

        if obekt.HPnstojast <= 0 or subekt.HPnstojast <= 0:
            # cls.jj = 1
            if subekt.HPnstojast <= 0:
                print(f'{obekt.ime} wins')
            else:
                print('IGTACYT wins')
            # subekt.vel = 5
            obekt.HPnstojast = obekt.HP
            subekt.HPnstojast = subekt.HP

            obekt.boj = False

            subekt.ljavaAtakaCD = 0
            subekt.djasnaAtakaCD = 0
            obekt.djasnaAtakaCD = 0
            obekt.ljavaAtakaCD = 0
            obekt.GCD = 0
            subekt.GCD = 0

            if cls.obektZastita:
                obekt.zastita -= obekt.specialno

            cls.syzdaj_promenlivi()
            return

    @classmethod
    def _kontrol_nad_igracyt(cls, e, obekt, subekt):
        # global cls.stypka, cls.defStart, cls.defStart, cls.healOverTime, cls.defUp, cls.tresenieProdylzitelnost
        if e.type == KEYDOWN and subekt.GCD == 0:
            # subekt.GCD = 0.1

            if e.key == K_1 and subekt.ljavaAtakaCD == 0 and subekt.ljavaAtakaMAX > 0:
                if randrange(1, 101) <= subekt.hitChance:
                    if randrange(1, 101) <= subekt.crit:
                        print('crit atacka')
                        cls.tresenieProdylzitelnost = 50
                        steta = cls.namyli_atakata(
                            ((subekt.ljavaAtaka + subekt.atkBonusl) * max(subekt.critMultiplier)), obekt.zastita)
                        obekt.HPnstojast -= steta
                        cls.tekstStetaObekt[0] = True
                        cls.scrollTxtObekt[0] = f'CRIT {steta}'
                        cls.scrollClrObekt[0] = 'green'
                        cls.scrollSizeObekt[0] = 2
                    else:
                        print('standarta ataka')
                        steta = cls.namyli_atakata((subekt.ljavaAtaka + subekt.atkBonusl), obekt.zastita)
                        obekt.HPnstojast -= steta
                        cls.tekstStetaObekt[0] = True
                        cls.scrollTxtObekt[0] = f'{steta}'
                        cls.scrollClrObekt[0] = 'red'
                else:
                    print('miss')
                    cls.tekstStetaObekt[0] = True
                    cls.scrollTxtObekt[0] = 'Miss'
                    cls.scrollClrObekt[0] = 'white'
                subekt.ljavaAtakaCD = 0.01
                subekt.GCD = 0.1
            if e.key == K_2 and subekt.djasnaAtakaCD == 0 and subekt.djasnaAtakaMAX > 0:
                if randrange(1, 101) <= subekt.hitChance:
                    if randrange(1, 101) <= subekt.crit:
                        print('crit atacka')
                        cls.tresenieProdylzitelnost = 50
                        steta = cls.namyli_atakata(
                            ((subekt.djasnaAtaka + subekt.atkBonusd) * max(subekt.critMultiplier)), obekt.zastita)
                        obekt.HPnstojast -= steta
                        cls.tekstStetaObekt[1] = True
                        cls.scrollTxtObekt[1] = f'CRIT {steta}'
                        cls.scrollClrObekt[1] = 'green'
                        cls.scrollSizeObekt[1] = 2
                    else:
                        print('silna ataka')
                        steta = cls.namyli_atakata((subekt.djasnaAtaka + subekt.atkBonusd), obekt.zastita)
                        obekt.HPnstojast -= steta
                        cls.tekstStetaObekt[1] = True
                        cls.scrollTxtObekt[1] = f'{steta}'
                        cls.scrollClrObekt[1] = 'red'
                else:
                    print('miss')
                    cls.tekstStetaObekt[1] = True
                    cls.scrollTxtObekt[1] = 'Miss'
                    cls.scrollClrObekt[1] = 'white'
                subekt.djasnaAtakaCD = 0.01
                subekt.GCD = 0.1
            if e.key == K_q and subekt.raznoCD == 0 and subekt._raznoto:
                print('razno')
                if subekt._raznoto[0].HP != 0:
                    subekt.HPnstojast += subekt._raznoto[0].HP
                    if subekt._raznoto[0].damage != 0:
                        obekt.HPnstojast -= subekt._raznoto[0].damage
                        cls.tekstStetaObekt[2] = True
                        cls.scrollTxtObekt[2] = f'{subekt._raznoto[0].damage}'
                        cls.scrollClrObekt[2] = 'black'
                    if subekt.HPnstojast > subekt.HP:
                        subekt.HPnstojast -= subekt.HPnstojast - subekt.HP
                elif subekt._raznoto[0].heal_per_second != 0:
                    cls.healOverTime = True
                elif subekt._raznoto[0].def_per_secod != 0:
                    cls.defUp = True

                    # obekt.HPnstojast -=
                subekt.GCD = 0.1
                subekt.raznoCD = 0.01
            if e.key == K_0:
                subekt.HPnstojast = 0

        # print(subekt.zastita)
        if cls.healOverTime:
            if int(subekt.raznoCD) == subekt._raznoto[0].heal_per_second[1]:
                cls.healOverTime = False
                cls.stypka = 0
            elif int(subekt.raznoCD) == subekt._raznoto[0].heal_per_second[1] - subekt._raznoto[0].heal_per_second[
                1] + cls.stypka:
                subekt.HPnstojast += subekt._raznoto[0].heal_per_second[0]
                if subekt.HPnstojast > subekt.HP:
                    subekt.HPnstojast -= subekt.HPnstojast - subekt.HP
                if int(subekt.raznoCD) <= subekt._raznoto[0].heal_per_second[1]:
                    cls.stypka += 1
        elif cls.defUp:
            if cls.defStart:
                subekt.zastita += subekt._raznoto[0].def_per_secod[0]
            cls.defStart = False
            draw.rect(EKRAN, (46, 255, 252), ((350, 150), (5, 300)))
            if int(subekt.raznoCD) == subekt._raznoto[0].def_per_secod[1]:
                cls.defUp = False
                cls.defStart = True
                subekt.zastita -= subekt._raznoto[0].def_per_secod[0]

    @classmethod
    def _scrollin_combat_text(cls, subekt, obekt):
        # subekt
        if cls.tekstStetaObekt[0]:
            if cls.randoObekt[0]:
                x, y = randrange(cls.obektkor[0], cls.obektkor[0] + 100), randrange(cls.obektkor[1],
                                                                                    cls.obektkor[1] + 100)
                cls.korObekt[0].append(x)
                cls.korObekt[0].append(y)
            cls.randoObekt[0] = False
            txt = font.Font(SRIFT, 40 * cls.scrollSizeObekt[0]).render(cls.scrollTxtObekt[0], True,
                                                                       Color(cls.scrollClrObekt[0]))

            EKRAN.blit(txt, (cls.korObekt[0][0], cls.korObekt[0][1] - subekt.ljavaAtakaCD * 150))
            if subekt.ljavaAtakaCD >= 1:
                cls.tekstStetaObekt[0] = False
                cls.randoObekt[0] = True
                cls.korObekt[0] = []
                cls.scrollSizeObekt[0] = 1
        if cls.tekstStetaObekt[1]:
            if cls.randoObekt[1]:
                x, y = randrange(cls.obektkor[0], cls.obektkor[0] + 100), randrange(cls.obektkor[1],
                                                                                    cls.obektkor[1] + 100)
                cls.korObekt[1].append(x)
                cls.korObekt[1].append(y)
            cls.randoObekt[1] = False
            txt2 = font.Font(SRIFT, 40 * cls.scrollSizeObekt[1]).render(cls.scrollTxtObekt[1], True,
                                                                        Color(cls.scrollClrObekt[1]))

            EKRAN.blit(txt2, (cls.korObekt[1][0], cls.korObekt[1][1] - subekt.djasnaAtakaCD * 150))
            if subekt.djasnaAtakaCD >= 1:
                cls.tekstStetaObekt[1] = False
                cls.randoObekt[1] = True
                cls.korObekt[1] = []
                cls.scrollSizeObekt[1] = 1
        if cls.tekstStetaObekt[2]:
            if cls.randoObekt[2]:
                x, y = randrange(cls.obektkor[0], cls.obektkor[0] + 100), randrange(cls.obektkor[1],
                                                                                    cls.obektkor[1] + 100)
                cls.korObekt[2].append(x)
                cls.korObekt[2].append(y)
            cls.randoObekt[2] = False
            txt2 = font.Font(SRIFT, 40 * cls.scrollSizeObekt[2]).render(cls.scrollTxtObekt[2], True,
                                                                        Color(cls.scrollClrObekt[2]))

            EKRAN.blit(txt2, (cls.korObekt[2][0], cls.korObekt[2][1] - subekt.raznoCD * 150))
            if subekt.raznoCD >= 1:
                cls.tekstStetaObekt[2] = False
                cls.randoObekt[2] = True
                cls.korObekt[2] = []
                cls.scrollSizeObekt[2] = 1

        # obekt
        if cls.tekstStetaSubekt[0]:
            if cls.randoSubekt[0]:
                x, y = randrange(cls.subektkor[0] - 50, cls.subektkor[0]), randrange(cls.subektkor[1],
                                                                                     cls.subektkor[1] + 50)
                cls.korSubekt[0].append(x)
                cls.korSubekt[0].append(y)
            cls.randoSubekt[0] = False
            txt = FONT40.render(cls.scrollTxtSubekt[0], True, Color(cls.scrollClrSubekt[0]))

            EKRAN.blit(txt, (cls.korSubekt[0][0], cls.korSubekt[0][1] - obekt.djasnaAtakaCD * 150))
            if obekt.djasnaAtakaCD >= 1:
                cls.tekstStetaSubekt[0] = False
                cls.randoSubekt[0] = True
                cls.korSubekt[0] = []
        if cls.tekstStetaSubekt[1]:
            if cls.randoSubekt[1]:
                x, y = randrange(cls.subektkor[0] - 50, cls.subektkor[0]), randrange(cls.subektkor[1],
                                                                                     cls.subektkor[1] + 50)
                cls.korSubekt[1].append(x)
                cls.korSubekt[1].append(y)
            cls.randoSubekt[1] = False
            txt = FONT40.render(cls.scrollTxtSubekt[1], True, Color(cls.scrollClrSubekt[1]))

            EKRAN.blit(txt, (cls.korSubekt[1][0], cls.korSubekt[1][1] - obekt.ljavaAtakaCD * 150))
            if obekt.ljavaAtakaCD >= 1:
                cls.tekstStetaSubekt[1] = False
                cls.randoSubekt[1] = True
                cls.korSubekt[1] = []
        if cls.tekstStetaSubekt[2]:
            if cls.randoSubekt[2]:
                x, y = randrange(cls.subektkor[0] - 50, cls.subektkor[0]), randrange(cls.subektkor[1],
                                                                                     cls.subektkor[1] + 50)
                cls.korSubekt[2].append(x)
                cls.korSubekt[2].append(y)
            cls.randoSubekt[2] = False
            txt = FONT40.render(cls.scrollTxtSubekt[2], True, Color(cls.scrollClrSubekt[2]))

            EKRAN.blit(txt, (cls.korSubekt[2][0], cls.korSubekt[2][1] - obekt.raznoCD * 150))
            if obekt.raznoCD >= 1:
                cls.tekstStetaSubekt[2] = False
                cls.randoSubekt[2] = True
                cls.korSubekt[2] = []

    @classmethod
    def _lenta_s_dejstvija(cls, subekt):
        # global cls.subektrz, cls.subektdj, cls.subektlj, cls.subektGCD
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

        EKRAN.blit(cls.predajse, (dvizX + 60 * 6, dvizY))

        if subekt.GCD != 0:
            # print('d', subekt.GCD)
            cls.subektGCD = int(250 - (250 * (subekt.GCD / subekt.GCDmax)))
            # print(cls.subektGCD)
            cls.gcdIkonka.set_alpha(cls.subektGCD)
        else:
            cls.gcdIkonka.set_alpha(0)

        if subekt.ljavaAtakaCD != 0:
            cls.subektlj = int(50 - (50 * (subekt.ljavaAtakaCD / subekt.ljavaAtakaMAX)))
            k1 = Rect((dvizX, dvizY), (cls.subektlj, 50))
            cls.cooldownIkonka.set_alpha(200)
            EKRAN.blit(transform.scale(cls.cooldownIkonka, (cls.subektlj, 50)), k1)
        if subekt.djasnaAtakaCD != 0:
            cls.subektdj = int(50 - (50 * (subekt.djasnaAtakaCD / subekt.djasnaAtakaMAX)))
            k2 = Rect((dvizX + 60, dvizY), (cls.subektdj, 50))
            cls.cooldownIkonka.set_alpha(200)
            EKRAN.blit(transform.scale(cls.cooldownIkonka, (cls.subektdj, 50)), k2)
        if subekt.raznoCD != 0:
            cls.subektrz = int(50 - (50 * (subekt.raznoCD / subekt.raznoCDMAX)))
            k3 = Rect((dvizX + 120, dvizY), (cls.subektrz, 50))
            cls.cooldownIkonka.set_alpha(200)
            EKRAN.blit(transform.scale(cls.cooldownIkonka, (cls.subektrz, 50)), k3)
        # draw.rect(EKRAN, (11, 158, 126), ((dvizX, dvizY), (4 * 50 + 4 * 10, cls.subektGCD)))
        EKRAN.blit(cls.gcdIkonka, (dvizX, dvizY))

    @classmethod
    def _tocki_zivot(cls, obekt, subekt):
        # global cls.jj, cls.subektKrvPromenliv, cls.obektKrvPromenliv, cls.obektKryvX, cls.subektKryvX
        cls.obektKryvX = obekt.HPnstojast / (obekt.HP / 200)
        cls.subektKryvX = subekt.HPnstojast / (subekt.HP / 200)
        # print(cls.obektKrvPromenliv, cls.jj)

        # print(cls.jj, obekt.boj)
        if cls.jj and obekt.boj:
            temps = [subekt.HPnstojast].copy()
            cls.subektKrvPromenliv = temps[0]
            temps2 = [obekt.HPnstojast].copy()
            cls.obektKrvPromenliv = temps2[0]
            # print(cls.subektKrvPromenliv, cls.obektKrvPromenliv)
            cls.jj = False
            return

        prahodnaDylzinaSubect = 0
        prahodnaDylzinaObekt = 0
        prehodenCvjatSubekt = (0, 0, 255)
        prehodenCvjatObekt = (0, 0, 255)

        if cls.subektKrvPromenliv < subekt.HPnstojast:
            cls.subektKrvPromenliv += 0.2
            prahodnaDylzinaSubect = int(-(subekt.HPnstojast - cls.subektKrvPromenliv) / (subekt.HP / 200))
            prehodenCvjatSubekt = (0, 255, 0)
        if cls.subektKrvPromenliv > subekt.HPnstojast:
            cls.subektKrvPromenliv -= 0.2
            prahodnaDylzinaSubect = int(-(subekt.HPnstojast - cls.subektKrvPromenliv) / (subekt.HP / 200))
            prehodenCvjatSubekt = (255, 255, 0)

        # subekt
        graniciZivotSubekt = Surface((207, 27))
        graniciZivotSubekt.fill((255, 255, 255))
        nastKryv = Rect((3, 3), (cls.subektKryvX, 20))
        fixedKv = Rect((3, 3), (200, 20))
        draw.rect(graniciZivotSubekt, (255, 0, 0), fixedKv)  # cervenija von na tockite zivot
        draw.rect(graniciZivotSubekt, (0, 255, 0), nastKryv)  # zelenija cjavt na tockite zivot, kojto namaljava
        ljNastojasto = FONT18.render(f'{subekt.HPnstojast}', False, (0, 0, 0))
        djMaksimalno = FONT18.render(f'{subekt.HP}', False, (0, 0, 0))
        draw.rect(graniciZivotSubekt, prehodenCvjatSubekt,
                  (nastKryv.right, nastKryv.y, prahodnaDylzinaSubect,
                   20))  # zyltata/zelenata lenta na promjanata v tockite zivot
        graniciZivotSubekt.blit(ljNastojasto, (fixedKv.left + 5, fixedKv.y - 4))
        graniciZivotSubekt.blit(djMaksimalno, (fixedKv.right - 30, fixedKv.y - 4))
        EKRAN.blit(graniciZivotSubekt, (cls.subektkor[0] - 10, cls.subektkor[1] + 230))

        if cls.obektKrvPromenliv < obekt.HPnstojast:
            cls.obektKrvPromenliv += 0.2
            prahodnaDylzinaObekt = int(-(obekt.HPnstojast - cls.obektKrvPromenliv) / (obekt.HP / 200))
            prehodenCvjatObekt = (0, 255, 0)
        if cls.obektKrvPromenliv > obekt.HPnstojast:
            cls.obektKrvPromenliv -= 0.2
            prahodnaDylzinaObekt = int(-(obekt.HPnstojast - cls.obektKrvPromenliv) / (obekt.HP / 200))
            prehodenCvjatObekt = (255, 255, 0)

        # obekt
        graniciZivotObekt = Surface((207, 27))
        graniciZivotObekt.fill((255, 255, 255))
        nastKryv1 = Rect((3, 3), (cls.obektKryvX, 20))
        fixedKv1 = Rect((3, 3), (200, 20))
        draw.rect(graniciZivotObekt, (255, 0, 0), fixedKv1)  # cervenija von na tockite zivot
        draw.rect(graniciZivotObekt, (0, 255, 0), nastKryv1)  # zelenija cjavt na tockite zivot, kojto namaljava
        nastojasto = FONT18.render(f'{obekt.HPnstojast}', False, (0, 0, 0))
        maksimalno = FONT18.render(f'{obekt.HP}', False, (0, 0, 0))
        draw.rect(graniciZivotObekt, prehodenCvjatObekt,
                  (nastKryv1.right, nastKryv1.y, prahodnaDylzinaObekt,
                   20))  # zyltata/zelenata lenta na promjanata v tockite zivot
        graniciZivotObekt.blit(nastojasto, (fixedKv1.left + 5, fixedKv1.y - 4))
        graniciZivotObekt.blit(maksimalno, (fixedKv1.right - 30, fixedKv1.y - 4))
        EKRAN.blit(graniciZivotObekt, (cls.obektkor[0] - 10, cls.obektkor[1] + 130))

    @classmethod
    def namyli_atakata(cls, ataka, zastita):
        if ataka - zastita <= 0:
            return 1
        return ataka - zastita


Combats.syzdaj_promenlivi()
