class weapon(object):
    def __init__(self, name, Range, Type, S, AP, D, Abilities):
        self.name = name
        self.Range = Range
        self.Type = Type
        self.S = S
        self.AP = AP
        self.D = D
        self.D = Abilities

    def print_name(self):
        return self.name

    def print_Range(self):
        return self.Range

    def print_Type(self):
        return self.Type

    def print_S(self):
        return self.S

    def print_AP(self):
        return self.AP

    def print_D(self):
        return self.D

    def print_Abilities(self):
        return self.Abilities
