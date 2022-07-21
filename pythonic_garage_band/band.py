class Band:
    instances = []
    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.instances.append(self)

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())

        return solos

    @classmethod
    def to_list(cls):
        return cls.instances

class Musician(Band):
    def __init__(self, name):
        self.name = name

    def play_solo(self):
        return self.solo

    def get_instrument(self):
        return self.instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"



class Guitarist(Musician):
    solo = "face melting guitar solo"
    instrument = "guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist(Musician):
    solo = "bom bom buh bom"
    instrument = "bass"


    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Musician):
    solo = "rattle boom crash"
    instrument = "drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"