angkaAawal = int(input("Masukan Angka Awal : "))
angkaAkhir = int(input("Masukan Angka Akhir : "))
print("1. Menggunakan While Loop \n2. Menggunakan For Loop")
inputMetode = int(input("Gunakan Metode yang mana ? (1 / 2)"))
print("===================================================")

match inputMetode:
    case 1:
        print("Looping ini Menggunakan While \n======================================")
        while angkaAawal <= angkaAkhir:
            if angkaAawal % 2 == 0:
                print(f"Angka Genap {angkaAawal}")
            if angkaAawal % 2 != 0:
                print(f"Angka Ganjil {angkaAawal}")
            angkaAawal += 1
    case 2:
        print("Looping ini Menggunakan For \n======================================")
        for x in range(angkaAawal, angkaAkhir + 1):
            if x % 2 == 0:
                print(f"Angka Genap {x}")
            if x % 2 != 0:
                print(f"Angka Ganjil {x}")
    case _:
        print("Salah Input Metode!!")