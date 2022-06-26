list = []
sum = 0

inputJumlahBelian = int(input("Masukan Jumlah Beli : "))
print("1. Menggunakan While Loop \n2. Menggunakan For Loop")
inputMetode = int(input("Gunakan Metode yang mana ? (1 / 2)"))
print("===================================================")

match inputMetode:
    case 1:
        print("Looping ini Menggunakan While \n======================================")
        i,j = 1,0
        while i <= inputJumlahBelian:
            barang = [input("Barang ke {} : ".format(i)), int(input("Harga Barang ke {} : ".format(i)))]
            list.append(barang)
            i += 1

        while j <= len(list):
            sum += list[j][1]

        print(f"Total Harga : Rp.{sum}")

    case 2:
        print("Looping ini Menggunakan For \n======================================")
        for x in range(0, inputJumlahBelian):
            barang = [input("Barang ke {} : ".format(x + 1)), int(input("Harga Barang ke {} : ".format(x + 1)))]
            list.append(barang)
        for y in range(0, len(list)):
            sum += list[y][1]

        print(f"Total Harga : Rp.{sum}")

    case _:
        print("Salah Input Metode!!")

