import csv
import os
import pickle
import unit
import army

version = 'V2.4.1 (beta)'
source = 'Michigan GT 2018'
#for file in directory:
# TODO: save michigan GT files, iterate through each.
# TODO: review pickle documentation, figure out how to store these inventory lists most effectively.
for file in os.listdir():
    if file[-3:] != 'csv':
        continue
    faction = file.split('.')[0]
    with open(file, newline='') as csvstats:
        statreader = csv.reader(csvstats, delimiter =',')
        curr = None
        nextRow = False
        weapons = False
        inventory = army.masterModels(name = faction , faction = faction)
        for row in statreader:
            print(' '.join(row))
            if row[1] == 'A':
                statHeaders = row
                nextRow = True
            elif nextRow:
                stats = row
                nextRow = False
                name = statHeaders[0]
                type = stats[6].lower()
                if type.lower() == 'walker':
                    type = 'vehicle'
                    stats[10] = stats[10] + ', walker'
                elif type.lower() == 'infantry*':
                    type = type[:-1]
                    stats[10] = stats[10] + ', this unit may not enter structures'
                evalString = 'unit.' + type + '(name,faction)'
                print(evalString)
                newUnit = eval(evalString)
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
                        weaponName = stats[0]
                        newWeapon = unit.weapon(weaponName,faction)
                        for key,value in zip(statHeaders,stats):
                            if key:
                                newWeapon[key] = value
                        newUnit['weapons'].append(newWeapon)
                else:
                    weapons = False
                    inventory.append(newUnit)

    pickle.dump(inventory, open(faction+'.p', 'wb'))




