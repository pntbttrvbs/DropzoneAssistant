import csv
import os
import pickle
import unit
import groupings

version = 'V2.4.1 (beta)'
source = 'Michigan GT 2018'
#for file in directory:
# TODO: save michigan GT files, iterate through each.
# TODO: review pickle documentation, figure out how to store these facInv lists most effectively.

inventory = {}

for file in os.listdir():
    if file[-3:] != 'csv':
        continue
    faction = file.split('.')[0]
    newUnits = []
    category = None
    with open(file, newline='') as csvstats:
        statreader = csv.reader(csvstats, delimiter =',')
        curr = None
        nextRow = False
        weapons = False
        facInv = {}
        for row in statreader:
            print(row)
            if row[1] == 'A':
                statHeaders = row
                nextRow = True
            elif nextRow and row[0] != 'WEAPONS':
                stats = row
                name = statHeaders[0]
                if row[0]:
                    name = name + ' - ' + row[0]
                type = stats[6].lower()
                if type == '':
                    nextRow = False
                    continue
                category = stats[7].lower()
                category = category.replace('*','')
                if category not in facInv:
                    facInv[category] = []
                if type.lower() == 'walker':
                    type = 'vehicle'
                    stats[10] = stats[10] + ', walker'
                elif type.lower() == 'infantry*':
                    type = type[:-1]
                    stats[10] = stats[10] + ', this unit may not enter structures'
                evalString = 'unit.' + type + '(name,faction)'
                x = eval(evalString)
                newUnits.append(x)
                for key,value in zip(statHeaders[1:],stats[1:]):
                    if key:
                        if '+' in key:
                            key = key.split('+')
                            value = value.split()
                            for newUnit in newUnits:
                                newUnit[key[0]] = value[0]
                                if len(value)> 1:
                                    newUnit[key[1]] = value[1]
                        else:
                            if key == 'Special':
                                value = value.split(',')
                            for newUnit in newUnits:
                                newUnit[key] = value

            elif row[0] == 'WEAPONS':
                statHeaders = row
                weapons = True
            elif weapons:
                stats = row
                if stats[0]:
                    if not stats[3]:
                        for newUnit in newUnits:
                            newUnit['special'].append(stats[0])
                    else:
                        weaponName = stats[0]
                        newWeapon = unit.weapon(weaponName,faction)
                        for key,value in zip(statHeaders[1:],stats[1:]):
                            if key:
                                newWeapon[key] = value
                        for newUnit in newUnits:
                            newUnit['weapons'].append(newWeapon)
                else:
                    weapons = False
                    nextRow = False
                    while newUnits:
                        print(category)
                        print(facInv)
                        facInv[category].append(newUnits.pop())
        while newUnits:
            facInv[category].append(newUnits.pop())
    inventory[faction] = facInv


pickle.dump(inventory, open('master_inventory.p', 'wb'))




