'''

id,QuestType,Active,Title,Description,goals,min,max
0,KILL,0,Troble in the town,Slay the PIG boss and his lieutenets,PIG boss slain {}/{}. \n Pig lieutenets slayn {}/{},0 0,1 4
1,KILL,0,Bunny Killer,Find and slay a rabbit,Rabbits slain {}/{},0,1
2,KILL,0,Slay flowers, Kill the flower mosters, Rose monster slain {}/{}. \n Dendilion monster slain {}/{}. \n Grass monster slain {}/{}.,0 0 0,5 6 7


'''
import csv
from pprint import pprint


def load_quest(id_number):
    with open('data/Quests/base_quests.csv', 'r') as basaQuest:
        reader = csv.DictReader(basaQuest)

        with open('data/Quests/active_quests.csv', 'a', newline='') as activQwriter:
            aq_writer = csv.writer(activQwriter)
            with open('data/Quests/active_quests.csv', 'r') as activQreader:
                aq_reder = csv.DictReader(activQreader)

                iflist = []

                for red in reader:
                    if red['id'] == str(id_number):
                        for activeRed in aq_reder:
                            iflist.append(activeRed['id'] != red['id'])
                        if all(iflist):
                            aq_writer.writerow(red.values())


def update_quest(id_number, *objectives:int):
    outLst = []

    with open('data/Quests/active_quests.csv', 'r') as activQreader:
        aq_reder = csv.DictReader(activQreader)

        for line in aq_reder:
            if line['id'] == str(id_number) and line['Active'] != '1':
                newObje = ' '.join(str(x) for x in objectives).split(' ')
                noviStojnosti = [int(x) for x in newObje]

                stariStojnosti = [int(x) for x in line['min'].split(' ')]
                sborStojnosti = map(lambda z, y: str(z + y), noviStojnosti, stariStojnosti)
                line['min'] = ' '.join(list(sborStojnosti))

                cilsaMax = [int(x) for x in line['max'].split(' ')]
                cislaMin = [int(x) for x in line['min'].split(' ')]
                daliPrikljuceno = map(lambda w, h: w >= h, cislaMin, cilsaMax)
                if all(daliPrikljuceno):
                    line['Active'] = '1'
                outLst.append(line)
            else:
                outLst.append(line)



    with open('data/Quests/active_quests.csv', 'w', newline='') as activQwriter:

        aq_writer = csv.DictWriter(activQwriter, fieldnames=['id','QuestType','Active','Title','Description','goals','min','max'])
        aq_writer.writeheader()
        for rite in outLst:
            aq_writer.writerow(rite)


#load_quest(0)
#load_quest(1)
update_quest(0, 1,1)
update_quest(1, 1)
update_quest(2, 2,2,2)
