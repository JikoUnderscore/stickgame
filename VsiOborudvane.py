from Oborudvane import Item
#import pympler.asizeof as razmer

mec = Item("Sword", 'Long Sword', 10, 'data/ikonki/sabja.png', 4, attack=8, cooldown=8)
mec1 = Item("Sword", 'Swift Sword', 10, 'data/ikonki/kysjasabja.png', 1, attack=4, cooldown=5)
bradva = Item('Axe', 'Heavy Axe', 12, 'data/ikonki/bradva.png', 4, attack=7, cooldown=7)
t1 = Item('Sword', 'sharp Sword', 12, 'data/ikonki/goljamec.png', 1, attack=10, cooldown=10)
t2 = Item('Axe', 'slow Axe', 12, 'data/ikonki/bradvazadyrva.png', 1, attack=8, cooldown=7)
t3 = Item('Hammer', 'the big Hammer', 12, 'data/ikonki/kovacencuk.png', 1, attack=20, cooldown=20)
t4 = Item('Dagger', 'swift knife', 12, 'data/ikonki/noc.png', 1, attack=5, cooldown=2)
t5 = Item('Hammer', 'G.F. Crowbar', 12, 'data/ikonki/kozikrak.png', 1, attack=4, cooldown=4)
t6 = Item('Sword', 'Bone Sword', 12, 'data/ikonki/mecotkost.png', 1, attack=6, cooldown=6)
t7 = Item('Dagger', 'short knife', 12, 'data/ikonki/dylygnoz.png', 1, attack=4, cooldown=2)
t8 = Item('Dagger', 'gay Dagger', 12, 'data/ikonki/krivnoz.png', 1, attack=4, cooldown=6)
t9 = Item('Sword', 'black Sword', 12, 'data/ikonki/goljammec.png', 1, attack=9, cooldown=9)
sapk = Item('Hat', 'good hat', 7, 'data/ikonki/izgorenasapka.png', defence=1, HP=5)
boot = Item('Boot', 'good boots', 7, 'data/ikonki/butusi.png', defence=1, HP=6, attackPower=10)


h1 = Item('Hat', 'Gas Mask', 4, 'data/ikonki/gazovamaska.png', defence=1, HP=6, hitChance=5)
h2 = Item('Hat', 'Militery Hat', 9, 'data/ikonki/grenadir.png', attackPower=19, attack=2, defence=1, HP=2)
h3 = Item('Hat', 'lucky 7', 7, 'data/ikonki/kysmet.png', defence=1, HP=7, attackPower=7, crit=7, critMultiplier=7, dodge=7)
h4 = Item('Hat', 'Miner Hat', 4, 'data/ikonki/minnakaska.png', defence=1, HP=13, dodge=5)
h5 = Item('Hat', 'War Hat', 13, 'data/ikonki/pehotnakaska.png', defence=1, HP=18, attackPower=3)

sh1 = Item('Chest', 'lucky shirt 7', 7, 'data/ikonki/potnik.png', defence=1, HP=7, attackPower=7, crit=7, critMultiplier=7, dodge=7)
w = Item('Sword', 'lucky sword 7', 7, 'data/ikonki/kysjasabja.png', defence=1, HP=7, attackPower=7, crit=7, critMultiplier=7, dodge=7)
sh2 = Item('Chest', 'Warm Sweter', 14, 'data/ikonki/pilover.png', defence=1, HP=16)
sh3 = Item('Chest', 'Robe 3', 8, 'data/ikonki/roba.png', attackPower=23, defence=1)
sh4 = Item('Chest', 'T-Shirt', 9, 'data/ikonki/teniska.png', attack=2, HP=10, hitChance=9)
sh5 = Item('Chest', 'Leather Vest', 9, 'data/ikonki/kozenagrejka.png', critMultiplier=3, crit=10, defence=1)

p1 = Item('Legs', 'Lucky pants', 7, 'data/ikonki/sportnigasti.png', defence=1, HP=7, attackPower=7, crit=7, critMultiplier=7, dodge=7)
p2 = Item('Legs', 'Hairy Long Pants', 8, 'data/ikonki/kozenigasti.png', HP=13, defence=1, hitChance=3)
p3 = Item('Legs', 'Shorts', 11, 'data/ikonki/kysigasti.png', attackPower=15, hitChance=5)
p4 = Item('Legs', 'Fantsy Pants', 9, 'data/ikonki/krasivigasti.png', defence=1, attack=1, hitChance=2, dodge=3)
p5 = Item('Legs', "Sergent's Underwere", 7, 'data/ikonki/kargopasti.png', defence=1, HP=10, attackPower=2)


