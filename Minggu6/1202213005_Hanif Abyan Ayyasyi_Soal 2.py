angkaAawal = int(input("Masukan Angka Awal : "))
angkaAkhir = int(input("Masukan Angka Akhir : "))
print("1. Menggunakan While Loop \n2. Menggunakan For Loop")
inputMetode = int(input("Gunakan Metode yang mana ? (1 / 2)"))
print("===================================================")

match inputMetode:
    case 1:
        print("Looping ini Menggunakan While \n======================================")
        while angkaAawal <= angkaAkhir:
            if angkaAawal % 15 == 0:
                print("DingDong")
            elif angkaAawal % 5 == 0:
                print("Dong")
            elif angkaAawal % 3 == 0:
                print("Ding")
            else:
                print(angkaAawal)
            angkaAawal += 1
    case 2:
        print("Looping ini Menggunakan For \n======================================")
        for x in range(angkaAawal, angkaAkhir + 1):
            if x % 15 == 0:
                print("DingDong")
            elif x % 5 == 0:
                print("Dong")
            elif x % 3 == 0:
                print("Ding")
            else:
                print(x)
    case _:
        print("Salah Input Metode!!")