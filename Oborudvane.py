from pygame import image
from math import ceil
from random import randrange

TIPOVE_ORYZIJA = ['Sword', 'Axe', 'Two-Handed Axe', 'Hammer', 'Dagger']
TIPOVE_BRONI = ['Hat', 'Boot', 'Chest', 'Legs', 'Finger']

prilagatelno = ['above', 'accessory', 'actionable', 'actual', 'additional', 'aforementioned', 'agricultural', 'american', 'ancillary', 'appropriate', 'associated', 'assorted', 'available', 'baked', 'based', 'basic', 'beautiful', 'behavioral', 'best', 'big', 'bigger', 'breakable', 'brief', 'broken', 'bulk', 'bulky', 'bulleted', 'care', 'ceremonial', 'certain', 'cheap', 'chief', 'choice', 'collectible', 'colored', 'commercial', 'common', 'comparable', 'complex', 'concrete', 'consumable', 'content', 'contraband', 'correct', 'corresponding', 'cosmetic', 'cost', 'costly', 'crafted', 'critical', 'crucial', 'cultural', 'curious', 'current', 'dangerous', 'decorative', 'deductible',
                'defective', 'delete', 'deleted', 'deli', 'delicate', 'desirable', 'detailed', 'different', 'difficult', 'discrete', 'discretionary', 'disparate', 'disposable', 'disputed', 'distinct', 'diverse', 'do', 'domestic', 'duplicate', 'earlier', 'easier', 'easy', 'edible', 'electrical', 'electronic', 'end', 'ended', 'enough', 'essential', 'everyday', 'exotic', 'expensive', 'extra', 'extraordinary', 'false', 'familiar', 'fashionable', 'favorite', 'few', 'fewer', 'final', 'financial', 'finished', 'first', 'following', 'food', 'foregoing', 'foreign', 'fragile', 'free', 'frequent', 'fresh', 'functional', 'further', 'general', 'gold', 'good',
                'grammatical', 'great', 'grilled', 'handcrafted', 'handmade', 'have', 'healthy', 'heavier', 'heaviest', 'heavy', 'hidden',
                'historical', 'hot', 'household', 'identical', 'illegal', 'important', 'incidental', 'independent', 'individual', 'inexpensive',
                'informational', 'initial', 'innumerable', 'insignificant', 'intangible', 'interesting', 'inventory', 'irrelevant', 'irreplaceable',
                'isolated', 'kind', 'large', 'larger', 'largest', 'last', 'later', 'latter', 'leading', 'lesser', 'level', 'lexical', 'like',
                'line', 'linguistic', 'little', 'local', 'loose', 'luxury', 'made', 'magical', 'main', 'major', 'manufactured', 'many', 'material',
                'medical', 'metal', 'military', 'minor', 'minute', 'miscellaneous', 'missing', 'more', 'most', 'multiple', 'multiplechoice',
                'mundane', 'natural', 'necessary', 'needed', 'negative', 'new', 'newsworthy', 'next', 'noncash', 'nonessential', 'nonfood',
                'nonperishable', 'novel', 'novelty', 'numerous', 'obvious', 'occasional', 'odd', 'old', 'older', 'on', 'one', 'only', 'open',
                'optional', 'ordinary', 'organic', 'original', 'other', 'outstanding', 'overhead', 'own', 'particular', 'perishable', 'personal',
                'pertinent', 'physical', 'plastic', 'popular', 'positive', 'possible', 'potential', 'practical', 'preceding', 'precious', 'prepaid', 'previous',
                'priced', 'principal', 'printed', 'priority', 'produced', 'profitable', 'promotional', 'purchased', 'quality', 'questionable',
                'random', 'rare', 'real', 'recent', 'recyclable', 'recycled', 'regular', 'related', 'relevant', 'religious', 'report', 'required',
                'respective', 'response', 'restricted', 'retail', 'right', 'sacred', 'same', 'sample', 'scaly', 'scarce', 'scattered', 'seasonal',
                'select', 'selling', 'sensitive', 'sentimental', 'separate', 'several', 'sharp', 'short', 'significant', 'silver', 'similar',
                'simple', 'single', 'small', 'smaller', 'smallest', 'special', 'specialized', 'specific', 'standard', 'stolen', 'strange', 'subsequent', 'such',
                'sundry', 'supplementary', 'surplus', 'suspicious', 'symbolic', 'tangible', 'taxable', 'technical', 'test', 'third', 'ticket', 'time',
                'toiletry', 'top', 'total', 'traditional', 'treasured', 'trivial', 'type', 'typical', 'unfamiliar', 'unimportant', 'unique',
                'unnecessary', 'unneeded', 'unrelated', 'unsold', 'unused', 'unusual', 'unwanted', 'up', 'usable', 'use', 'used', 'useful', 'useless',
                'usual', 'utilitarian', 'valuable', 'value', 'various', 'vegetarian', 'verbal', 'very', 'virtual', 'visible', 'wooden', 'wrong'
                ]


