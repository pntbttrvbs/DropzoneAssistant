class army():
    #this is a set of battlegroups, but we'll want to put condititions on this.
    #point size is one of the key features!
    def __init__(self):
        self.battlegroups = []

    @Property
    def pts_size(self):
        return sum(battlegroup.pts_size() for battlegroup in self.battlegroups)

class battlegroup():
    # ditto with squad, might want to get everything else going first.
    # maxSquads is 3

    __doc__ = """
            A Battlegroup is a collection of Squads which are activated together (see ‘The Turn Sequence’). 
            A typical Battlegroup will contain between 1 and 3 Squads. Battlegroups normally consist of complementary 
            Squads which together can fulfil a specific battlefield role. For example, an Armour Battlegroup will 
            contain large numbers of tanks, while a support Battlegroup will contain more specialized Squads. 
            Their compositions are defined by the Battlegroup Sheets, which are shown on page 5 of Rulebook 2.4.1.
            """


class squad(list):
    # should I subclass unit again to get this? or, I could just subclass list; since this is essentially a list.

    __doc__ = """
            Units normally operate in groups known as ‘Squads’ and as part of a larger formation known as a Battlegroup.
             Your army will usually be made up of several Battlegroups. 

            A Squad is usually a group of identical Units which operate as a cohesive whole. The size of a Squad 
            is defined on the Core Stat Sheet. Units within a Squad move and shoot simultaneously.
            """