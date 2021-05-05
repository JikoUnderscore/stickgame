"""

GAME ENGINE - in progress build

"""
from pygame import *
from Cuzd import newRender
from Oborudvane import TIPOVE_ORYZIJA, TIPOVE_BRONI, sakk
from Postojanni import MAP, poslednaZona, dvizenie, EKRAN, FPS, FONT15, FONT20, FONT22, FONT25, FONT28, FONT35, nastojastaZona
from vojna import Combats as Combat, CD
from json import load

_cash_sak = []
_selected_details_stop = 0
_dvizeniie_miska = True


class Sprite:
    """
    Osnovite na vjaka rusinka,

    Nasledjava se za da moze da se risuva klasyt na ekrana.

    """

    def __init__(self, figura, kor_x, kor_y, hitbox_promeni_y=None, hitbox_promeni_x=None, ikonka=None, ime='???'):
        self.covece = image.load(figura).convert_alpha()
        self.dylzina, self.visocina = self.covece.get_size()
        self.hitbox = self.covece.get_rect()
        self.korX = kor_x
        self.korY = kor_y
        self.hitbox.x = kor_x
        self.hitbox.y = kor_y
        self.promjanaY = 0
        self.promjanaX = 0
        self.ime = ime

        if hitbox_promeni_y is not None:
            self.hitbox.height = self.covece.get_height() - hitbox_promeni_y[1]
            self.promjanaY = hitbox_promeni_y[0]
        if hitbox_promeni_x is not None:
            self.hitbox.width = self.covece.get_width() - hitbox_promeni_x[1]
            self.promjanaX = hitbox_promeni_x[0]

        if ikonka is not None:
            self.ikonka = image.load(ikonka).convert_alpha()
        else:
            self.ikonka = image.load('data/tekstIkona.png').convert()

    # def __del__(self):
    #     print(f'{self}/{self.ime} is deleted !!!')

    def narisuvane(self):
        EKRAN.blit(self.covece, (self.hitbox.x - self.promjanaX, self.hitbox.y - self.promjanaY))
        draw.rect(EKRAN, (255, 0, 0), self.hitbox, 2)

    def __del__(self):
        print(self, 'deleted')


