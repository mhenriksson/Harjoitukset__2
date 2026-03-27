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



auto = Auto("ABC-123", 142)
auto.kiihdytä(100)
auto.kulje(1.5)