class Item:
    __slots__ = (
        'tip',  'raw_name',  'quantity',  'ikonka', 'cname',  'value',  'netValue',  'attack',  'defence',  'damage',  'HP',  'cooldown',
        'attackPower',  'crit',  'critMultiplier',  'hitChance',  'dodge',  'def_per_secod',  'heal_per_second',  'note')

    def __init__(self, tip, raw_name, value, ikona=None, quantity=1, attack=0, damage=0, defence=0, HP=0, cooldown=0, attackPower=0,
                 crit=0, critMultiplier=0, hitChance=0, dodge=0, heal_per_second=0, def_per_secod=0, note=0):
        # if heal_per_second is None:
        #     heal_per_second = [0, 0]
        # if def_per_secod is None:
        #     heal_per_second = [0, 0]
        self.tip = tip
        self.raw_name = raw_name.strip().lower()
        self.quantity = quantity
        if ikona is not None:
            self.ikonka = image.load(ikona).convert_alpha()
        #self.used = False
        self.cname = None
        self.value = value
        self.netValue = quantity * value

        self.attack = attack
        self.defence = defence
        self.damage = damage
        self.HP = HP
        self.cooldown = cooldown
        self.attackPower = attackPower
        self.crit = crit
        self.critMultiplier = critMultiplier
        self.hitChance = hitChance
        self.dodge = dodge

        self.def_per_secod = def_per_secod
        self.heal_per_second = heal_per_second
        if heal_per_second != 0:
            self.note = f'heal {heal_per_second[0]} amonth for {heal_per_second[1]} secs'
        elif def_per_secod != 0:
            self.note = f'increese defence with {def_per_secod[0]} for {def_per_secod[1]} secs'
        else:
            self.note = note

    def pluss(self, other, tip):
        if 'Sword' == tip:
            if self.tip == 'Sword':
                return _sword_with(self, other)
            else:
                return _sword_with(other, self)
        elif 'Axe' == tip:
            if self.tip == 'Axe':
                return _axe_with(self, other)
            else:
                return _axe_with(other, self)
        elif 'Hammer' == tip:
            if self.tip == 'Hammer':
                return _hammer_with(self, other)
            else:
                return _hammer_with(other, self)
        elif 'Dagger' == tip:
            if self.tip == 'Dagger':
                return _dagger_with(self, other)
            else:
                return _dagger_with(other, self)
        elif 'Hat' == tip:
            if self.tip == 'Hat':
                return _hat_with(self, other)
            else:
                return _hat_with(other, self)
        elif 'Boot' == tip:
            if self.tip == 'Boot':
                return _boot_with(self, other)
            else:
                return _boot_with(other, self)
        elif 'Chest' == tip:
            if self.tip == 'Chest':
                return _chest_with(self, other)
            else:
                return _chest_with(other, self)
        elif 'Legs' == tip:
            if self.tip == 'Legs':
                return _legs_with(self, other)
            else:
                return _legs_with(other, self)
        elif 'Finger' == tip:
            if self.tip == 'Finger':
                return _finger_with(self, other)
            else:
                return _finger_with(other, self)
        else:
            print('no no NOooo ')

    # def __del__(self):
    #     print(f" '{self.raw_name}' is deleted")

    def recalc(self):
        self.netValue = self.quantity * self.value

    def kopiraj(self):
        tmp = Item(self.tip, self.raw_name, self.value, attack=self.attack, damage=self.damage,defence=self.defence, HP=self.HP,cooldown=self.cooldown,
                   attackPower=self.attackPower, crit=self.crit, critMultiplier=self.critMultiplier, hitChance=self.hitChance,dodge=self.dodge, heal_per_second=self.heal_per_second, def_per_secod=self.def_per_secod, note=self.note)
        tmp.ikonka = self.ikonka
        return tmp


