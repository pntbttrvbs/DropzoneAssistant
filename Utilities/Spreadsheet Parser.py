import csv
import pickle
import unit

version = 'V2.4.1 (beta)'
source = 'Michigan GT 2018'
#for file in directory:
# TODO: save michigan GT files, iterate through each.
# TODO: review pickle documentation, figure out how to store these inventory lists most effectively.
with open('Mich Shaltari Stats.csv', newline='') as csvstats:
    statreader = csv.reader(csvstats, delimiter =',')
    curr = None
    nextRow = False
    weapons = False
    inventory = []
    for row in statreader:
        print(' '.join(row))
        if row[1] == 'A':
            statHeaders = row
            nextRow = True
        elif nextRow:
            stats = row
            nextRow = False
            evalString = 'unit.' + stats[6].lower() +'()'
            newUnit = eval(evalString)
            newUnit['name'] = statHeaders[0]
            for key,value in zip(statHeaders,stats):
                if key:
                    if '+' in key:
                        key = key.split('+')
                        value = value.split()
                        newUnit[key[0]] = value[0]
                        if len(value)> 1:
                            newUnit[key[1]] = value[1]
                    else:
                        newUnit[key] = value
        elif row[0] == 'WEAPONS':
            statHeaders = row
            weapons = True
        elif weapons:
            stats = row
            if stats[0]:
                if not stats[3]:
                    newUnit['special'] = newUnit['special'] + stats[0]
                else:
                    newWeapon = unit.weapon()
                    newWeapon['name'] = stats[0]
                    for key,value in zip(statHeaders,stats):
                        if key:
                            newWeapon[key] = value
                    newUnit['weapons'].append(newWeapon)
            else:
                weapons = False
                inventory.append(newUnit)





