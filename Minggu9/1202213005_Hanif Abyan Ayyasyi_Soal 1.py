def luas_persegi(sisi):
    luas  = sisi * sisi
    print(f"Hasil Luas = {luas}")

def volume_kubus(sisi):
    volume  = sisi * sisi * sisi
    print(f"Hasil Luas = {volume}")

print("""
    1. Hitung Luas Persegi
    2. Volume Kubus
""")
sisi = int(input("Masukan Nilai Sisi = "))
pilih = int(input("Pilih : "))

match pilih:
    case 1 :
        luas_persegi(sisi)
    case 2 :
        volume_kubus(sisi)
    case _:
        print("Tidak ada Pilihan!")