def kombinirane(ime1, ime2, procenti):
    novAtaka = ceil(((ime1.attack + ime2.attack) * procenti[0]) + ((ime1.attack + ime2.attack) / 2)) if procenti[0] else 0
    novZastita = max(ime1.defence, ime2.defence)
    novSteta = max(ime1.damage, ime2.damage)
    novHP = ceil((ime1.HP + ime2.HP) * procenti[1] + max(ime1.HP, ime2.HP)) if procenti[1] else 0
    novCD = ceil(((ime1.cooldown + ime2.cooldown) * procenti[2]) + ((ime1.cooldown + ime2.cooldown) / 2)) if procenti[2] else 0
    novCrit = ceil((ime1.crit + ime2.crit) * procenti[3] + max(ime1.crit, ime2.crit)) if procenti[3] else 0
    novCrtMul = max(ime1.critMultiplier, ime2.critMultiplier)
    novHit = ceil(((ime1.hitChance + ime2.hitChance) * procenti[4]) + ((ime1.hitChance + ime2.hitChance) / 2)) if procenti[4] else 0
    novDoj = ceil((ime1.dodge + ime2.dodge) * procenti[5] + max(ime1.dodge, ime2.dodge)) if procenti[5] else 0
    novAP = ceil(ime1.attackPower + ime2.attackPower) if procenti[6] else 0

    if '+' in ime1.raw_name:
        novIme = ime1.raw_name.replace('+', '++')
    elif '+' in ime2.raw_name:
        novIme = ime2.raw_name.replace('+', '++')
    else:
        razno = proizvolno_ime(novAtaka, novZastita, novSteta, novHP, novCD, novAP, novCrit, novCrtMul, novHit, novDoj)
        novIme = razno[0] + ' ' + ime1.raw_name + '+ of the ' + razno[1]

    novStojnost = int((min(ime1.value, ime2.value) / 2) + max(ime1.value, ime2.value))

    return novIme, novStojnost, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit, novCrtMul, novHit, novDoj


def _sword_with(ime1, ime2):
    """ ime1 is a sword and ime2 is an other item """

    if ime2.tip in TIPOVE_ORYZIJA:
        # pcAtaka = 0.25
        # pcHP = 0.25
        # pcCD = 0.05
        # pcCrit = 0.25
        # cpHit = 0.25
        # pcDoj = 0.25
        pcAtaka = 0.15
        pcHP = 0.50
        pcCD = 0.15
        pcCrit = 0.50
        cpHit = 0.15
        pcDoj = 0.50
        isAPon = 1
    else:
        pcAtaka = 0.15
        pcHP = 0.50
        pcCD = 0.15
        pcCrit = 0.50
        cpHit = 0.15
        pcDoj = 0.50
        isAPon = 1
    # novAtaka = ceil(((ime1.attack + ime2.attack) * pcAtaka) + ((ime1.attack + ime2.attack) / 2))
    # novZastita = max(ime1.defence, ime2.defence)
    # novSteta = max(ime1.damage, ime2.damage)
    # novHP = ceil((ime1.HP + ime2.HP) * pcHP + max(ime1.HP, ime2.HP))
    # novCD = ceil(((ime1.cooldown + ime2.cooldown) * pcCD) + ((ime1.cooldown + ime2.cooldown) / 2))
    # novAP = ceil(ime1.attackPower + ime2.attackPower)
    # novCrit = ceil((ime1.crit + ime2.crit) * pcCrit + max(ime1.crit, ime2.crit))
    # novCrtMul = max(ime1.critMultiplier, ime2.critMultiplier)
    # novHit = ceil(((ime1.hitChance + ime2.hitChance) * cpHit) + ((ime1.hitChance + ime2.hitChance) / 2))
    # novDoj = ceil((ime1.dodge + ime2.dodge) * pcDoj + max(ime1.dodge, ime2.dodge))
    #
    # if '+' in ime1.raw_name:
    #     novIme = ime1.raw_name.replace('+', '++')
    # elif '+' in ime2.raw_name:
    #     novIme = ime2.raw_name.replace('+', '++')
    # else:
    #     razno = proizvolno_ime(novAtaka, novZastita, novSteta, novHP, novCD, novAP, novCrit, novCrtMul, novHit, novDoj)
    #     #novIme = ime2.raw_name.split()[0] + ' ' + ime1.raw_name + '+ of the ' + ime2.tip
    #     novIme = razno[0] + ' ' + ime1.raw_name + '+ of the ' + razno[1]
    #
    #
    # novStojnost = int((min(ime1.value, ime2.value) / 2) + max(ime1.value, ime2.value))

    novIme, novStojnost, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit, novCrtMul, novHit, novDoj = kombinirane(ime1, ime2, (pcAtaka,
        pcHP, pcCD, pcCrit, cpHit, pcDoj, isAPon))

    return Item('Sword', novIme, novStojnost, 'data/ikonki/test_sabja.png', 1, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit,
                novCrtMul, novHit, novDoj)


