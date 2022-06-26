angkaAwal = int(input("Masukan Angka Pertama : "))
selang = int(input("Msukan Selang Angka : "))
angkaAkhir = int(input("Masukan Angka Akhir : "))

print("1. Menggunakan While Loop \n2. Menggunakan For Loop")
inputMetode = int(input("Gunakan Metode yang mana ? (1 / 2)"))
print("===================================================")

match inputMetode:
    case 1:
        print("Looping ini Menggunakan While \n======================================")
        while angkaAwal < angkaAkhir:
            print(angkaAwal, end=" ")
            angkaAwal+=selang

    case 2:
        print("Looping ini Menggunakan For \n======================================")
        for x in range(angkaAwal,angkaAkhir,selang):
            print(x, end=" ")
    case _:
        print("Salah Input Metode!!")


