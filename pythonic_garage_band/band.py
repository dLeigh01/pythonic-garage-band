class Band:
    instances = []
    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.instances.append(self)

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{type(self).__name__} instance. Name = {self.name}"

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


class Guitarist(Musician):
    solo = "face melting guitar solo"
    instrument = "guitar"


class Bassist(Musician):
    solo = "bom bom buh bom"
    instrument = "bass"


class Drummer(Musician):
    solo = "rattle boom crash"
    instrument = "drums"