def _axe_with(ime1, ime2):
    """ ime1 is an axe and ime2 is an other item """

    if ime2.tip in TIPOVE_ORYZIJA:
        # pcAtaka = 0.25
        # pcHP = 0.25
        # pcCD = 0.05
        # pcCrit = 0.25
        # cpHit = 0.25
        # pcDoj = 0.25
        pcAtaka = 0.90
        pcHP = 0.10
        pcCD = 0.15
        pcCrit = 0.10
        cpHit = 0.10
        pcDoj = 0.10
        isAPon = 1
    else:
        pcAtaka = 0.90
        pcHP = 0.10
        pcCD = 0.15
        pcCrit = 0.10
        cpHit = 0.10
        pcDoj = 0.10
        isAPon = 1

    # novAtaka = ceil(((ime1.attack + ime2.attack) * pcAtaka) + ((ime1.attack + ime2.attack) / 2))
    # novZastita = max(ime1.defence, ime2.defence)
    # novSteta = max(ime1.damage, ime2.damage)
    # novHP = ceil((ime1.HP + ime2.HP) * pcHP + max(ime1.HP, ime2.HP))
    # novCD = ceil(((ime1.cooldown + ime2.cooldown) * pcCD) + ((ime1.cooldown + ime2.cooldown) / 2))
    # novAP = ceil(ime1.attackPower + ime2.attackPower)
    # novCrit = ceil((ime1.crit + ime2.crit) * pcCrit + max(ime1.crit, ime2.crit))
    # novCrtMul = max(ime1.critMultiplier, ime2.critMultiplier)
    # novHit = ceil(((ime1.hitChance + ime2.hitChance) * cpHit) + ((ime1.hitChance + ime2.hitChance) / 2))
    # novDoj = ceil((ime1.dodge + ime2.dodge) * pcDoj + max(ime1.dodge, ime2.dodge))
    #
    # if '+' in ime1.raw_name:
    #     novIme = ime1.raw_name.replace('+', '++')
    # elif '+' in ime2.raw_name:
    #     novIme = ime2.raw_name.replace('+', '++')
    # else:
    #     razno = proizvolno_ime(novAtaka, novZastita, novSteta, novHP, novCD, novAP, novCrit, novCrtMul, novHit, novDoj)
    #     novIme = razno[0] + ' ' + ime1.raw_name + '+ of the ' + razno[1]
    #
    # novStojnost = int((min(ime1.value, ime2.value) / 2) + max(ime1.value, ime2.value))
    novIme, novStojnost, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit, novCrtMul, novHit, novDoj = kombinirane(ime1, ime2, (
        pcAtaka, pcHP, pcCD, pcCrit, cpHit, pcDoj, isAPon))

    return Item('Axe', novIme, novStojnost, 'data/ikonki/test_bradva.png', 1, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit,
                novCrtMul, novHit, novDoj)


