from unit import unit
from collections.abc import MutableSequence

class Grouping(MutableSequence):

    @classmethod
    def getClassName(cls):
        return cls.__name__

    def __init__(self, *args, trait = None, **kwargs):
        super(Grouping, self).__init__(*args, **kwargs)
        self.group_trait = trait
        self.members = []


    def check(self, object):
        trait = self.group_trait
        if trait and self[trait] and object[trait]:
            if object[trait] != self[trait]:
                raise TypeError(trait + ' is not equal!',object[trait], self[trait])

    def __getitem__(self, item):
        if type(item) is int:
            return self.members[item]

        values = []

        for member in self.members:
            v = member[item]
            if type(v) is str:
                v = v.replace('*','')
            values.append(v)
        #the grouping doesn't yet have a member that confines its trait
        if len(values) == 0:
            return None
        #these would be individual values, such as HP.
        if len(values) > 1:
            try:
                v = set(values)
                if len(v) == 1:
                    return v.pop()
            except:
                return values
        #these would be collective values, such as category, coherency.
        else:
            return values[0]

    def __setitem__(self, key, value):
        self.check(value)
        self.members[key] = value

    def __len__(self): return len(self.members)

    def __delitem__(self, key): del self.members[key]

    def insert(self, index, object):
        self.check(object)
        self.members.insert(index,object)

    def __repr__(self):
        return self.getClassName() + ': ' + repr(self.members)

class army(Grouping):
    def __init__(self, *args, **kwargs):
        super(army,self).__init__(*args,**kwargs)
        #self.group_trait = 'faction'

class battlegroup(Grouping):
    def __init__(self, *args, **kwargs):
        super(battlegroup, self).__init__(*args,**kwargs)
        self.group_trait = 'category'
    __doc__ = """
            A Battlegroup is a collection of Squads which are activated together (see ‘The Turn Sequence’). 
            A typical Battlegroup will contain between 1 and 3 Squads. Battlegroups normally consist of complementary 
            Squads which together can fulfil a specific battlefield role. For example, an Armour Battlegroup will 
            contain large numbers of tanks, while a support Battlegroup will contain more specialized Squads. 
            Their compositions are defined by the Battlegroup Sheets, which are shown on page 5 of Rulebook 2.4.1.
            """


class squad(unit, Grouping):
    __doc__ = """
            Units normally operate in groups known as ‘Squads’ and as part of a larger formation known as a Battlegroup.
             Your army will usually be made up of several Battlegroups. 

            A Squad is usually a group of identical Units which operate as a cohesive whole. The size of a Squad 
            is defined on the Core Stat Sheet. Units within a Squad move and shoot simultaneously.
            """
    def __init__(self):
        pass