class Igrac(Sprite, CD):
    _poslednoMahnato = []
    _it1Predmetyt = []
    _it2Predmetyt = []
    # _kov = 0
    _y_move = 0

    _sakk_toggle = False

    _ljavoOryzie = []
    _djasnoOryzie = []
    _sapkata = []
    _gornisteto = []
    _dolnisteto = []
    _obuvkite = []
    _prystenyt1, _prystenyt2 = [], []
    _raznoto = []
    _znackata = []
    _lj, _dj = 0, 0
    _s, _g, _d, _o = 0, 0, 0, 0
    _p1, _p2 = 0, 0
    _r, _z = 0, 0

    _igrac_info = 0
    bagazPopInfo = []
    cervenoPremahvane = [False] * 10
    poCerenPyt = 20

    kovaneTipBronja = set()
    kovaneMarkiranTip = [(0, 0, 0), (0, 0, 0), False]

    def __init__(self, figura, kor_x, kor_y, hitbox_promeni_y=None, hitbox_promeni_x=None):
        Sprite.__init__(self, figura, kor_x, kor_y, hitbox_promeni_y, hitbox_promeni_x)
        CD.__init__(self)
        self.vel = 5
        self.playerPosX = self.korX
        self._invent = image.load('data/bagazicovek2.png').convert_alpha()

        self.atkBonusl = 0
        self.atkBonusd = 0

        self.praznoMjasto = image.load('data/ikonki/praznomjasto.png').convert_alpha()
        self.sapkaIkonka = image.load('data/ikonki/0sapka.png').convert()
        self.gornisteIkonka = image.load('data/ikonki/0teniska.png').convert()
        self.dolnisteIkonka = image.load('data/ikonki/0gasti.png').convert()
        self.obuvkiIkonka = image.load('data/ikonki/0obuvki.png').convert()
        self.prystenIkonka = image.load('data/ikonki/0prysten.png').convert()
        self.raznoIkonka = image.load('data/ikonki/0razno.png').convert()
        self.znackaIkonka = image.load('data/ikonki/0znacka.png').convert()

        self.oryzieIkonka = image.load('data/ikonki/0mec.png').convert()
        self.kovacev = image.load('data/sakk.png').convert_alpha()
        self.kovacevHittbox = self.kovacev.get_rect()

    def bagaz_v_ranicata(self, e):
        global _dvizeniie_miska
        if e.type == KEYUP:
            if e.key == K_i:
                Igrac._sakk_toggle = not Igrac._sakk_toggle
                _dvizeniie_miska = not _dvizeniie_miska
                Igrac._y_move = 0
                _cash_sak.clear()
                Igrac._poslednoMahnato.clear()
        if self._sakk_toggle:
            x, y = mouse.get_pos()
            xx, yy = 450, 150
            EKRAN.blit(self._invent, (0, 0))
            num_y = 0
            num_x = 0

            if self._igrac_info == 0:
                igranSpravka = Rect(20, 50, 130, 220)
                draw.rect(self._invent, (255, 255, 255), igranSpravka)

                f = {"Health: ": f'{self.HP}', 'attack: ': f'{self.ljavaAtaka}+{self.atkBonusl}/{self.djasnaAtaka}+{self.atkBonusd}',
                     'attack CD: ': f'{self.ljavaAtakaMAX}/{self.djasnaAtakaMAX}', 'def: ': f'{self.zastita}', 'Atk power: ': f'{self.attackPower}',
                     'hitchance: ': f'{self.hitChance}%', 'dodge: ': f'{self.dodge}', 'CritChance: ': f'{self.crit}',
                     'CritMultiplier : ': f'{max(self.critMultiplier)}', 'raznoCD: ': f'{self.raznoCDMAX}'}
                n = 0
                for k, v in f.items():
                    tt = FONT15.render(k + v, False, Color('black'))
                    self._invent.blit(tt, (igranSpravka.x, igranSpravka.y + n))
                    n += 20
                Igrac._igrac_info = 1

            if _cash_sak:
                global _selected_details_stop
                if _selected_details_stop:
                    r = draw.rect(self._invent, (221, 226, 240), (25, 369, 377, 315))

                    d = {'Name:': f'{_cash_sak[0].raw_name}', 'Type:': f'{_cash_sak[0].tip}', 'Atk:': f"{_cash_sak[0].attack}",
                         'Def:': f'{_cash_sak[0].defence}', '+HP:': f'{_cash_sak[0].HP}', 'Use CD:': f'{_cash_sak[0].cooldown}',
                         'DMG:': f'{_cash_sak[0].damage}',
                         'AtkPower': f'{_cash_sak[0].attackPower}', 'HitChance': f'{_cash_sak[0].hitChance}',
                         'CritMultiplier': f'{_cash_sak[0].critMultiplier}',
                         'CritChance': f'{_cash_sak[0].crit}', 'Special: ': f'{_cash_sak[0].note}', 'Dodge': f'{_cash_sak[0].dodge}',
                         chr(int('0x2C0F', 16)) + ':': f'{_cash_sak[0].value}'}
                    m = 0
                    for k, v in d.items():
                        ime = FONT22.render(k, False, Color("black"))
                        imekor = [r.x, r.y + m]
                        stoinost = FONT22.render(v[0:18], False, (2, 71, 2))
                        kvstoinost = stoinost.get_rect()
                        kvstoinost.right = r.right - 5
                        kvstoinost.y = r.y + m

                        if v != '0':
                            if k == chr(int('0x2C0F', 16)) + ':':
                                kvstoinost.bottom = r.bottom
                                imekor[0] = kvstoinost.left - 35
                                imekor[1] = r.bottom - 32

                            if k == 'Special: ':
                                kvstoinost.x = 110

                            self._invent.blit(ime, imekor)
                            self._invent.blit(stoinost, kvstoinost)
                            m += 25
                            if len(v) > 18:
                                kvstoinost.y += 25
                                kvstoinost.x = imekor[0]
                                self._invent.blit(FONT22.render(v[18:], False, (2, 71, 2)), kvstoinost)
                                m += 25

                    _selected_details_stop = 0

            if mouse.get_pressed(3)[2]:
                _cash_sak.clear()
            igranici = draw.rect(self._invent, (0, 0, 255), (430, 145, 625, 540))
            krk = Rect((self._invent.get_width() - 45, 13, 40, 40))

            if _cash_sak:
                EKRAN.blit(_cash_sak[0].ikonka, (x, y))

            if krk.collidepoint(x, y):
                if mouse.get_pressed(3)[0]:
                    Igrac._sakk_toggle = False
                    _dvizeniie_miska = True
                    Igrac._y_move = 0
                    _cash_sak.clear()
                    Igrac._poslednoMahnato.clear()
            kraenpredmet = set()
            for n, i in sakk:
                xrer = Rect(xx + num_x, yy + num_y + self._y_move, 50, 50)
                kraenpredmet.add(xrer.bottom)
                if xrer.collidepoint(x, y):
                    txt = f"{n} / {i.tip}"
                    infurma = FONT22.render(txt, False, Color("white"), (0, 0, 0))
                    kvinfurma = infurma.get_rect()
                    kvinfurma.x = x + 20
                    kvinfurma.y = y
                    if kvinfurma.right >= self._invent.get_width():
                        kvinfurma.right = self._invent.get_width()
                    EKRAN.blit(infurma, kvinfurma)

                    if mouse.get_pressed(3)[0]:
                        _cash_sak.clear()
                        _selected_details_stop = 1
                        _cash_sak.append(i)
                if igranici.top < xrer.bottom and igranici.bottom > xrer.top:
                    draw.rect(self._invent, (0, 0, 0), xrer, 4)
                    self._invent.blit(i.ikonka, xrer)

                    if i.quantity >= 2:
                        infurma2 = FONT15.render(f' {i.quantity}', False, Color("white"), (0, 0, 0))
                        kvinfurma2 = infurma2.get_rect()
                        kvinfurma2.bottomright = xrer.bottomright
                        self._invent.blit(infurma2, kvinfurma2)

                num_x += 60
                if num_x >= 60 * 10:
                    num_x = 0
                    num_y += 60

            if e.type == MOUSEBUTTONDOWN:
                if e.button == 4 and min(kraenpredmet) - 50 < igranici.top:
                    Igrac._y_move += 60
                elif e.button == 5 and max(kraenpredmet) > igranici.bottom:
                    Igrac._y_move -= 60

            self._vyoryzi_ljavo(e)
            self._vyoryzi_djasno(e)
            self._sapka(e)
            self._gorniste(e)
            self._dolniste(e)
            self._obuvki(e)
            self._prysten1(e)
            self._prysten2(e)
            self._razno(e)
            self._znacka(e)

            # Dva izkacasti butona
            if self.bagazPopInfo:
                sinjo = Rect((self.bagazPopInfo[0].centerx - 100, self.bagazPopInfo[0].bottom), (100, 50))
                cerveno = Rect((self.bagazPopInfo[0].centerx, self.bagazPopInfo[0].bottom), (100, 50))

                draw.rect(EKRAN, (255, 0, 0), cerveno)
                draw.rect(EKRAN, (0, 0, 255), sinjo)

                if sinjo.collidepoint(x, y) and mouse.get_pressed(3)[0]:
                    print('sinjo')
                    _cash_sak.clear()
                    _cash_sak.append(self.bagazPopInfo[1])
                    _selected_details_stop = 1
                    self.bagazPopInfo.clear()
                elif cerveno.collidepoint(x, y) and mouse.get_pressed(3)[0]:
                    print('cerveno')
                    cislo = None
                    if self.bagazPopInfo[1].tip == 'Hat':
                        cislo = 0
                    elif self.bagazPopInfo[1].tip == 'Chest':
                        cislo = 1
                    elif self.bagazPopInfo[1].tip == 'Legs':
                        cislo = 2
                    elif self.bagazPopInfo[1].tip == 'Boot':
                        cislo = 3
                    elif self.bagazPopInfo[1].tip == 'Finger' and self.bagazPopInfo[0].y == 110:
                        cislo = 4
                    elif self.bagazPopInfo[1].tip == 'Finger' and self.bagazPopInfo[0].y == 170:
                        cislo = 5
                    elif self.bagazPopInfo[1].tip == 'Mis':
                        cislo = 6
                    elif self.bagazPopInfo[1].tip == 'Trinket':
                        cislo = 7
                    elif self.bagazPopInfo[1].tip in TIPOVE_ORYZIJA and self.bagazPopInfo[0].x == 200:
                        cislo = 8
                    elif self.bagazPopInfo[1].tip in TIPOVE_ORYZIJA and self.bagazPopInfo[0].x == 270:
                        cislo = 9
                    self.cervenoPremahvane[cislo] = True
                    self.bagazPopInfo.clear()

    def _dobavjane(self, spisyk, ljavo=True, djasno=True):
        for n, add in enumerate(spisyk):
            if add != 0:
                if n == 0 and ljavo:
                    self.ljavaAtaka = self.ljavaAtaka + add
                elif n == 1 and djasno:
                    self.djasnaAtaka = self.djasnaAtaka + add
                elif n == 2:
                    self.zastita = self.zastita + add
                elif n == 3:
                    self.HP = self.HP + add
                    self.HPnstojast = self.HP
                elif n == 4 and ljavo:
                    self.ljavaAtakaMAX = self.ljavaAtakaMAX + add
                elif n == 5 and djasno:
                    self.djasnaAtakaMAX = self.djasnaAtakaMAX + add
                elif n == 6:
                    self.attackPower = self.attackPower + add
                    self.atkBonusl = round((self.attackPower / 10))
                    self.atkBonusd = round((self.attackPower / 10))
                elif n == 7:
                    self.crit = self.crit + add
                elif n == 8:
                    self.critMultiplier.append(add)
                elif n == 9:
                    self.hitChance = self.hitChance + add
                elif n == 10:
                    self.dodge = self.dodge + add
        Igrac._igrac_info = 0

    def _premahvane(self, spisyk, ljavo=True, djasno=True):
        for n, add in enumerate(spisyk):
            if add != 0:
                if n == 0 and ljavo:
                    self.ljavaAtaka = self.ljavaAtaka - add
                elif n == 1 and djasno:
                    self.djasnaAtaka = self.djasnaAtaka - add
                elif n == 2:
                    self.zastita = self.zastita - add
                elif n == 3:
                    self.HP = self.HP - add
                    self.HPnstojast = self.HP
                elif n == 4 and ljavo:
                    self.ljavaAtakaMAX = self.ljavaAtakaMAX - add
                elif n == 5 and djasno:
                    self.djasnaAtakaMAX = self.djasnaAtakaMAX - add
                elif n == 6:
                    self.attackPower = self.attackPower - add
                    self.atkBonusl = round((self.attackPower / 10))
                    self.atkBonusd = round((self.attackPower / 10))
                elif n == 7:
                    self.crit = self.crit - add
                elif n == 8:
                    self.critMultiplier.remove(add)
                elif n == 9:
                    self.hitChance = self.hitChance - add
                elif n == 10:
                    self.dodge = self.dodge - add
        Igrac._igrac_info = 0

    def _sapka(self, e):
        try:
            if self._sapkata[0].tip != 'Hat':
                print(f'{self._sapkata[0].tip} is not a HAT')
                _cash_sak.clear()
                self._sapkata.clear()
        except IndexError:
            pass

        sapkaKvadrat = Rect(200, 110, 50, 50)
        if self._sapkata:
            self._invent.blit(self._sapkata[0].ikonka, sapkaKvadrat)
            if self._s == 0:
                Igrac._s = 1
                s = [
                    self._sapkata[0].attack, self._sapkata[0].attack,
                    self._sapkata[0].defence,
                    self._sapkata[0].HP,
                    self._sapkata[0].cooldown, self._sapkata[0].cooldown,
                    self._sapkata[0].attackPower,
                    self._sapkata[0].crit,
                    self._sapkata[0].critMultiplier,
                    self._sapkata[0].hitChance,
                    self._sapkata[0].dodge]
                self._dobavjane(s)
                sakk.remove(self._sapkata[0])
                _cash_sak.clear()
                return
        else:
            self._invent.blit(self.sapkaIkonka, sapkaKvadrat)

        if sapkaKvadrat.collidepoint(mouse.get_pos()) or self.cervenoPremahvane[0]:
            if e.type == MOUSEBUTTONUP and e.button == 1 and not self._sapkata or self.cervenoPremahvane[0]:
                if self._s == 1:
                    Igrac._poslednoMahnato = self._sapkata.copy()
                    s = [
                        Igrac._poslednoMahnato[0].attack, Igrac._poslednoMahnato[0].attack,
                        Igrac._poslednoMahnato[0].defence,
                        Igrac._poslednoMahnato[0].HP,
                        Igrac._poslednoMahnato[0].cooldown, Igrac._poslednoMahnato[0].cooldown,
                        Igrac._poslednoMahnato[0].attackPower,
                        Igrac._poslednoMahnato[0].crit,
                        Igrac._poslednoMahnato[0].critMultiplier,
                        Igrac._poslednoMahnato[0].hitChance,
                        Igrac._poslednoMahnato[0].dodge]
                    self._premahvane(s)
                    sakk.add(self._sapkata[0])

                self.cervenoPremahvane[0] = False
                Igrac._s = 0
                self._sapkata = _cash_sak.copy()
                del self._sapkata[1:]
                return
            elif e.type == MOUSEBUTTONUP and e.button == 1 and self._sapkata:
                print('pop')
                self.bagazPopInfo.append(sapkaKvadrat)
                self.bagazPopInfo.append(self._sapkata[0])

    def _gorniste(self, e):
        try:
            if self._gornisteto[0].tip != 'Chest':
                print(f'{self._gornisteto[0].tip} is not a Chest')
                _cash_sak.clear()
                self._gornisteto.clear()
        except IndexError:
            pass

        gornisteKvadrat = Rect(200, 170, 50, 50)
        if self._gornisteto:
            self._invent.blit(self._gornisteto[0].ikonka, gornisteKvadrat)
            if self._g == 0:
                Igrac._g = 1
                s = [
                    self._gornisteto[0].attack, self._gornisteto[0].attack,
                    self._gornisteto[0].defence,
                    self._gornisteto[0].HP,
                    self._gornisteto[0].cooldown, self._gornisteto[0].cooldown,
                    self._gornisteto[0].attackPower,
                    self._gornisteto[0].crit,
                    self._gornisteto[0].critMultiplier,
                    self._gornisteto[0].hitChance,
                    self._gornisteto[0].dodge]
                self._dobavjane(s)
                sakk.remove(self._gornisteto[0])
                _cash_sak.clear()
                return
        else:
            self._invent.blit(self.gornisteIkonka, gornisteKvadrat)

        if gornisteKvadrat.collidepoint(mouse.get_pos()) or self.cervenoPremahvane[1]:
            if e.type == MOUSEBUTTONUP and e.button == 1 and not self._gornisteto or self.cervenoPremahvane[1]:
                if self._g == 1:
                    Igrac._poslednoMahnato = self._gornisteto.copy()
                    s = [Igrac._poslednoMahnato[0].attack, Igrac._poslednoMahnato[0].attack,
                         Igrac._poslednoMahnato[0].defence,
                         Igrac._poslednoMahnato[0].HP,
                         Igrac._poslednoMahnato[0].cooldown, Igrac._poslednoMahnato[0].cooldown,
                         Igrac._poslednoMahnato[0].attackPower,
                         Igrac._poslednoMahnato[0].crit,
                         Igrac._poslednoMahnato[0].critMultiplier,
                         Igrac._poslednoMahnato[0].hitChance,
                         Igrac._poslednoMahnato[0].dodge]
                    self._premahvane(s)
                    sakk.add(self._gornisteto[0])

                self.cervenoPremahvane[1] = False
                Igrac._g = 0
                self._gornisteto = _cash_sak.copy()
                del self._gornisteto[1:]
                return
            elif e.type == MOUSEBUTTONUP and e.button == 1 and self._gornisteto:
                print('pop')
                self.bagazPopInfo.append(gornisteKvadrat)
                self.bagazPopInfo.append(self._gornisteto[0])

    def _dolniste(self, e):
        try:
            if self._dolnisteto[0].tip != 'Legs':
                print(f'{self._dolnisteto[0].tip} is not a Pants')
                _cash_sak.clear()
                self._dolnisteto.clear()
        except IndexError:
            pass

        dolnisteKvadrat = Rect(200, 230, 50, 50)
        if self._dolnisteto:
            self._invent.blit(self._dolnisteto[0].ikonka, dolnisteKvadrat)
            if self._d == 0:
                Igrac._d = 1

                s = [
                    self._dolnisteto[0].attack, self._dolnisteto[0].attack,
                    self._dolnisteto[0].defence,
                    self._dolnisteto[0].HP,
                    self._dolnisteto[0].cooldown, self._dolnisteto[0].cooldown,
                    self._dolnisteto[0].attackPower,
                    self._dolnisteto[0].crit,
                    self._dolnisteto[0].critMultiplier,
                    self._dolnisteto[0].hitChance,
                    self._dolnisteto[0].dodge]
                self._dobavjane(s)
                sakk.remove(self._dolnisteto[0])

                _cash_sak.clear()
                return
        else:
            self._invent.blit(self.dolnisteIkonka, dolnisteKvadrat)

        if dolnisteKvadrat.collidepoint(mouse.get_pos()) or self.cervenoPremahvane[2]:
            if e.type == MOUSEBUTTONUP and e.button == 1 and not self._dolnisteto or self.cervenoPremahvane[2]:
                if self._d == 1:
                    Igrac._poslednoMahnato = self._dolnisteto.copy()
                    s = [
                        Igrac._poslednoMahnato[0].attack, Igrac._poslednoMahnato[0].attack,
                        Igrac._poslednoMahnato[0].defence,
                        Igrac._poslednoMahnato[0].HP,
                        Igrac._poslednoMahnato[0].cooldown, Igrac._poslednoMahnato[0].cooldown,
                        Igrac._poslednoMahnato[0].attackPower,
                        Igrac._poslednoMahnato[0].crit,
                        Igrac._poslednoMahnato[0].critMultiplier,
                        Igrac._poslednoMahnato[0].hitChance,
                        Igrac._poslednoMahnato[0].dodge]
                    self._premahvane(s)
                    sakk.add(self._dolnisteto[0])

                self.cervenoPremahvane[2] = False
                Igrac._d = 0
                self._dolnisteto = _cash_sak.copy()
                del self._dolnisteto[1:]
                return
            elif e.type == MOUSEBUTTONUP and e.button == 1 and self._dolnisteto:
                print('pop')
                self.bagazPopInfo.append(dolnisteKvadrat)
                self.bagazPopInfo.append(self._dolnisteto[0])

    def _obuvki(self, e):
        try:
            if self._obuvkite[0].tip != 'Boot':
                print(f'{self._obuvkite[0].tip} is not a Boot')
                _cash_sak.clear()
        except IndexError:
            pass

        obuvkiKvadrat = Rect(200, 290, 50, 50)
        if self._obuvkite:
            self._invent.blit(self._obuvkite[0].ikonka, obuvkiKvadrat)
            if self._o == 0:
                Igrac._o = 1
                s = [
                    self._obuvkite[0].attack, self._obuvkite[0].attack,
                    self._obuvkite[0].defence,
                    self._obuvkite[0].HP,
                    self._obuvkite[0].cooldown, self._obuvkite[0].cooldown,
                    self._obuvkite[0].attackPower,
                    self._obuvkite[0].crit,
                    self._obuvkite[0].critMultiplier,
                    self._obuvkite[0].hitChance,
                    self._obuvkite[0].dodge]
                self._dobavjane(s)
                sakk.remove(self._obuvkite[0])
                _cash_sak.clear()
                return
        else:
            self._invent.blit(self.obuvkiIkonka, obuvkiKvadrat)

        if obuvkiKvadrat.collidepoint(mouse.get_pos()) or self.cervenoPremahvane[3]:
            if e.type == MOUSEBUTTONUP and e.button == 1 and not self._obuvkite or self.cervenoPremahvane[3]:
                if self._o == 1:
                    Igrac._poslednoMahnato = self._obuvkite.copy()
                    s = [
                        Igrac._poslednoMahnato[0].attack, Igrac._poslednoMahnato[0].attack,
                        Igrac._poslednoMahnato[0].defence,
                        Igrac._poslednoMahnato[0].HP,
                        Igrac._poslednoMahnato[0].cooldown, Igrac._poslednoMahnato[0].cooldown,
                        Igrac._poslednoMahnato[0].attackPower,
                        Igrac._poslednoMahnato[0].crit,
                        Igrac._poslednoMahnato[0].critMultiplier,
                        Igrac._poslednoMahnato[0].hitChance,
                        Igrac._poslednoMahnato[0].dodge]
                    self._premahvane(s)
                    sakk.add(self._obuvkite[0])

                self.cervenoPremahvane[3] = False
                Igrac._o = 0
                self._obuvkite = _cash_sak.copy()
                del self._obuvkite[1:]
                return
            elif e.type == MOUSEBUTTONUP and e.button == 1 and self._obuvkite:
                print('pop')
                self.bagazPopInfo.append(obuvkiKvadrat)
                self.bagazPopInfo.append(self._obuvkite[0])

    def _prysten1(self, e):
        try:
            if self._prystenyt1[0].tip != 'Finger':
                print(f'{self._prystenyt1[0].tip} is not a Finger')
                _cash_sak.clear()
                self._prystenyt1.clear()
        except IndexError:
            pass

        prystenKvadrat = Rect(340, 110, 50, 50)
        if self._prystenyt1:
            self._invent.blit(self._prystenyt1[0].ikonka, prystenKvadrat)
            if self._p1 == 0:
                Igrac._p1 = 1
                s = [
                    self._prystenyt1[0].attack, self._prystenyt1[0].attack,
                    self._prystenyt1[0].defence,
                    self._prystenyt1[0].HP,
                    self._prystenyt1[0].cooldown, self._prystenyt1[0].cooldown,
                    self._prystenyt1[0].attackPower,
                    self._prystenyt1[0].crit,
                    self._prystenyt1[0].critMultiplier,
                    self._prystenyt1[0].hitChance,
                    self._prystenyt1[0].dodge]
                self._dobavjane(s)
                sakk.remove(self._prystenyt1[0])
                _cash_sak.clear()
                return
        else:
            self._invent.blit(self.prystenIkonka, prystenKvadrat)

        if prystenKvadrat.collidepoint(mouse.get_pos()) or self.cervenoPremahvane[4]:
            if e.type == MOUSEBUTTONUP and e.button == 1 and not self._prystenyt1 or self.cervenoPremahvane[4]:
                if self._p1 == 1:
                    Igrac._poslednoMahnato = self._prystenyt1.copy()
                    s = [
                        Igrac._poslednoMahnato[0].attack, Igrac._poslednoMahnato[0].attack,
                        Igrac._poslednoMahnato[0].defence,
                        Igrac._poslednoMahnato[0].HP,
                        Igrac._poslednoMahnato[0].cooldown, Igrac._poslednoMahnato[0].cooldown,
                        Igrac._poslednoMahnato[0].attackPower,
                        Igrac._poslednoMahnato[0].crit,
                        Igrac._poslednoMahnato[0].critMultiplier,
                        Igrac._poslednoMahnato[0].hitChance,
                        Igrac._poslednoMahnato[0].dodge]
                    self._premahvane(s)
                    sakk.add(self._prystenyt1[0])

                self.cervenoPremahvane[4] = False
                Igrac._p1 = 0
                self._prystenyt1 = _cash_sak.copy()
                del self._prystenyt1[1:]
                return
            elif e.type == MOUSEBUTTONUP and e.button == 1 and self._prystenyt1:
                print('pop')
                self.bagazPopInfo.append(prystenKvadrat)
                self.bagazPopInfo.append(self._prystenyt1[0])

    def _prysten2(self, e):
        try:
            if self._prystenyt2[0].tip != 'Finger':
                print(f'{self._prystenyt2[0].tip} is not a Finger')
                _cash_sak.clear()
                self._prystenyt2.clear()
        except IndexError:
            pass

        prystenKvadrat = Rect(340, 170, 50, 50)
        if self._prystenyt2:
            self._invent.blit(self._prystenyt2[0].ikonka, prystenKvadrat)
            if self._p2 == 0:
                Igrac._p2 = 1
                s = [
                    self._prystenyt2[0].attack, self._prystenyt2[0].attack,
                    self._prystenyt2[0].defence,
                    self._prystenyt2[0].HP,
                    self._prystenyt2[0].cooldown, self._prystenyt2[0].cooldown,
                    self._prystenyt2[0].attackPower,
                    self._prystenyt2[0].crit,
                    self._prystenyt2[0].critMultiplier,
                    self._prystenyt2[0].hitChance,
                    self._prystenyt2[0].dodge]
                self._dobavjane(s)
                sakk.remove(self._prystenyt2[0])
                _cash_sak.clear()
                return
        else:
            self._invent.blit(self.prystenIkonka, prystenKvadrat)

        if prystenKvadrat.collidepoint(mouse.get_pos()) or self.cervenoPremahvane[5]:
            if e.type == MOUSEBUTTONUP and e.button == 1 and not self._prystenyt2 or self.cervenoPremahvane[5]:
                if self._p2 == 1:
                    Igrac._poslednoMahnato = self._prystenyt2.copy()
                    s = [
                        Igrac._poslednoMahnato[0].attack, Igrac._poslednoMahnato[0].attack,
                        Igrac._poslednoMahnato[0].defence,
                        Igrac._poslednoMahnato[0].HP,
                        Igrac._poslednoMahnato[0].cooldown, Igrac._poslednoMahnato[0].cooldown,
                        Igrac._poslednoMahnato[0].attackPower,
                        Igrac._poslednoMahnato[0].crit,
                        Igrac._poslednoMahnato[0].critMultiplier,
                        Igrac._poslednoMahnato[0].hitChance,
                        Igrac._poslednoMahnato[0].dodge]
                    self._premahvane(s)
                    sakk.add(self._prystenyt2[0])

                self.cervenoPremahvane[5] = False
                Igrac._p2 = 0
                self._prystenyt2 = _cash_sak.copy()
                del self._prystenyt2[1:]
                return
            elif e.type == MOUSEBUTTONUP and e.button == 1 and self._prystenyt2:
                print('pop')
                self.bagazPopInfo.append(prystenKvadrat)
                self.bagazPopInfo.append(self._prystenyt2[0])

    def _razno(self, e):
        try:
            if self._raznoto[0].tip != 'Mis':
                print(f'{self._raznoto[0].tip} is not a Mis')
                _cash_sak.clear()
                self._raznoto.clear()
        except IndexError:
            pass

        raznoKvadrat = Rect(340, 230, 50, 50)
        if self._raznoto:
            self._invent.blit(self._raznoto[0].ikonka, raznoKvadrat)
            if self._r == 0:
                Igrac._r = 1
                self.raznoCDMAX += self._raznoto[0].cooldown
                Igrac._igrac_info = 0
                sakk.remove(self._raznoto[0])
                _cash_sak.clear()
                return
        else:
            self._invent.blit(self.raznoIkonka, raznoKvadrat)

        if raznoKvadrat.collidepoint(mouse.get_pos()) or self.cervenoPremahvane[6]:
            if e.type == MOUSEBUTTONUP and e.button == 1 and not self._raznoto or self.cervenoPremahvane[6]:
                if self._r == 1:
                    Igrac._poslednoMahnato = self._raznoto.copy()
                    self.raznoCDMAX -= self._raznoto[0].cooldown
                    Igrac._igrac_info = 0
                    sakk.add(self._raznoto[0])

                self.cervenoPremahvane[6] = False
                Igrac._r = 0
                self._raznoto = _cash_sak.copy()
                del self._raznoto[1:]
                return
            elif e.type == MOUSEBUTTONUP and e.button == 1 and self._raznoto:
                print('pop')
                self.bagazPopInfo.append(raznoKvadrat)
                self.bagazPopInfo.append(self._raznoto[0])

    def _znacka(self, e):
        try:
            if self._znackata[0].tip != 'Trinket':
                print(f'{self._znackata[0].tip} is not a Trinket')
                _cash_sak.clear()
                self._znackata.clear()
        except IndexError:
            pass

        znackaKvadrat = Rect(340, 290, 50, 50)
        if self._znackata:
            self._invent.blit(self._znackata[0].ikonka, znackaKvadrat)
            if self._z == 0:
                Igrac._z = 1

                sakk.remove(self._znackata[0])

                _cash_sak.clear()
                return
        else:
            self._invent.blit(self.znackaIkonka, znackaKvadrat)

        if znackaKvadrat.collidepoint(mouse.get_pos()) or self.cervenoPremahvane[7]:
            if e.type == MOUSEBUTTONUP and e.button == 1 and not self._znackata or self.cervenoPremahvane[7]:
                if self._z == 1:
                    Igrac._poslednoMahnato = self._znackata.copy()

                    sakk.add(self._znackata[0])

                self.cervenoPremahvane[7] = False
                Igrac._z = 0
                self._znackata = _cash_sak.copy()
                del self._znackata[1:]
                return
            elif e.type == MOUSEBUTTONUP and e.button == 1:
                print('pop')
                self.bagazPopInfo.append(znackaKvadrat)
                self.bagazPopInfo.append(self._znackata[0])

    def _vyoryzi_ljavo(self, e):
        try:
            if self._ljavoOryzie[0].tip not in TIPOVE_ORYZIJA:
                print(f'{self._ljavoOryzie[0].tip} is not a weapon')
                _cash_sak.clear()
                self._ljavoOryzie.clear()
        except IndexError:
            pass

        ljavoOryzieKvadrat = Rect(200, 50, 50, 50)
        if self._ljavoOryzie:
            self._invent.blit(self._ljavoOryzie[0].ikonka, ljavoOryzieKvadrat)
            if self._lj == 0:
                Igrac._lj = 1
                s = [
                    self._ljavoOryzie[0].attack, self._ljavoOryzie[0].attack,
                    self._ljavoOryzie[0].defence,
                    self._ljavoOryzie[0].HP,
                    self._ljavoOryzie[0].cooldown, self._ljavoOryzie[0].cooldown,
                    self._ljavoOryzie[0].attackPower,
                    self._ljavoOryzie[0].crit,
                    self._ljavoOryzie[0].critMultiplier,
                    self._ljavoOryzie[0].hitChance,
                    self._ljavoOryzie[0].dodge]
                self._dobavjane(s, djasno=False)
                sakk.remove(self._ljavoOryzie[0])
                _cash_sak.clear()
                return
        else:
            self._invent.blit(self.oryzieIkonka, ljavoOryzieKvadrat)

        if ljavoOryzieKvadrat.collidepoint(mouse.get_pos()) or self.cervenoPremahvane[8]:
            if e.type == MOUSEBUTTONUP and e.button == 1 and not self._ljavoOryzie or self.cervenoPremahvane[8]:
                if self._lj == 1:
                    Igrac._poslednoMahnato = self._ljavoOryzie.copy()
                    s = [
                        Igrac._poslednoMahnato[0].attack, Igrac._poslednoMahnato[0].attack,
                        Igrac._poslednoMahnato[0].defence,
                        Igrac._poslednoMahnato[0].HP,
                        Igrac._poslednoMahnato[0].cooldown, Igrac._poslednoMahnato[0].cooldown,
                        Igrac._poslednoMahnato[0].attackPower,
                        Igrac._poslednoMahnato[0].crit,
                        Igrac._poslednoMahnato[0].critMultiplier,
                        Igrac._poslednoMahnato[0].hitChance,
                        Igrac._poslednoMahnato[0].dodge]
                    self._premahvane(s, djasno=False)
                    sakk.add(self._ljavoOryzie[0])

                self.cervenoPremahvane[8] = False
                Igrac._lj = 0
                self._ljavoOryzie = _cash_sak.copy()
                del self._ljavoOryzie[1:]
                return
            elif e.type == MOUSEBUTTONUP and e.button == 1 and self._ljavoOryzie:
                print('pop')
                self.bagazPopInfo.append(ljavoOryzieKvadrat)
                self.bagazPopInfo.append(self._ljavoOryzie[0])

    def _vyoryzi_djasno(self, e):
        try:
            if self._djasnoOryzie[0].tip not in TIPOVE_ORYZIJA:
                print(f'{self._djasnoOryzie[0].tip} is not a weapon')
                _cash_sak.clear()
                self._djasnoOryzie.clear()
        except IndexError:
            pass

        djasnoOryzieKvadrat = Rect(270, 50, 50, 50)
        if self._djasnoOryzie:
            self._invent.blit(self._djasnoOryzie[0].ikonka, djasnoOryzieKvadrat)
            if self._dj == 0:
                Igrac._dj = 1
                s = [
                    self._djasnoOryzie[0].attack, self._djasnoOryzie[0].attack,
                    self._djasnoOryzie[0].defence,
                    self._djasnoOryzie[0].HP,
                    self._djasnoOryzie[0].cooldown, self._djasnoOryzie[0].cooldown,
                    self._djasnoOryzie[0].attackPower,
                    self._djasnoOryzie[0].crit,
                    self._djasnoOryzie[0].critMultiplier,
                    self._djasnoOryzie[0].hitChance,
                    self._djasnoOryzie[0].dodge]
                self._dobavjane(s, ljavo=False)
                sakk.remove(self._djasnoOryzie[0])
                _cash_sak.clear()
                return
        else:
            self._invent.blit(self.oryzieIkonka, djasnoOryzieKvadrat)

        if djasnoOryzieKvadrat.collidepoint(mouse.get_pos()) or self.cervenoPremahvane[9]:
            if e.type == MOUSEBUTTONUP and e.button == 1 and not self._djasnoOryzie or self.cervenoPremahvane[9]:
                if self._dj == 1:
                    Igrac._poslednoMahnato = self._djasnoOryzie.copy()
                    s = [
                        Igrac._poslednoMahnato[0].attack, Igrac._poslednoMahnato[0].attack,
                        Igrac._poslednoMahnato[0].defence,
                        Igrac._poslednoMahnato[0].HP,
                        Igrac._poslednoMahnato[0].cooldown, Igrac._poslednoMahnato[0].cooldown,
                        Igrac._poslednoMahnato[0].attackPower,
                        Igrac._poslednoMahnato[0].crit,
                        Igrac._poslednoMahnato[0].critMultiplier,
                        Igrac._poslednoMahnato[0].hitChance,
                        Igrac._poslednoMahnato[0].dodge]
                    self._premahvane(s, ljavo=False)
                    sakk.add(self._djasnoOryzie[0])

                self.cervenoPremahvane[9] = False
                Igrac._dj = 0
                self._djasnoOryzie = _cash_sak.copy()
                del self._djasnoOryzie[1:]
                return
            elif e.type == MOUSEBUTTONUP and e.button == 1 and self._djasnoOryzie:
                print('pop')
                self.bagazPopInfo.append(djasnoOryzieKvadrat)
                self.bagazPopInfo.append(self._djasnoOryzie[0])

    def dvizenie(self, vyrtene_na_fona=False, plus_kolko_pyti_da_se_vyrti=0, otrezi_pri_vurtene=None, dolu=0, djasno=0, gore=0, ljavo=0):
        global _dvizeniie_miska
        if otrezi_pri_vurtene is None:
            otrezi_pri_vurtene = (0, 0)
        if not vyrtene_na_fona and _dvizeniie_miska:
            mx, my = mouse.get_pos()
            klavisNatisnat = key.get_pressed()
            if (klavisNatisnat[K_a] and self.hitbox.x > 0 + ljavo) or (
                    self.hitbox.x > 0 + ljavo and mouse.get_pressed(3)[2] and self.hitbox.centerx > mx):
                self.hitbox.x -= self.vel
            if (klavisNatisnat[K_d] and self.hitbox.x + djasno < EKRAN.get_width()) or (
                    self.hitbox.x + djasno < EKRAN.get_width() and mouse.get_pressed(3)[2] and self.hitbox.centerx < mx):
                self.hitbox.x += self.vel
            if (klavisNatisnat[K_w] and self.hitbox.y > -100 + gore) or (
                    self.hitbox.y > -100 + gore and mouse.get_pressed(3)[2] and self.hitbox.bottom > my):
                self.hitbox.y -= self.vel
            if (klavisNatisnat[K_s] and self.hitbox.y + dolu < EKRAN.get_height()) or (
                    self.hitbox.y + dolu < EKRAN.get_height() and mouse.get_pressed(3)[2] and self.hitbox.bottom < my):
                self.hitbox.y += self.vel
        elif _dvizeniie_miska:
            self._dvizenie_iz_sebe_si(plus_kolko_pyti_da_se_vyrti, otrezi_pri_vurtene, dolu, djasno, gore, ljavo)

    def _dvizenie_iz_sebe_si(self, vyrtene, otr, dolu, djasno, gore, ljavo):
        klavisNatisnat = key.get_pressed()

        startScrollPosX = EKRAN.get_width() / 2
        mx, my = mouse.get_pos()
        if (klavisNatisnat[K_a] and self.hitbox.x > 0 + ljavo) or (
                self.hitbox.x > 0 + ljavo and mouse.get_pressed(3)[2] and self.hitbox.centerx > mx):
            if self.hitbox.x < startScrollPosX and self.playerPosX + otr[0] > 0:
                self.playerPosX -= self.vel
                dvizenie[0] += self.vel
                if (klavisNatisnat[K_w] and self.hitbox.y > -100 + gore) or (
                        _dvizeniie_miska and self.hitbox.y > -100 + gore and mouse.get_pressed(3)[2] and self.hitbox.bottom > my):
                    self.hitbox.y -= self.vel
                if (klavisNatisnat[K_s] and self.hitbox.y + dolu < EKRAN.get_height()) or (
                        _dvizeniie_miska and self.hitbox.y + dolu < EKRAN.get_height() and mouse.get_pressed(3)[2] and self.hitbox.bottom < my):
                    self.hitbox.y += self.vel
                return
            self.hitbox.x -= self.vel
        if (klavisNatisnat[K_d] and self.hitbox.x + djasno < EKRAN.get_width()) or (
                self.hitbox.x + djasno < EKRAN.get_width() and mouse.get_pressed(3)[2] and self.hitbox.centerx < mx):
            if self.hitbox.x > startScrollPosX and self.playerPosX + otr[1] < EKRAN.get_width() * vyrtene:
                dvizenie[0] -= self.vel
                self.playerPosX += self.vel
                if (klavisNatisnat[K_w] and self.hitbox.y > -100 + gore) or (
                        _dvizeniie_miska and self.hitbox.y > -100 + gore and mouse.get_pressed(3)[2] and self.hitbox.bottom > my):
                    self.hitbox.y -= self.vel
                if (klavisNatisnat[K_s] and self.hitbox.y + dolu < EKRAN.get_height()) or (
                        _dvizeniie_miska and self.hitbox.y + dolu < EKRAN.get_height() and mouse.get_pressed(3)[2] and self.hitbox.bottom < my):
                    self.hitbox.y += self.vel
                return
            self.hitbox.x += self.vel
        if (klavisNatisnat[K_w] and self.hitbox.y > -100 + gore) or (
                self.hitbox.y > -100 + gore and mouse.get_pressed(3)[2] and self.hitbox.bottom > my):
            self.hitbox.y -= self.vel
        if (klavisNatisnat[K_s] and self.hitbox.y + dolu < EKRAN.get_height()) or (
                self.hitbox.y + dolu < EKRAN.get_height() and mouse.get_pressed(3)[2] and self.hitbox.bottom < my):
            self.hitbox.y += self.vel

    def kovane_predmeti(self, e):
        global _selected_details_stop
        x, y = mouse.get_pos()
        bck = draw.rect(EKRAN, (255, 0, 0), (50, 55, 150, 130), 2)
        if bck.collidepoint(x, y) and mouse.get_pressed(3)[0]:
            Igrac._y_move = 0
            _cash_sak.clear()
            try:
                sakk.add(self._it2Predmetyt[0])
            except IndexError:
                pass
            try:
                sakk.add(self._it1Predmetyt[0])
            except IndexError:
                pass
            self._it1Predmetyt.clear()
            self._it2Predmetyt.clear()
            for k, v in MAP.items():
                MAP[k] = False
            MAP['Camp'] = True
            nastojastaZona.clear()
            nastojastaZona.append('Camp')

        EKRAN.blit(self.kovacev, self.kovacevHittbox)

        it1 = draw.rect(EKRAN, (255, 0, 0), (540, 95, 100, 100), 2)
        it2 = draw.rect(EKRAN, (255, 0, 0), (760, 95, 100, 100), 2)
        plus = draw.rect(EKRAN, (0, 255, 0), (670, 45, 50, 50))
        clin = draw.rect(EKRAN, (100, 100, 100), (670, 230, 50, 50))

        if e.type == MOUSEBUTTONUP and e.button == 1:
            if clin.collidepoint(x, y):
                self.kovaneTipBronja.clear()
                _cash_sak.clear()
                Igrac.kovaneMarkiranTip = [(0, 0, 0), (0, 0, 0), False]
                try:
                    sakk.add(self._it2Predmetyt[0])
                except IndexError:
                    pass
                try:
                    sakk.add(self._it1Predmetyt[0])
                except IndexError:
                    pass
                self._it1Predmetyt.clear()
                self._it2Predmetyt.clear()
            elif it1.collidepoint(x, y):
                self.kovaneTipBronja.clear()
                Igrac.kovaneMarkiranTip = [(0, 0, 0), (0, 0, 0), False]
                if self._it1Predmetyt:
                    _cash_sak.clear()
                    print('full', self._it1Predmetyt)
                    sakk.add(self._it1Predmetyt[0])
                    self._it1Predmetyt.clear()
                else:
                    print('empti 1')
                    self._it1Predmetyt = _cash_sak.copy()
                    del self._it1Predmetyt[1:]
                    try:
                        sakk.remove(self._it1Predmetyt[0])
                    except IndexError:
                        pass
                    _cash_sak.clear()
            elif it2.collidepoint(x, y):
                self.kovaneTipBronja.clear()
                Igrac.kovaneMarkiranTip = [(0, 0, 0), (0, 0, 0), False]
                if self._it2Predmetyt:
                    _cash_sak.clear()
                    print('full', self._it2Predmetyt)
                    sakk.add(self._it2Predmetyt[0])
                    self._it2Predmetyt.clear()
                else:
                    print('empti 2')
                    self._it2Predmetyt = _cash_sak.copy()
                    del self._it2Predmetyt[1:]
                    try:
                        sakk.remove(self._it2Predmetyt[0])
                    except IndexError as eror:
                        print(eror)
                        pass
                    _cash_sak.clear()
            elif plus.collidepoint(x, y) and self._it2Predmetyt and self._it1Predmetyt and self.kovaneTipBronja:  # [...] and [...] and set(...)
                self._kovane_zapocvane(self._it1Predmetyt[0], self._it2Predmetyt[0], self.kovaneTipBronja)
                self._it1Predmetyt.clear()
                self._it2Predmetyt.clear()
                self.kovaneTipBronja.clear()
                Igrac.kovaneMarkiranTip = [(0, 0, 0), (0, 0, 0), False]
                return
            elif plus.collidepoint(x, y) and not self.kovaneTipBronja:
                print('SELECT ITEM TYPE !!!!')
                return
            elif plus.collidepoint(x, y):
                print('PUT ITEMS IN THE SLOTS 11!')
                return

        if self._it1Predmetyt:
            EKRAN.blit(self._it1Predmetyt[0].ikonka, it1)
        if self._it2Predmetyt:
            EKRAN.blit(self._it2Predmetyt[0].ikonka, it2)
        if self._it1Predmetyt and self._it2Predmetyt:
            brrer1 = Rect((660, 100), (66, 20))
            brrer2 = Rect((660, 100 + 20), (66, 20))
            tesktTip1 = self._it1Predmetyt[0].tip
            tesktTip2 = self._it2Predmetyt[0].tip
            if not self.kovaneTipBronja or self.kovaneMarkiranTip[2]:
                self.kovaneMarkiranTip[2] = False
                draw.rect(self.kovacev, self.kovaneMarkiranTip[0], brrer1)
                txt1 = FONT15.render(f' {tesktTip1} ', False, (255, 255, 255), self.kovaneMarkiranTip[0]).convert_alpha()
                self.kovacev.blit(txt1, brrer1)

                draw.rect(self.kovacev, self.kovaneMarkiranTip[1], brrer2)
                txt2 = FONT15.render(f' {tesktTip2} ', False, (255, 255, 255), self.kovaneMarkiranTip[1]).convert_alpha()
                self.kovacev.blit(txt2, brrer2)

            if brrer1.collidepoint(x, y) and mouse.get_pressed(3)[0]:
                print('hit')
                draw.rect(EKRAN, (255, 0, 0), brrer1, 2)
                Igrac.kovaneMarkiranTip = [(100, 100, 100), (0, 0, 0), True]
                self.kovaneTipBronja.clear()
                self.kovaneTipBronja.add(tesktTip1)
            elif brrer2.collidepoint(x, y) and mouse.get_pressed(3)[0]:
                print('hit2')
                draw.rect(EKRAN, (255, 0, 0), brrer2, 2)
                Igrac.kovaneMarkiranTip = [(0, 0, 0), (100, 100, 100), True]
                self.kovaneTipBronja.clear()
                self.kovaneTipBronja.add(tesktTip2)
        else:
            draw.rect(EKRAN, (0, 0, 0), ((660, 100), (66, 20 + 20)))

        num_y = 0
        num_x = 0
        igranici = draw.rect(self.kovacev, (100, 200, 70), (355, 300, 680, 450))
        for n, i in sakk:

            xrer = Rect(355 + num_x, 300 + num_y + self._y_move, 50, 50)
            if igranici.top < xrer.bottom and igranici.bottom > xrer.top:
                draw.rect(self.kovacev, (255, 0, 0), xrer, 2)
                self.kovacev.blit(i.ikonka, xrer)

            if xrer.collidepoint(x, y):
                if mouse.get_pressed(3)[0]:
                    _cash_sak.clear()
                    _selected_details_stop = 1
                    _cash_sak.append(i)

            if i.quantity >= 2:
                infurma2 = FONT15.render(f' {i.quantity}', False, Color("white"), (0, 0, 0))
                kvinfurma2 = infurma2.get_rect()
                kvinfurma2.bottomright = xrer.bottomright
                self.kovacev.blit(infurma2, kvinfurma2)

            num_x += 60
            if num_x >= 60 * 11:
                num_x = 0
                num_y += 60

        if _cash_sak:
            EKRAN.blit(_cash_sak[0].ikonka, (x, y))

        if mouse.get_pressed(3)[2]:
            _cash_sak.clear()

        if e.type == MOUSEBUTTONDOWN:
            if e.button == 4:
                Igrac._y_move += 60
            elif e.button == 5:
                Igrac._y_move -= 60

        if _selected_details_stop:
            r = draw.rect(self.kovacev, (221, 226, 240), (10, 315, 335, 390))

            d = {'Name:': f'{_cash_sak[0].raw_name}', 'Type:': f'{_cash_sak[0].tip}', 'Atk:': f"{_cash_sak[0].attack}",
                 'Def:': f'{_cash_sak[0].defence}', '+HP:': f'{_cash_sak[0].HP}', 'Use CD:': f'{_cash_sak[0].cooldown}',
                 'DMG:': f'{_cash_sak[0].damage}',
                 'AtkPower': f'{_cash_sak[0].attackPower}', 'HitChance': f'{_cash_sak[0].hitChance}',
                 'CritMultiplier': f'{_cash_sak[0].critMultiplier}',
                 'CritChance': f'{_cash_sak[0].crit}', 'Special: ': f'{_cash_sak[0].note}', 'Dodge': f'{_cash_sak[0].dodge}',
                 chr(int('0x2C0F', 16)) + ':': f'{_cash_sak[0].value}'}
            m = 0
            for k, v in d.items():
                ime = FONT22.render(k, False, Color("black"))
                imekor = [r.x, r.y + m]
                stoinost = FONT22.render(v[0:24], False, (2, 71, 2))
                kvstoinost = stoinost.get_rect()
                kvstoinost.right = r.right - 5
                kvstoinost.y = r.y + m

                if v != '0':
                    if k == chr(int('0x2C0F', 16)) + ':':
                        kvstoinost.bottom = r.bottom
                        imekor[0] = kvstoinost.left - 35
                        imekor[1] = r.bottom - 32

                    if k == 'Special: ':
                        kvstoinost.x = r.x + 80

                    self.kovacev.blit(ime, imekor)
                    self.kovacev.blit(stoinost, kvstoinost)
                    m += 25
                    if len(v) > 24:
                        kvstoinost.y += 25
                        kvstoinost.x = imekor[0]
                        self.kovacev.blit(FONT22.render(v[24:], False, (2, 71, 2)), kvstoinost)
                        m += 25

            _selected_details_stop = 0

    @staticmethod
    def _kovane_zapocvane(item1, item2, tip: set[str]):
        print(item1.raw_name.count('+'), item2.raw_name.count('+'))
        if item1.raw_name.count('+') == item2.raw_name.count('+'):
            if item1.raw_name.count('+') < 2 or item2.raw_name.count('+') < 2:
                print('combining', item1, item2)
                sakk.add(item1.pluss(item2, tip.pop().strip()))
                return
            else:
                sakk.add(item1)
                sakk.add(item2)
                print('Item to high of a level')
        else:
            sakk.add(item1)
            sakk.add(item2)
            print(f"'{item1.raw_name}' is not the same power lvl  as '{item2.raw_name}'")


