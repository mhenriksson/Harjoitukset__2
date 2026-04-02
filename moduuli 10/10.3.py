class hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohdekerros):
        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(hissien_lkm):
            self.hissit.append(hissi(alin_kerros, ylin_kerros))

    def aja_hissia(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)

    def palohaly(self):
        print("Palohälytys, siirry alimpaan kerrokseen.")

talo = Talo(1, 10, 3)

hissin_numero = int(input("Minkä hissin haluat valita? (0-2): "))
kohdekerros = int(input(f"Mille kerrokselle ajat? ({talo.alin_kerros}-{talo.ylin_kerros}): "))
talo.aja_hissia(hissin_numero, kohdekerros)
print("Saavuit paikalle.")

print()
talo.palohaly()

