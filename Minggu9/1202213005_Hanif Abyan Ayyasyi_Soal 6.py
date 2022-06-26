class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
        self.pi = 22 / 7

    def hitungLuasLingkaran(self):
        luasLingkaran = self.pi * (self.jari_jari ** 2)
        return round(luasLingkaran, 2)


class Kerucut(Lingkaran):
    def __init__(self, jari_jari, tinggi):
        super().__init__(jari_jari)
        self.tinggi = tinggi

    def hitungVolumeKerucut(self):
        volumeKerucut = (Lingkaran.hitungLuasLingkaran(self) * self.tinggi) * (1 / 3)
        return round(volumeKerucut, 2)


class Bola(Lingkaran):
    def __init__(self, jari_jari):
        super().__init__(jari_jari)

    def hitungVolumeBola(self):
        volumeBola = (Lingkaran.hitungLuasLingkaran(self) * self.jari_jari) * (4 / 3)
        return round(volumeBola, 2)


print("--------------------- ORIGAMI ---------------------")
jari2_origami = int(input("Jari - Jari : "))
luas_origami = Lingkaran(jari2_origami).hitungLuasLingkaran()
print(f"Luas        : {luas_origami}")
print("--------------------- Cone Ice ---------------------")
jari2_cone_ice = int(input("Jari - Jari : "))
tinggi_cone_ice = int(input("Tinggi      : "))
volume_cone_ice = Kerucut(jari2_cone_ice,tinggi_cone_ice).hitungVolumeKerucut()
print(f"Volume      : {volume_cone_ice}")
print("--------------------- Bowling ---------------------")
jari2_bowling = int(input("Jari - Jari : "))
volume_bowling = Bola(jari2_bowling).hitungVolumeBola()
print(f"Volume      : {volume_bowling}")