r1 = Item('Finger', 'Ring of the Lion', 13, 'data/ikonki/lyvprysten.png', 1, attackPower=36, hitChance=-9, attack=3)
r2 = Item('Finger', 'Ring of the Bear', 12, 'data/ikonki/meckaprysten.png', 1, HP=15, defence=1, cooldown=4, note='Increeses the atk CD by "Use CD"')
r3 = Item('Finger', 'Ring of the Bird', 13, 'data/ikonki/pticaprysten.png', 1, cooldown=-5, HP=-26,           note='Reduses atk CD by "Use CD"') #
r4 = Item('Finger', 'Ring of the Snake', 12, 'data/ikonki/zmijaprysten.png', 1, critMultiplier=2, crit=25, HP=-20, defence=-1)
r5 = Item('Finger', 'Ring of the Monkey', 13, 'data/ikonki/majmunaprysten.png', 1, dodge=25, attack=-8)

r6 = Item('Finger', 'Assault Band', 12, 'data/ikonki/aprysten.png', 1, attack=1, attackPower=15)
r7 = Item('Finger', 'Vigor Band', 11, 'data/ikonki/bprysten.png', 1, HP=10)
r8 = Item('Finger', 'Focus Band',11, 'data/ikonki/cprysten.png', 1, cooldown=-1)
r9 = Item('Finger', 'Bone Band', 12, 'data/ikonki/dprysten.png',  1, crit=5, critMultiplier=1.5)
r10 = Item('Finger', 'Ivory Band', 13, 'data/ikonki/eprysten.png', 1, dodge=5)

hp4 = Item('Mis', 'Bandage', 8, 'data/ikonki/lepinka.png',           HP=5,  cooldown=10, note='haels by +HP')
hp1 = Item('Mis', 'Bandage 2', 5, 'data/ikonki/lepinka.png',         HP=10, cooldown=20, note='Haels by +HP')
hp5 = Item('Mis', 'First Aid Kit', 10, 'data/ikonki/pyrvanuzda.png', HP=20, cooldown=30, note='haels by +HP')

hp2 = Item('Mis', 'Food', 5, 'data/ikonki/hotdog.png', cooldown=5, heal_per_second=(3, 3))
hp3 = Item('Mis', 'Sheald', 6, 'data/ikonki/sejf.png', cooldown=5, def_per_secod=(5, 3))

dm1 = Item('Mis', 'damage 1', 8, 'data/ikonki/butilka1.png', cooldown=9, damage=5, HP=-3, note='deal dmg to the enemy at the cost of HP')
dm2 = Item('Mis', 'damage 2', 8, 'data/ikonki/butilka2.png', cooldown=11, damage=8, HP=-6, note='deal dmg to the enemy at the cost of HP')
dm3 = Item('Mis', 'damage 3', 8, 'data/ikonki/butilka3.png', cooldown=13, damage=11, HP=-7, note='deal dmg to the enemy at the cost of HP')
dm4 = Item('Mis', 'damage 4', 8, 'data/ikonki/butilka4.png', cooldown=15, damage=14, HP=-8, note='deal dmg to the enemy at the cost of HP')
dm5 = Item('Mis', 'damage 5', 8, 'data/ikonki/butilka5.png', cooldown=17, damage=17, HP=-9, note='deal dmg to the enemy at the cost of HP')

testpredmet = Item('Mis', 'TEST ITEM NAME', 9, 'data/ikonki/butilka5.png',1,6,6,6,6,6,6,6,6,6,6,note='This is a two row sentence This is a two row sentence This is a two row sentence')

# print(razmer.asizesof(mec,mec1,bradva,t1,t2,t3,t4,t5,t6,t7,t8,t9,sapk,boot,h1,h2,h3,h4,h5,sh1,w,sh2,sh3,sh4,sh5,p1,p2,p3,p4,p5,r1,r2,r3,r4,r5,r6,
#                       r7,r8,r9,r1,hp1,hp2,hp3,hp4,hp5,dm1,dm2,dm3,dm4,dm5, testpredmet, code=True))
# print(razmer.asizeof(mec,mec1,bradva,t1,t2,t3,t4,t5,t6,t7,t8,t9,sapk,boot,h1,h2,h3,h4,h5,sh1,w,sh2,sh3,sh4,sh5,p1,p2,p3,p4,p5,r1,r2,r3,r4,r5,r6,
#                       r7,r8,r9,r1,hp1,hp2,hp3,hp4,hp5,dm1,dm2,dm3,dm4,dm5, testpredmet, code=True))

if __name__ == '__main__':
    # ne izpolzvani

    z1 = Item('Trinket', 'Trinket 1', 20, '???', note='Has a 1% chance to be imune for the rest of the fight')
    z2 = Item('Trinket', 'Trinket 2', 50 , '????', cooldown=30, note='Stuns target for 3 seconds')
    z3 = Item('Trinket', 'Trinket 3', 40, '???', note='Increese healing by 25%')
    z4 = Item('Trinket', 'Trinket 4', 35, '???', note='Heal 5HP when you deal damage')
    z5 = Item('Trinket', 'Trinket 5', 50, '???', note='Has 5% chance when struck in combat to increase all stats by 5')
    z6 = Item('Trinket', 'GUn 1', 20, '???', cooldown=10, damage=10)
    z7 = Item('Trinket', 'multy shooter', 30,'????', cooldown=6, damage=3, note='Shots target two times')