def _hammer_with(ime1, ime2):
    """ ime1 is a hammer and ime2 is an other item """

    if ime2.tip in TIPOVE_ORYZIJA:
        pcAtaka = 0.90
        pcHP = 0.55
        pcCD = 0.15
        pcCrit = 0.10
        cpHit = 0.10
        pcDoj = 0.10
        isAPon = 1
    else:
        pcAtaka = 0.90
        pcHP = 0.55
        pcCD = 0.15
        pcCrit = 0.10
        cpHit = 0.10
        pcDoj = 0.10
        isAPon = 1

    novIme, novStojnost, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit, novCrtMul, novHit, novDoj = kombinirane(ime1, ime2, (
        pcAtaka, pcHP, pcCD, pcCrit, cpHit, pcDoj, isAPon))

    return Item('Hammer', novIme, novStojnost, 'data/ikonki/test_boencuk.png', 1, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit,
                novCrtMul, novHit, novDoj)


def _dagger_with(ime1, ime2):
    """ ime1 is a dagger and ime2 is an other item """

    if ime2.tip in TIPOVE_ORYZIJA:
        pcAtaka = 0.25
        pcHP = 0.25
        pcCD = 0.15
        pcCrit = 0.80
        cpHit = 0.10
        pcDoj = 0.60
        isAPon = 1
    else:
        pcAtaka = 0.25
        pcHP = 0.25
        pcCD = 0.15
        pcCrit = 0.80
        cpHit = 0.10
        pcDoj = 0.60
        isAPon = 1

    novIme, novStojnost, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit, novCrtMul, novHit, novDoj = kombinirane(ime1, ime2, (
        pcAtaka, pcHP, pcCD, pcCrit, cpHit, pcDoj, isAPon))

    return Item('Dagger', novIme, novStojnost, 'data/ikonki/test_kama.png', 1, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit,
                novCrtMul, novHit, novDoj)


def _hat_with(ime1, ime2):
    """ ime1 is a hat and ime2 is an other item """

    if ime2.tip in TIPOVE_ORYZIJA:
        pcAtaka = 0
        pcHP = 0.10
        pcCD = 0
        pcCrit = 0.20
        cpHit = 0.90
        pcDoj = 0.50
        isAPon = 0
    else:
        pcAtaka = 0
        pcHP = 0.10
        pcCD = 0
        pcCrit = 0.20
        cpHit = 0.90
        pcDoj = 0.50
        isAPon = 0

    novIme, novStojnost, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit, novCrtMul, novHit, novDoj = kombinirane(ime1, ime2, (
        pcAtaka, pcHP, pcCD, pcCrit, cpHit, pcDoj, isAPon))

    return Item('Hat', novIme, novStojnost, 'data/ikonki/test_sapka.png', 1, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit,
                novCrtMul, novHit, novDoj)


def _boot_with(ime1, ime2):
    """ ime1 is are boots and ime2 is an other item """

    if ime2.tip in TIPOVE_ORYZIJA:
        pcAtaka = 0.25
        pcHP = 0.25
        pcCD = 0.15
        pcCrit = 0.80
        cpHit = 0.10
        pcDoj = 0.60
        isAPon = 1
    else:
        pcAtaka = 0.25
        pcHP = 0.25
        pcCD = 0.15
        pcCrit = 0.80
        cpHit = 0.10
        pcDoj = 0.60
        isAPon = 1

    novIme, novStojnost, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit, novCrtMul, novHit, novDoj = kombinirane(ime1, ime2, (
        pcAtaka, pcHP, pcCD, pcCrit, cpHit, pcDoj, isAPon))

    return Item('Boot', novIme, novStojnost, 'data/ikonki/test_obuvki.png', 1, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit,
                novCrtMul, novHit, novDoj)