class Obekt(Sprite, CD):
    __slots__ = (
        'covece', 'dylzina', 'visocina', 'hitbox', 'korX', 'korY', 'promjanaY', 'promjanaX', 'ime', 'ikonka', 'ljavaAtakaCD', 'djasnaAtakaCD',
        'ljavaAtaka', 'djasnaAtaka', 'GCD', 'GCDmax', 'ljavaAtakaMAX', 'djasnaAtakaMAX', 'raznoCD', 'raznoCDMAX', 'zastita', 'HP', 'HPnstojast',
        'attackPower', 'hitChance', 'crit', 'critMultiplier', 'dodge', 'kljuc', 'specialno', 'boj')

    def __init__(self, figura, kor_x, kor_y):
        Sprite.__init__(self, figura, kor_x, kor_y)
        CD.__init__(self)

        self.kljuc = False
        self.specialno = 0
        self.boj = False
        self.msgbox = Surface((200, 100)).convert()
        self.msgbox.fill((144, 100, 144))
        self.msgbox.blit(newRender(f'F to fight {self.ime}', FONT15, Color('white'), (0, 0, 0)), (0, 0))

    def vrazduvane(self, subekt, vid_vrag='0'):
        if self.hitbox.colliderect(subekt.hitbox):
            EKRAN.blit(self.msgbox, (x if (x := self.hitbox.x - 80) >= 0 else 0, y if (y := self.hitbox.y - 200 + 50) >= 0 else 0))
            if key.get_pressed()[K_f]:
                self.boj = True
                innertime = time.Clock()
                while self.boj:
                    ee = event.poll()
                    if ee.type == QUIT:
                        break
                    CD_dt = innertime.tick(FPS) / 1000
                    Combat.narisuvaj_pojnoto_pole(self, subekt)
                    if vid_vrag[0] == '0':
                        Combat.normalen_mob(ee, CD_dt, self, subekt)
                    elif vid_vrag[0] == '1':
                        Combat.elit_mob(ee, CD_dt, self, subekt)
                    elif vid_vrag[0] == '2':
                        Combat.oficer_mob(ee, CD_dt, self, subekt, vid_vrag[1])
                    elif vid_vrag[0] == 'B':
                        Combat.bos_mob(ee, CD_dt, self, subekt)
                    display.flip()


