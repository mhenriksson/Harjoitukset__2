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



auto = Auto("ABC-123", 142)
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
auto.tulosta()
auto.kiihdytä(-200)
auto.tulosta()
