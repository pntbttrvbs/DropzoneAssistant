from unit import unit

class grouping(list):
    def __init__(self,*args, name = None, faction = None, **kwargs):
        super(grouping,self).__init__(*args,**kwargs)
        self.faction = faction
        self.name = name


class masterModels(grouping):
    def __init__(self,*args, **kwargs):
        super(masterModels, self).__init__(*args,**kwargs)

class army(grouping):
    def __init__(self, *args, **kwargs):
        super(army,self).__init__(*args,**kwargs)

class battlegroup():

    __doc__ = """
            A Battlegroup is a collection of Squads which are activated together (see ‘The Turn Sequence’). 
            A typical Battlegroup will contain between 1 and 3 Squads. Battlegroups normally consist of complementary 
            Squads which together can fulfil a specific battlefield role. For example, an Armour Battlegroup will 
            contain large numbers of tanks, while a support Battlegroup will contain more specialized Squads. 
            Their compositions are defined by the Battlegroup Sheets, which are shown on page 5 of Rulebook 2.4.1.
            """


class squad(unit, grouping):
    __doc__ = """
            Units normally operate in groups known as ‘Squads’ and as part of a larger formation known as a Battlegroup.
             Your army will usually be made up of several Battlegroups. 

            A Squad is usually a group of identical Units which operate as a cohesive whole. The size of a Squad 
            is defined on the Core Stat Sheet. Units within a Squad move and shoot simultaneously.
            """
    def __init__(self):
        pass