class ObektDrug(Sprite):
    kljuc1 = False
    magazin = False
    _y_move = 0
    _y_move_obekt = 0
    _y_move_lj = 0
    _y_move_dj = 0
    barterdj = {}
    barterlj = {}
    barterljStojnost = 0
    barterdjStojnost = 0
    barterPopinfo = set()
    # popdrop = 0
    obnoviSakk = True
    obnoviMagazin = True

    govorizbori: list[Rect] = []
    govorIzboriMiska = [0, 0, 0]
    goMiska = False
    goKlavietura = False
    msgCjat = (221, 96, 230)
    convboxY = 200
    convbox = Surface((EKRAN.get_width(), convboxY))
    convbox.fill(msgCjat)

    def __init__(self, figura, kor_x, kor_y, dialog=None, ime='???'):
        Sprite.__init__(self, figura, kor_x, kor_y, ime=ime)

        if dialog is not None:
            with open(dialog, 'r') as f:
                self.TEXST = load(f)

        self.msgbox = Surface((400, 100), SRCALPHA).convert_alpha()
        self.msgbox.fill((0, 0, 0, 0))
        self.msgbox.blit(newRender(f'E to speak with {self.ime}', FONT25, Color('white'), (0, 0, 0)), (0, 0))

        # self.kljuc = False
        self.sak = {}
        self.neiskam = tuple()
        self.pryrvonacalenTekst = True

        self.magazinFon = image.load('data/magazin.png').convert_alpha()

        self.govor = False
        self.node = '0'

    def vid1_nov(self, e):
        if e.type == MOUSEBUTTONUP:
            ((izbor1, izbor2, izbor3),) = self.TEXST[self.node].values()
            ObektDrug.goMiska = True
            mx, my = mouse.get_pos()
            ObektDrug.govorIzboriMiska = [0, 0, 0]
            if self.govorizbori[0].collidepoint((mx, my)) and izbor1:
                self.govorIzboriMiska[0] = 1
            elif self.govorizbori[1].collidepoint((mx, my)) and izbor2:
                self.govorIzboriMiska[1] = 1
            elif self.govorizbori[2].collidepoint((mx, my)) and izbor3:
                self.govorIzboriMiska[2] = 1
        elif e.type == KEYUP and e.key != K_e:
            ObektDrug.goKlavietura = True
            ((izbor1, izbor2, izbor3),) = self.TEXST[self.node].values()
            ObektDrug.govorIzboriMiska = [0, 0, 0]
            if izbor1 and (e.key == K_1):
                self.govorIzboriMiska[0] = 1
            elif izbor2 and (e.key == K_1 or e.key == K_2):
                self.govorIzboriMiska[1] = 1
            elif izbor3 and (e.key == K_1 or e.key == K_2 or e.key == K_3):
                self.govorIzboriMiska[2] = 1

        if self.goKlavietura or self.goMiska:
            ObektDrug.goMiska = False
            ObektDrug.goKlavietura = False
            print(self.govorIzboriMiska)
            ((izbor1, izbor2, izbor3),) = self.TEXST[self.node].values()
            mis1, mis2, mis3 = self.govorIzboriMiska
            if (izbor1 and mis1) or (izbor2 and (mis1 or mis2)) or (izbor3 and (mis1 or mis2 or mis3)):
                if mis1:
                    sledvast = 0
                elif mis2:
                    sledvast = 1
                elif mis3:
                    sledvast = 2

                if int(sledvastIzbor := self.TEXST[f'options{self.node}'].split('|')[sledvast]) < 0:
                    self.govor = False
                    self.node = '0'
                    self.pryrvonacalenTekst = True
                    return
                elif sledvastIzbor == '100':  # 100 -> aktivirane na magazin
                    ObektDrug.magazin = True
                    self.node = '0'
                    self.pryrvonacalenTekst = True
                    return
                self.node = sledvastIzbor

                ((k, v),) = self.TEXST[self.node].items()

                self.convbox.fill(self.msgCjat)
                self.convbox.blit(newRender(f'{k}', FONT15, Color('white'), (0, 0, 0)), (0, 0))

                izvorY = 80
                self.govorizbori.clear()
                for izbor in v:
                    kv = newRender(izbor, FONT15, Color('white'), (0, 0, 0))
                    kvw = kv.get_rect()
                    kvw.y = EKRAN.get_height() - self.convboxY + izvorY
                    self.govorizbori.append(kvw)
                    self.convbox.blit(kv, (0, izvorY))
                    izvorY += 25
        elif self.pryrvonacalenTekst:
            self.pryrvonacalenTekst = False
            ((k, v),) = self.TEXST[self.node].items()

            self.convbox.fill(self.msgCjat)
            self.convbox.blit(newRender(f'{k}', FONT15, Color('white'), (0, 0, 0)), (0, 0))

            izvorY = 80
            self.govorizbori.clear()
            for izbor in v:
                kv = newRender(izbor, FONT15, Color('white'), (0, 0, 0))
                kvw = kv.get_rect()
                kvw.y = EKRAN.get_height() - self.convboxY + izvorY
                self.govorizbori.append(kvw)
                self.convbox.blit(kv, (0, izvorY))
                izvorY += 25

    def _magazinyt_barter(self, e):
        global _selected_details_stop, _dvizeniie_miska
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                ObektDrug.magazin = False
                _dvizeniie_miska = True
                self.govor = False
        sx, sy = 10, 35
        ox, oy = 725, 35
        mx, my = mouse.get_pos()
        lx, ly = 370, 460
        dx, dy = 542, 460

        EKRAN.blit(self.magazinFon, (0, 0))
        subektBagaz = Rect((sx, sy), (345, 650))
        obektBagaz = Rect((ox, oy), (345, 650))
        bartaerLjavo = Rect(lx, ly, 160, 215)
        barterrDjasno = Rect(dx, dy, 160, 215)
        draw.rect(self.magazinFon, (30, 30, 30), bartaerLjavo)
        draw.rect(self.magazinFon, (30, 30, 30), barterrDjasno)

        pocistiLj = Rect((lx, ly - 45), (70, 30))
        pocistiDj = Rect((dx + 160 - 70, dy - 45), (70, 30))
        kupi = Rect((dx - 35, dy - 45), (70, 30))
        if e.type == MOUSEBUTTONUP:
            if pocistiLj.collidepoint(mx, my) and e.button == 1:
                for vv in self.barterlj.values():
                    if vv.quantity > 1 and sakk.inside.get(vv.raw_name, False):
                        sakk.inside[vv.raw_name].quantity += vv.quantity
                    else:
                        sakk.add(vv)
                self.barterlj.clear()
                self.barterPopinfo.clear()
                _cash_sak.clear()
                ObektDrug.obnoviSakk = True
            elif pocistiDj.collidepoint(mx, my) and e.button == 1:
                for vv in self.barterdj.values():
                    if self.sak.get(vv.raw_name, False) and self.sak[vv.raw_name].quantity >= 1:
                        self.sak[vv.raw_name].quantity += vv.quantity
                    else:
                        self.sak[vv.raw_name] = vv
                self.barterdj.clear()
                self.barterPopinfo.clear()
                _cash_sak.clear()
                ObektDrug.obnoviMagazin = True
            elif kupi.collidepoint(mx, my) and e.button == 1:
                if self.barterljStojnost >= self.barterdjStojnost:
                    for itt in self.barterdj.values():
                        sakk.add(itt)
                        itt.value = int(itt.value * 0.5)
                    for itt in self.barterlj.values():
                        self.sak[itt.raw_name] = itt
                        itt.value = int(itt.value * 1.8)
                    self.barterlj.clear()
                    self.barterdj.clear()
                else:
                    print('ne gi dava za tazi suma ')

                obstaStojnost = 0
                for itt in self.barterlj.values():
                    itt.recalc()
                    obstaStojnost += itt.netValue
                ObektDrug.barterljStojnost = obstaStojnost
                ob = FONT25.render(chr(int('0x2C0F', 16)) + f' {self.barterljStojnost}     ', False, (0, 0, 0), (100, 100, 100))
                self.magazinFon.blit(ob, bartaerLjavo.bottomleft)

                obstaStojnost = 0
                for itt in self.barterdj.values():
                    itt.recalc()
                    obstaStojnost += itt.netValue
                ObektDrug.barterdjStojnost = obstaStojnost
                ob = FONT25.render(chr(int('0x2C0F', 16)) + f' {self.barterdjStojnost}    ', False, (0, 0, 0), (100, 100, 100))
                self.magazinFon.blit(ob, barterrDjasno.bottomleft)

                ObektDrug.obnoviSakk = True
                ObektDrug.obnoviMagazin = True

        draw.rect(self.magazinFon, (237, 215, 50), pocistiLj)
        draw.rect(self.magazinFon, (237, 215, 50), pocistiDj)
        draw.rect(self.magazinFon, (22, 168, 127), kupi, 5)

        num_y = 0
        num_x = 0
        kraenpredmetpodS = {0}
        for ime, predmet in sakk:
            xrer = Rect((num_x + sx, num_y + self._y_move + sy), (50, 50))
            kraenpredmetpodS.add(xrer.bottom)

            if xrer.collidepoint(mx, my) and mouse.get_pressed(3)[0]:
                self.barterPopinfo.clear()
                _cash_sak.clear()
                _selected_details_stop = 1
                _cash_sak.append(predmet)

            if subektBagaz.top < xrer.bottom and subektBagaz.bottom > xrer.top:
                if subektBagaz.collidepoint(mx, my) or self.obnoviSakk:
                    txt = f'               {predmet.raw_name} '
                    ltxt = txt[:45]
                    dtxt = txt[45:]

                    imeNaPredmet = FONT15.render(ltxt, False, (0, 0, 0), (255, 255, 255))
                    cenaNapredmet = FONT25.render(chr(int('0x2C0F', 16)) + f' {predmet.value:02d}', False, (0, 0, 0), (255, 255, 255))
                    kvcenaNapredmet = cenaNapredmet.get_rect()
                    kvcenaNapredmet.right = subektBagaz.right
                    kvcenaNapredmet.y = xrer.y

                    if len(txt) > 45:
                        imeNaPredmetOstatyk = FONT15.render('                ' + dtxt, False, (0, 0, 0), (255, 255, 255))
                        self.magazinFon.blit(imeNaPredmetOstatyk, (xrer.x, xrer.y + 20))

                    imeNaPredmetKv = imeNaPredmet.get_rect()
                    draw.rect(self.magazinFon, (255, 255, 255), ((imeNaPredmetKv.right, xrer.y), (abs(imeNaPredmetKv.right - kvcenaNapredmet.x), 20)))
                    self.magazinFon.blit(imeNaPredmet, xrer)
                    self.magazinFon.blit(cenaNapredmet, kvcenaNapredmet)

                draw.rect(EKRAN, (0, 0, 0), xrer, 4)
                EKRAN.blit(predmet.ikonka, xrer)

                if predmet.quantity >= 2:
                    infurma2 = FONT15.render(f' {predmet.quantity}', False, Color("white"), (0, 0, 0))
                    kvinfurma2 = infurma2.get_rect()
                    kvinfurma2.bottomright = xrer.bottomright
                    EKRAN.blit(infurma2, kvinfurma2)

            num_x += 60
            if num_x >= 60 * 1:
                num_x = 0
                num_y += 60
        ObektDrug.obnoviSakk = False

        num_y = 0
        num_x = 0
        kraenpredmetpodO = {0}
        for ime, predmet in self.sak.items():
            orer = Rect((num_x + ox, num_y + self._y_move_obekt + oy), (50, 50))
            kraenpredmetpodO.add(orer.bottom)
            if orer.collidepoint(mx, my) and mouse.get_pressed(3)[0]:
                self.barterPopinfo.clear()
                _cash_sak.clear()
                _selected_details_stop = 1
                _cash_sak.append(predmet)

            if obektBagaz.top < orer.bottom and obektBagaz.bottom > orer.top:
                if obektBagaz.collidepoint(mx, my) or self.obnoviMagazin:
                    txt = f'               {predmet.raw_name} '
                    ltxt = txt[:45]
                    dtxt = txt[45:]

                    imeNaPredmet = FONT15.render(ltxt, False, (0, 0, 0), (255, 255, 255))
                    cenaNapredmet = FONT25.render(chr(int('0x2C0F', 16)) + f' {predmet.value:02d}', False, (0, 0, 0), (255, 255, 255))
                    kvcenaNapredmet = cenaNapredmet.get_rect()
                    kvcenaNapredmet.right = obektBagaz.right
                    kvcenaNapredmet.y = orer.y

                    if len(txt) > 45:
                        imeNaPredmetOstatyk = FONT15.render('                ' + dtxt, False, (0, 0, 0), (255, 255, 255))
                        self.magazinFon.blit(imeNaPredmetOstatyk, (orer.x, orer.y + 20))

                    imeNaPredmetKv = imeNaPredmet.get_rect()
                    draw.rect(self.magazinFon, (255, 255, 255),
                              ((imeNaPredmetKv.right + obektBagaz.x, orer.y), (abs(imeNaPredmetKv.right - kvcenaNapredmet.x) - obektBagaz.x, 20)))
                    self.magazinFon.blit(imeNaPredmet, orer)
                    self.magazinFon.blit(cenaNapredmet, kvcenaNapredmet)

                draw.rect(EKRAN, (0, 0, 0), orer, 4)
                EKRAN.blit(predmet.ikonka, orer)

                if predmet.quantity >= 2:
                    infurma2 = FONT15.render(f' {predmet.quantity}', False, Color("white"), (0, 0, 0))
                    kvinfurma2 = infurma2.get_rect()
                    kvinfurma2.bottomright = orer.bottomright
                    EKRAN.blit(infurma2, kvinfurma2)

            num_x += 60
            if num_x >= 60 * 1:
                num_x = 0
                num_y += 60
        ObektDrug.obnoviMagazin = False

        num_y = 0
        num_x = 0
        kraenpredmetpodlj = {0}
        for predmet in self.barterlj.values():
            ljrer = Rect((num_x + lx, num_y + self._y_move_lj + ly), (50, 50))
            kraenpredmetpodlj.add(ljrer.bottom)

            if ljrer.collidepoint(mx, my) and mouse.get_pressed(3)[0] and not _cash_sak:
                self.barterPopinfo.clear()
                self.barterPopinfo.add(ljrer.midbottom)
                self.barterPopinfo.add(predmet)

            if bartaerLjavo.top < ljrer.bottom and bartaerLjavo.bottom > ljrer.top:
                draw.rect(EKRAN, (0, 0, 0), ljrer, 4)

                EKRAN.blit(predmet.ikonka, ljrer)
                if predmet.quantity >= 2:
                    infurma2 = FONT15.render(f' {predmet.quantity}', False, Color("white"), (0, 0, 0))
                    kvinfurma2 = infurma2.get_rect()
                    kvinfurma2.bottomright = ljrer.bottomright
                    EKRAN.blit(infurma2, kvinfurma2)

            num_x += 55
            if num_x >= 55 * 3:
                num_x = 0
                num_y += 55
                if self.barterPopinfo:
                    try:
                        srx, sry = list(self.barterPopinfo)[0]
                    except TypeError:
                        srx, sry = list(self.barterPopinfo)[1]
                    if ljrer.y <= sry <= ljrer.bottom:
                        num_y += 50

        num_y = 0
        num_x = 0
        kraenpredmetpoddj = {0}
        for predmet in self.barterdj.values():
            djrer = Rect((num_x + dx, num_y + self._y_move_dj + dy), (50, 50))
            kraenpredmetpoddj.add(djrer.bottom)

            if djrer.collidepoint(mx, my) and mouse.get_pressed(3)[0] and not _cash_sak:
                self.barterPopinfo.clear()
                self.barterPopinfo.add(djrer.midbottom)
                self.barterPopinfo.add(predmet)

            if barterrDjasno.top < djrer.bottom and barterrDjasno.bottom > djrer.top:
                draw.rect(EKRAN, (0, 0, 0), djrer, 4)

                EKRAN.blit(predmet.ikonka, djrer)
                if predmet.quantity >= 2:
                    infurma2 = FONT15.render(f' {predmet.quantity}', False, Color("white"), (0, 0, 0))
                    kvinfurma2 = infurma2.get_rect()
                    kvinfurma2.bottomright = djrer.bottomright
                    EKRAN.blit(infurma2, kvinfurma2)

            num_x += 55
            if num_x >= 55 * 3:
                num_x = 0
                num_y += 55
                if self.barterPopinfo:
                    try:
                        _, sry = list(self.barterPopinfo)[0]
                    except TypeError:
                        _, sry = list(self.barterPopinfo)[1]
                    if djrer.y <= sry <= djrer.bottom:
                        num_y += 50

        if e.type == MOUSEBUTTONDOWN and subektBagaz.collidepoint(mx, my):
            if e.button == 4 and min(kraenpredmetpodS) - 50 < subektBagaz.top:
                ObektDrug._y_move += 60
            elif e.button == 5 and max(kraenpredmetpodS) > subektBagaz.bottom:
                ObektDrug._y_move -= 60
        elif e.type == MOUSEBUTTONDOWN and obektBagaz.collidepoint(mx, my):
            if e.button == 4 and min(kraenpredmetpodO) - 50 < obektBagaz.top:
                ObektDrug._y_move_obekt += 60
            elif e.button == 5 and max(kraenpredmetpodO) > obektBagaz.bottom:
                ObektDrug._y_move_obekt -= 60
        elif e.type == MOUSEBUTTONDOWN and bartaerLjavo.collidepoint(mx, my):
            if e.button == 4 and min(kraenpredmetpodlj, default=520) - 50 < bartaerLjavo.top:
                ObektDrug._y_move_lj += 60
                self.barterPopinfo.clear()
            elif e.button == 5 and max(kraenpredmetpodlj, default=625) > bartaerLjavo.bottom:
                ObektDrug._y_move_lj -= 60
                self.barterPopinfo.clear()
        elif e.type == MOUSEBUTTONDOWN and barterrDjasno.collidepoint(mx, my):
            if e.button == 4 and min(kraenpredmetpoddj, default=520) - 50 < barterrDjasno.top:
                ObektDrug._y_move_dj += 60
                self.barterPopinfo.clear()
            elif e.button == 5 and max(kraenpredmetpoddj, default=625) > barterrDjasno.bottom:
                ObektDrug._y_move_dj -= 60
                self.barterPopinfo.clear()

        if _selected_details_stop:
            r = Rect((370, 30), (335, 390))
            draw.rect(self.magazinFon, (221, 226, 240), r)

            d = {'Name:': f'{_cash_sak[0].raw_name}', 'Type:': f'{_cash_sak[0].tip}', 'Atk:': f"{_cash_sak[0].attack}",
                 'Def:': f'{_cash_sak[0].defence}', '+HP:': f'{_cash_sak[0].HP}', 'Use CD:': f'{_cash_sak[0].cooldown}',
                 'DMG:': f'{_cash_sak[0].damage}',
                 'AtkPower': f'{_cash_sak[0].attackPower}', 'HitChance': f'{_cash_sak[0].hitChance}',
                 'CritMultiplier': f'{_cash_sak[0].critMultiplier}',
                 'CritChance': f'{_cash_sak[0].crit}', 'Special: ': f'{_cash_sak[0].note}', 'Dodge': f'{_cash_sak[0].dodge}',
                 chr(int('0x2C0F', 16)) + ':': f'{_cash_sak[0].value}'}
            m = 0
            for k, v in d.items():
                ime = FONT22.render(k, False, Color("black"))
                imekor = [r.x, r.y + m]
                stoinost = FONT22.render(v[0:24], False, (2, 71, 2))
                kvstoinost = stoinost.get_rect()
                kvstoinost.right = r.right - 5
                kvstoinost.y = r.y + m

                if v != '0':
                    if k == chr(int('0x2C0F', 16)) + ':':
                        kvstoinost.bottom = r.bottom
                        imekor[0] = kvstoinost.left - 35
                        imekor[1] = r.bottom - 32

                    if k == 'Special: ':
                        kvstoinost.x = r.x + 80

                    self.magazinFon.blit(ime, imekor)
                    self.magazinFon.blit(stoinost, kvstoinost)
                    m += 25
                    if len(v) > 24:
                        kvstoinost.y += 25
                        kvstoinost.x = imekor[0]
                        self.magazinFon.blit(FONT22.render(v[24:], False, (2, 71, 2)), kvstoinost)
                        m += 25

            _selected_details_stop = 0
            if self.barterPopinfo:
                _cash_sak.clear()

        if _cash_sak:
            EKRAN.blit(_cash_sak[0].ikonka, (mx, my))
        if mouse.get_pressed(3)[2]:
            _cash_sak.clear()
            self.barterPopinfo.clear()

        if e.type == MOUSEBUTTONUP:
            if bartaerLjavo.collidepoint(mx, my) and e.button == 1 and _cash_sak and not self.barterPopinfo:
                if _cash_sak[0].raw_name in self.neiskam:
                    print('no no no')
                    _cash_sak.clear()
                    return
                elif _cash_sak[0].raw_name in list(self.barterlj.keys()):
                    self.barterlj[_cash_sak[0].raw_name].quantity += 1
                elif _cash_sak[0].quantity > 1:
                    self.barterlj[_cash_sak[0].raw_name] = _cash_sak[0].kopiraj()
                else:
                    self.barterlj[_cash_sak[0].raw_name] = _cash_sak[0]
                sakk.remove(_cash_sak[0])
                _cash_sak.clear()
                ObektDrug.obnoviSakk = True

                obstaStojnost = 0
                for itt in self.barterlj.values():
                    itt.recalc()
                    obstaStojnost += itt.netValue
                ObektDrug.barterljStojnost = obstaStojnost
                ob = FONT25.render(chr(int('0x2C0F', 16)) + f' {self.barterljStojnost}    ', False, (0, 0, 0), (100, 100, 100))
                self.magazinFon.blit(ob, bartaerLjavo.bottomleft)
            elif barterrDjasno.collidepoint(mx, my) and e.button == 1 and _cash_sak and not self.barterPopinfo:
                if _cash_sak[0].raw_name in [x.lower() for x in sakk.inside.keys()]:
                    print('oh no oh no')
                    _cash_sak.clear()
                    return
                elif _cash_sak[0].raw_name in list(self.barterdj.keys()):
                    self.barterdj[_cash_sak[0].raw_name].quantity += 1
                elif _cash_sak[0].quantity > 1:
                    self.barterdj[_cash_sak[0].raw_name] = _cash_sak[0].kopiraj()
                else:
                    self.barterdj[_cash_sak[0].raw_name] = _cash_sak[0]
                if self.sak[_cash_sak[0].raw_name].quantity > 1:
                    self.sak[_cash_sak[0].raw_name].quantity -= 1
                else:
                    del self.sak[_cash_sak[0].raw_name]
                _cash_sak.clear()
                ObektDrug.obnoviMagazin = True

                obstaStojnost = 0
                for itt in self.barterdj.values():
                    itt.recalc()
                    obstaStojnost += itt.netValue
                ObektDrug.barterdjStojnost = obstaStojnost
                ob = FONT25.render(chr(int('0x2C0F', 16)) + f' {self.barterdjStojnost}    ', False, (0, 0, 0), (100, 100, 100))
                self.magazinFon.blit(ob, barterrDjasno.bottomleft)

        if self.barterPopinfo and not _cash_sak:
            try:
                srx, sry = list(self.barterPopinfo)[0]
                predmetyty = list(self.barterPopinfo)[1]
            except TypeError:
                srx, sry = list(self.barterPopinfo)[1]
                predmetyty = list(self.barterPopinfo)[0]

            sinjo = Rect((srx - 100, sry), (100, 50))
            cerveno = Rect((srx, sry), (100, 50))
            draw.rect(EKRAN, (255, 0, 0), cerveno)
            draw.rect(EKRAN, (0, 0, 255), sinjo)
            if sinjo.collidepoint(mx, my) and mouse.get_pressed(3)[0]:

                _cash_sak.clear()
                _selected_details_stop = 1
                _cash_sak.append(predmetyty)
            elif cerveno.collidepoint(mx, my) and mouse.get_pressed(3)[0]:
                if srx <= 505:
                    if predmetyty.raw_name in self.barterlj and predmetyty.quantity > 1:
                        sakk.add(predmetyty.kopiraj())
                        predmetyty.quantity -= 1
                    else:
                        sakk.add(self.barterlj.pop(predmetyty.raw_name))
                    self.barterPopinfo.clear()
                    obstaStojnost = 0
                    for itt in self.barterlj.values():
                        itt.recalc()
                        obstaStojnost += itt.netValue
                    ObektDrug.barterljStojnost = obstaStojnost
                    ob = FONT25.render(chr(int('0x2C0F', 16)) + f' {self.barterljStojnost}     ', False, (0, 0, 0), (100, 100, 100))
                    self.magazinFon.blit(ob, bartaerLjavo.bottomleft)
                    ObektDrug.obnoviSakk = True
                else:
                    if predmetyty.raw_name in self.barterdj and predmetyty.quantity > 1:
                        predmetyty.quantity -= 1
                    else:
                        del self.barterdj[predmetyty.raw_name]
                    self.barterPopinfo.clear()

                    if self.sak.get(predmetyty.raw_name, False) and self.sak[predmetyty.raw_name].quantity >= 1:
                        self.sak[predmetyty.raw_name].quantity += 1
                    else:
                        self.sak[predmetyty.raw_name] = predmetyty.kopiraj()

                    obstaStojnost = 0
                    for itt in self.barterdj.values():
                        itt.recalc()
                        obstaStojnost += itt.netValue
                    ObektDrug.barterdjStojnost = obstaStojnost
                    ob = FONT25.render(chr(int('0x2C0F', 16)) + f' {self.barterdjStojnost}    ', False, (0, 0, 0), (100, 100, 100))
                    self.magazinFon.blit(ob, barterrDjasno.bottomleft)
                    ObektDrug.obnoviMagazin = True

    def razgovarjane(self, subekt, e):
        global _dvizeniie_miska
        if self.hitbox.colliderect(subekt.hitbox):
            _dvizeniie_miska = True
            if not self.govor:
                EKRAN.blit(self.msgbox, ((x if (x := self.hitbox.x - 80) >= 0 else 0), (y if (y := self.hitbox.y - 50) >= 0 else 0)))
            if key.get_pressed()[K_e] or self.govor:
                EKRAN.blit(self.convbox, (0, EKRAN.get_height() - 200))
                self.govor = True
                _dvizeniie_miska = False
                if self.magazin:
                    self._magazinyt_barter(e)
                    return
                self.vid1_nov(e)
            else:
                self.govor = False
                ObektDrug._y_move = 0
                self._y_move_obekt = 0

    @classmethod
    def spusyk_pestera(cls, e_nov: bool):
        cls.kljuc1 = e_nov