def _chest_with(ime1, ime2):
    """ ime1 is a chest and ime2 is an other item """

    if ime2.tip in TIPOVE_ORYZIJA:
        pcAtaka = 0.25
        pcHP = 0.25
        pcCD = 0.15
        pcCrit = 0.80
        cpHit = 0.10
        pcDoj = 0.60
        isAPon = 1
    else:
        pcAtaka = 0.25
        pcHP = 0.25
        pcCD = 0.15
        pcCrit = 0.80
        cpHit = 0.10
        pcDoj = 0.60
        isAPon = 1

    novIme, novStojnost, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit, novCrtMul, novHit, novDoj = kombinirane(ime1, ime2, (
        pcAtaka, pcHP, pcCD, pcCrit, cpHit, pcDoj, isAPon))

    return Item('Chest', novIme, novStojnost, 'data/ikonki/teniska_test.png', 1, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit,
                novCrtMul, novHit, novDoj)


def _legs_with(ime1, ime2):
    """ ime1 is are legs and ime2 is an other item """

    if ime2.tip in TIPOVE_ORYZIJA:
        pcAtaka = 0.25
        pcHP = 0.25
        pcCD = 0.15
        pcCrit = 0.80
        cpHit = 0.10
        pcDoj = 0.60
        isAPon = 1
    else:
        pcAtaka = 0.25
        pcHP = 0.25
        pcCD = 0.15
        pcCrit = 0.80
        cpHit = 0.10
        pcDoj = 0.60
        isAPon = 1

    novIme, novStojnost, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit, novCrtMul, novHit, novDoj = kombinirane(ime1, ime2, (
        pcAtaka, pcHP, pcCD, pcCrit, cpHit, pcDoj, isAPon))

    return Item('Legs', novIme, novStojnost, 'data/ikonki/test_gasti.png', 1, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit,
                novCrtMul, novHit, novDoj)


def _finger_with(ime1, ime2):
    """ ime1 is a finger and ime2 is an other item """

    if ime2.tip in TIPOVE_ORYZIJA:
        pcAtaka = 0.25
        pcHP = 0.25
        pcCD = 0.15
        pcCrit = 0.80
        cpHit = 0.10
        pcDoj = 0.60
        isAPon = 1
    else:
        pcAtaka = 0.25
        pcHP = 0.25
        pcCD = 0.15
        pcCrit = 0.80
        cpHit = 0.10
        pcDoj = 0.60
        isAPon = 1

    novIme, novStojnost, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit, novCrtMul, novHit, novDoj = kombinirane(ime1, ime2, (
        pcAtaka, pcHP, pcCD, pcCrit, cpHit, pcDoj, isAPon))

    return Item('Finger', novIme, novStojnost, 'data/ikonki/test_prysten.png', 1, novAtaka, novSteta, novZastita, novHP, novCD, novAP, novCrit,
                novCrtMul, novHit, novDoj)


