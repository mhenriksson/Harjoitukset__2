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

class kilpailu:
    def __init__(self, nimi, kilometrit, autot):
        self.nimi = nimi
        self.kilometrit = kilometrit
        self.autot = autot


    def tunti_kuluu(self):
        for auto in self.autot:
            m = random.randint(-10, 15)
            auto.kiihdytä(m)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{'Rekisteritunnus':<20} {'Huippunopeus':>15} {'Hetkinopeus':>15} {'Kuljettumatka':>15}")
        print("-" * 65)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<20} {auto.huippunopeus:>15} {auto.hetkinopeus:>15} {auto.kuljettumatka:>15}")

    def kilpailu_ohi(self):

        for auto in self.autot:
            if auto.kuljettumatka >= self.kilometrit:
                return True
        return False

autot = []
for i in range(1, 11):
    auto = Auto("ABC-" + str(i), random.randint(100, 200))
    autot.append(auto)

kilpailu = kilpailu("Suuri romuralli", 8000, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()
print(f"\nKilpailu päättyi {tunti} tuntia ajettu.")