class Predmet(Sprite):
    __slots__ = ('covece', 'dylzina', 'visocina', 'hitbox', 'korX', 'korY', 'promjanaY', 'promjanaX', 'ime', 'ikonka')

    def __init__(self, figura, kor_x, kor_y, hitbox_promeni_y=None, hitbox_promeni_x=None, syobstenie=''):
        Sprite.__init__(self, figura, kor_x, kor_y, hitbox_promeni_y, hitbox_promeni_x)
        self.msgbox = Surface((200, 100)).convert()
        self.msgbox.fill((144, 100, 144))
        self.msgbox.blit(newRender(syobstenie, FONT15, Color('white'), (0, 0, 0)), (0, 0))

    def block(subekt, self):
        if not self.hitbox.colliderect(subekt.hitbox):
            return
        overlap = self.hitbox.clip(subekt.hitbox)
        if overlap.width > overlap.height:
            if self.hitbox.y < subekt.hitbox.y:
                self.hitbox.bottom = subekt.hitbox.top
            else:
                self.hitbox.top = subekt.hitbox.bottom
        else:
            if self.hitbox.x < subekt.hitbox.x:
                self.hitbox.right = subekt.hitbox.left
            else:
                self.hitbox.left = subekt.hitbox.right

    def push(self, subekt):
        if not self.hitbox.colliderect(subekt.hitbox):
            return
        overlap = self.hitbox.clip(subekt.hitbox)
        if overlap.width > overlap.height:
            if self.hitbox.y < subekt.hitbox.y:
                self.hitbox.bottom = subekt.hitbox.top
            else:
                self.hitbox.top = subekt.hitbox.bottom
        else:
            if self.hitbox.x < subekt.hitbox.x:
                self.hitbox.right = subekt.hitbox.left
            else:
                self.hitbox.left = subekt.hitbox.right

    def auto_boxx(self, subekt):
        if self.hitbox.colliderect(subekt.hitbox) and self.hitbox.bottom > subekt.hitbox.bottom:
            print('hitt')

    def naris_msgbox(self):
        EKRAN.blit(self.msgbox, (x if (x := self.hitbox.x - 80) >= 0 else 0, y if (y := self.hitbox.y - 200 + 50) >= 0 else 0))