def proizvolno_ime(novAtaka, novZastita, novSteta, novHP, novCD, novAP, novCrit, novCrtMul, novHit, novDoj):
    d = {novAtaka: 'novAtaka', novZastita: 'novZastita', novSteta: 'novSteta', novHP: 'novHP', novCD: 'novCD', novAP: 'novAP', novCrit: 'novCrit',
         novCrtMul: 'novCrtMul', novHit: 'novHit', novDoj: 'novDoj'}

    maxstat = d.get(max(d))

    if maxstat == 'novAtaka':
        zivotno = ['Viper Snake', 'Black Mamba', 'Crocodile', 'Mosquito', ' Human', 'Scorpion', 'Shark', 'Cobra']
        return prilagatelno[randrange(0, 334)], zivotno[randrange(0,8)]
    elif maxstat == 'novZastita':
        zivotno = ['Hedgehog', 'Turtle', 'Armadillo', 'Beaver', 'Koala', 'Lizard']
        return prilagatelno[randrange(0, 334)], zivotno[randrange(0, 6)]
    elif maxstat == 'novSteta':
        zivotno = ['Elk', 'Deer', 'Caribou', 'Impala', 'Moose', 'Antelope', 'Zebra', 'Gazelle']
        return prilagatelno[randrange(0, 334)], zivotno[randrange(0, 8)]
    elif maxstat == 'novHP':
        zivotno = ['Gorilla', 'Hippopotamus', 'Buffalo', 'Bear', 'Rhinoceros', 'Bovinae', 'Bison', 'Elephant seal']
        return prilagatelno[randrange(0, 334)], zivotno[randrange(0, 8)]
    elif maxstat == 'novCD':
        zivotno = ['Dinosaur', 'Elephant', 'Giraffe', 'Mammoth', 'Manatee', 'Panda', 'Vulture', 'Walrus']
        return prilagatelno[randrange(0, 334)], zivotno[randrange(0, 8)]
    elif maxstat == 'novAP':
        zivotno = ['Eagle', 'Falcon', 'Fox', 'Hawk', 'Komodo Dragon']
        return prilagatelno[randrange(0, 334)], zivotno[randrange(0, 5)]
    elif maxstat == 'novCrit':
        zivotno = ['Coyote', 'Dingo', 'Hyena', 'Jackal', 'Wolf', 'Goose']
        return prilagatelno[randrange(0, 334)], zivotno[randrange(0, 6)]
    elif maxstat == 'novCrtMul':
        zivotno = ['Boar', 'Iguana', 'Kangaroo', 'Pig', 'Wasp', 'Badger', 'Hornet']
        return prilagatelno[randrange(0, 334)], zivotno[randrange(0, 7)]
    elif maxstat == 'novHit':
        zivotno = ['Cougar', 'Jaguar', 'Leopard', 'Lion', 'Lynx', 'Panther', 'Cat', 'Cheetah']
        return prilagatelno[randrange(0, 334)], zivotno[randrange(0, 8)]
    elif maxstat == 'novDoj':
        zivotno = ['Hare', 'Dolphin', 'Horse', 'Mouse', 'Bat', 'Crow', 'Dragonfly', 'Fly']
        return prilagatelno[randrange(0, 334)], zivotno[randrange(0, 8)]


class Container:
    def __init__(self, name):
        self.name = name
        self.inside = {}

    def __iter__(self):
        return iter(self.inside.items())

    def __len__(self):
        return len(self.inside)

    def __contains__(self, item):
        return item.raw_name in self.inside

    def __getitem__(self, item):
        return self.inside[item.raw_name]

    def __setitem__(self, item, value):
        self.inside[item.raw_name] = value
        return self[item]

    def add(self, item, quantity=1):
        if quantity < 0:
            raise ValueError("Negative quantity. Use remove() instead")

        if item in self:
            self[item].quantity += quantity
            self[item].recalc()
        else:
            self[item] = item

    def remove(self, item, quantity=1):
        if item not in self:
            raise KeyError("Item not in container")
        if quantity < 0:
            raise ValueError("Negative quantity. Use add() instead")

        if self[item].quantity <= quantity:
            del self.inside[item.raw_name]
        else:
            self[item].quantity -= quantity
            self[item].recalc()


sakk = Container('sakk')

# backpack = Container("Backpack")

# mec = Item("Sword", 'Normal Sword', 10, 2, attack=3)
# mec1 = Item("Sword", 'Swift Sword', 10, 2, attack=4)
# bradva = Item('Axe','Axe' , 12,2, attack=7)
# gold = Item("Gold Coin","Gold Coin", 1, 50)
# potion = Item("Potion", 5)


# backpack.add(gold)


# def purchase(*items):
#     for item in items:
#         if item.value > backpack[gold].quantity:
#             print("You don't have enough money!")
#             print(f"Come back when you have {item.value - backpack[gold].quantity} more gold.")
#         else:
#             backpack.remove(gold, item.value)
#             backpack.add(item)
#             print(f"You purchased a '{item.tip}'")

# print(backpack[gold].quantity)
# purchase(mec, potion)
# print(backpack[gold].quantity)
#
# print(backpack[gold])


# def show_backpack():
#     print()
#     print('________')
#     for n, i in backpack:
#         print(f"{n} / {i.tip}, boj={i}, {i.attack=}")

# backpack.add(mec1)
# forge(mec, bradva)
# forge(mec, bradva)
# show_backpack()
#
#
# forge(backpack.inside.get('xorde+'), backpack.inside.get('xorde+'))
# show_backpack()
