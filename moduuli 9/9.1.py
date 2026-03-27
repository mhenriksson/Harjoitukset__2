class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, hetkinopeus, kuljettumatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkinopeus = 0
        self.kuljettunopeus = 0

auto = Auto("ABC-123", 142)

print(f"auton rekisteritunnus on:{auto.rekisteritunnus} ja huippunopeus: {auto.huippunopeus}")