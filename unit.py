class unit():
    def __init__(self):
        self.statMappings = {'A': 'armour', 'Mv': 'movement speed', 'CM':'countermeasures','DP':'damage points',
                        'Pts':'points', 'Type':'type', 'Category':'category', 'S':'squad size', 'C':'coherency',
                        'T':'transport options', 'Special':'special', 'WEAPONS':'weapons'}

        self.stats = {stat:None for stat in self.statMappings.values()}
        self.stats['coherency'] = 3
        self.stats['weapons'] = []

    __doc__ = "A single model or infantry base is known as a ‘Unit’. " \
              "There are three basic types of these encountered on the battlefield; infantry, vehicles and aircraft."

    def __setitem__(self,key,value):
        if key in self.statMappings:
            key = self.statMappings[key]
        self.stats[key] = value

    def __getitem__(self,key):
        if key in self.statMappings:
            key = self.statMappings[key]
        return self.stats[key]

    def __repr__(self):
        return str(self.stats)

class infantry(unit):
    def __init__(self, **kwargs):
        super(infantry, self).__init__(**kwargs)
        self.statMappings['cqb'] = 'close quarter battle'
        self.statMappings['F'] = 'fortitude'

    __doc__ = """Infantry are soldiers who fight on foot. 
            They are normally slow, poorly armoured, and extremely vulnerable in the open.
            However, infantry are highly useful Units and are often essential to victory. 
            They are the only Units in the game that can garrison Structures and Forests, 
            which makes them tenacious opposition where cover is available.
            
            Infantry are usually mechanized in some way (such as riding in armoured personnel carriers) 
            to give them a measure of protection and speed when en-route to their objectives. 
            Certain elite infantry Units are especially deadly to other infantry 
            during the room to room bloodbath of close quarter battle. 
            Infantry are represented by Bases, with 3-5 individual infantrymen on a base. 
            For game purposes, the whole Base is treated as a single Unit, 
            eliminating the need to move fiddly infantry separately.
            
            Dropzone Commander Beta Rules V2.4.1
            """

    pass

class vehicle(unit):
    def __init__(self, **kwargs):
        super(vehicle, self).__init__(**kwargs)

    __doc__ =  """
            Vehicles are ground based, armoured Units which represent an army’s core fighting force. 
            They can vary from light scout buggies to vast war machines of terrifying proportions. 
            Normally well armoured, they often need to be engaged at closer range due to their employment of 
            countermeasures. 
            
            They can bring potent firepower to bear against other vehicles and scenic features, 
            and are best employed where stalwart resistance or brute force is required. 
            
            Vehicles are typically the fastest ground based Units in an army, and as such are more flexible 
            than infantry on the ground. However, they are often deployed and relocated 
            into the thick of the action by airborne dropships. 
            The only major threat to large vehicles is that presented by powerful weapons. 
            However, they can be vulnerable in the close confines of urban warfare, 
            where many of their advantages against infantry dry up.
            
            Dropzone Commander Beta Rules V2.4.1
            """

    pass

class aircraft(unit):
    def __init__(self, **kwargs):
        super(aircraft, self).__init__(**kwargs)
        self.statMappings['LZ'] = 'landing zone'

    __doc__ = """
            Air superiority is often essential to successful operations. 
            
            Dropships, carriers and gunships operate in a similar manner to helicopters of the 21st century, 
            and are commonplace in most armies. Flights of dropships can be launched with breathtaking speed 
            from low orbit or atmospheric spacecraft, delivering combat troops to hotspots with precision. 
            Without these airborne workhorses, rapid deployment, manoeuvre and redeployment would be impossible. 
            It is often a requirement for an entire attacking army to be deployed from the air, 
            while defenders stand hopelessly outnumbered, praying for deliverance by their own inbound reinforcements. 
            
            Gunships can loiter for extended periods over the battlefield, raining death from above 
            in relentless torrents, providing a constant menace to ground troops. 
            
            Lightning fast aircraft can be called in to drop ordnance on the enemy or to intercept and destroy 
            enemy aircraft. Fast movers make dazzling strafing runs on enemy positions, 
            and vie for aerial supremacy in deadly duels. Strike aircraft can assail virtually any position at any time,
            making them a constant threat to ground forces, while fighters ensure that the sky is never safe. 
            However, their linear movement often makes it necessary to fly over enemy air defences, 
            making them vulnerable to well organised ground fire.
    
            Dropzone Commander Beta Rules V2.4.1
            """

    pass

class weapon(unit):
    def __init__(self):
        self.statMappings = {'E':'energy', 'Sh':'shots','Ac':'accuracy','R(f)':'full range','R(c)':'countered range','Mf':'move and fire','Arc':'arc of fire', 'Special':'special'}
        self.stats = {stat:None for stat in self.statMappings.values()}

    __doc__ = """
            Most Units are equipped with weapons capable of delivering death and destruction to the enemy. 
            The offensive capabilities of a Unit (if it has any) are represented by its Weapons Stat Sheet.
            """



