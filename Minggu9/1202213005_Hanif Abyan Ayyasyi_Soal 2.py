def luas_persegi(sisi):
    luas  = sisi * sisi
    return luas

def volume_kubus(sisi):
    volume  = sisi * sisi * sisi
    return volume

print("""
    1. Hitung Luas Persegi
    2. Volume Kubus
""")
sisi = int(input("Masukan Nilai Sisi = "))
pilih = int(input("Pilih : "))

match pilih:
    case 1 :
        luas = luas_persegi(sisi)
        print(f"Luas Persegi =  {luas}")
    case 2 :
        volume = volume_kubus(sisi)
        print(f"Volume Kubus =  {volume}")
    case _:
        print("Tidak ada Pilihan!")