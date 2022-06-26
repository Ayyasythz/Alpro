angkaAwal = int(input("Masukan Deret Pertama : "))
angkaAkhir = int(input("Sampai Deret Ke berapa : "))

print("1. Menggunakan While Loop \n2. Menggunakan For Loop")
inputMetode = int(input("Gunakan Metode yang mana ? (1 / 2)"))
print("===================================================")

match inputMetode:
    case 1:
        print("Looping ini Menggunakan While \n======================================")
        while angkaAwal < angkaAkhir+1:
            print(f"{2 * (angkaAwal*angkaAwal) - angkaAwal}",end=" ")
            angkaAwal+=1

    case 2:
        print("Looping ini Menggunakan For \n======================================")
        for x in range(angkaAwal,angkaAkhir+1):
            print(f"{(2 * (x * x)) - x}", end=" ")
    case _:
        print("Salah Input Metode!!")

