class KARTA:
    zonaPopInfo = image.load('data/zone_popup.png').convert_alpha()
    enter = Surface((200, 50)).convert()
    enter.fill((30, 30, 30))
    prodylzi = Surface((200, 50)).convert()
    prodylzi.fill((30, 30, 30))
    tekstaVlizane = True
    tekstMiska = True
    miskaInfo = Surface((10, 10)).convert()

    def __init__(self, zonata=None, kor_x=0, kor_y=0, ikonata=None, mini_ikonka=None, mini_x=0, mini_y=0):
        if zonata is not None:
            self.zona = image.load(zonata).convert()
            self.dylzina = self.zona.get_rect().width
            self.visocina = self.zona.get_rect().height
        if ikonata is not None:
            self.ikonka = image.load(ikonata).convert_alpha()
            self.hitbox = self.ikonka.get_rect()
            self.hitbox.x = kor_x
            self.hitbox.y = kor_y
        if mini_ikonka is not None:
            self.miniIkonka: Surface = image.load(mini_ikonka).convert_alpha()
            self.miniHitbox: Rect = self.miniIkonka.get_rect()
            self.miniHitbox.height, self.miniHitbox.width = self.miniIkonka.get_height() // 1, self.miniIkonka.get_width() // 1
            self.miniHitbox.x = mini_x
            self.miniHitbox.y = mini_y
        self.x_vyrtene = 0
        self.colide = True

    def risuvaj_zonata(self, vyrtene_na_fona=False):
        if not vyrtene_na_fona:
            EKRAN.blit(self.zona, (0, 0))
        else:
            self._risuvaj_zona_iz_sebe_si()

    def _risuvaj_zona_iz_sebe_si(self):
        rel_x = self.x_vyrtene % self.dylzina
        EKRAN.blit(self.zona, (rel_x - self.dylzina, 0))
        if rel_x < EKRAN.get_width():
            EKRAN.blit(self.zona, (rel_x, 0))
        self.x_vyrtene += dvizenie[0]
        dvizenie[0] = 0

    def _risuvane(self):
        EKRAN.blit(self.ikonka, self.hitbox)
        draw.rect(EKRAN, (255, 0, 0), self.hitbox, 2)

    def ikona_markitana(self, na_zona):
        x, y = mouse.get_pos()
        if self.hitbox.collidepoint(x, y):
            self._risuvane()
            if mouse.get_pressed(3)[0]:
                poslednaZona[0].clear()
                poslednaZona[1].clear()
                poslednaZona[0]['Camp'] = True
                poslednaZona[1].append((420, 400))
                for k, v in MAP.items():
                    MAP[k] = False
                MAP[na_zona] = True
                nastojastaZona.clear()
                nastojastaZona.append(na_zona)
                self.colide = False

    def mini_ikonka_markirana(self, na_zona, ekrann, subekt, kvadratce):
        ekrann.blit(self.miniIkonka, self.miniHitbox)

        mx, my = mouse.get_pos()
        cvetovePodMiskata = EKRAN.get_at((mx, my))[:3]  # r, g, b
        miskaNadCvjat = list(filter(lambda c: c > 8, cvetovePodMiskata))
        if self.miniHitbox.collidepoint(mx, my) and any(miskaNadCvjat):
            if self.tekstMiska:
                KARTA.tekstMiska = False
                txt3 = FONT15.render(f' This zone is {na_zona} ', False, (0, 0, 0), (230, 230, 230))
                self.miskaInfo = transform.scale(self.miskaInfo, txt3.get_size())
                self.miskaInfo.blit(txt3, (0, 0))
            EKRAN.blit(self.miskaInfo, (mx + 20, my))
        elif not self.tekstMiska:
            KARTA.tekstMiska = True

        if self.miniHitbox.colliderect(kvadratce) and self.colide:
            EKRAN.blit(self.zonaPopInfo, (EKRAN.get_width() / 4, EKRAN.get_height() / 4))
            self.zonaPopInfo.blit(self.enter, (50, 300))
            self.zonaPopInfo.blit(self.prodylzi, (300, 300))
            if self.tekstaVlizane:
                KARTA.tekstaVlizane = False
                txt = FONT15.render('1. Enter the zone', False, (255, 255, 255))
                self.enter.blit(txt, (10, 15))
                txt2 = FONT15.render('2. Continue ...', False, (255, 255, 255))
                self.prodylzi.blit(txt2, (10, 15))

            if key.get_pressed()[K_1]:
                subekt.hitbox.x, subekt.hitbox.y = 50, 490
                for k, v in MAP.items():
                    MAP[k] = False
                    self.colide = False
                MAP[na_zona] = True
                nastojastaZona.clear()
                nastojastaZona.append(na_zona)
            elif key.get_pressed()[K_2]:
                self.colide = False
        elif not self.miniHitbox.colliderect(kvadratce):
            self.colide = True

# import inspect
# mros = inspect.getmro(Obekt)
# print(mros)
# child_attrs = dir(mros[0])
# parent_attrs1 = dir(mros[1])
# parent_attrs2 = dir(mros[2])
#
# inherited_attr1 = [item for item in child_attrs if item in parent_attrs1]
# inherited_attr2 = [item for item in child_attrs if item in parent_attrs2]
#
# print(parent_attrs)
# print(child_attrs)
# print(inherited_attr1)
# print(inherited_attr2)
