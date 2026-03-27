import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkinopeus = 0
        self.kuljettumatka = 0

    def tulosta(self):
        print(f"rekisteritunnus:     {self.rekisteritunnus}")
        print(f"Huippunopeus:        {self.huippunopeus}")
        print(f"hetkinopeus:         {self.hetkinopeus}")
        print(f"Kuljettumatka:       {self.kuljettumatka}")



    def kiihdytä(self, nopeudenmuutos):
        self.hetkinopeus += nopeudenmuutos
        if self.hetkinopeus < 0:
            self.hetkinopeus = 0
        if self.hetkinopeus > self.huippunopeus:
            self.hetkinopeus = self.huippunopeus

    def kulje(self, tuntimaara):
        self.kuljettumatka += (self.hetkinopeus * tuntimaara)

autot = []
for i in range(1, 11):
    auto = Auto("ABC-" + str(i), random.randint(100, 200))
    autot.append(auto)

while True:
    for auto in autot:
        m = random.randint(-10, 15)
        auto.kiihdytä(m)
        auto.kulje(1)

    if any(auto.kuljettumatka >= 10000 for auto in autot):
        break

print(f"{'Rekisteritunnus':<20} {'Huippunopeus':>15} {'Hetkinopeus':>15} {'Kuljettumatka':>15}")
print("-" * 65)
for auto in autot:
    print(f"{auto.rekisteritunnus:<20} {auto.huippunopeus:>15} {auto.hetkinopeus:>15} {auto.kuljettumatka:>15}")