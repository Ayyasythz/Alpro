jumlhTangga = int(input("Masukan Tinggi Tangga : "))

print("1. Menggunakan While Loop \n2. Menggunakan For Loop")
inputMetode = int(input("Gunakan Metode yang mana ? (1 / 2)"))
print("===================================================")

match inputMetode:
    case 1:
        print("Looping ini Menggunakan While \n======================================")
        i = 1
        while i < jumlhTangga+1:
            j = 1
            while j <= i:
                print("*", end="")
                j += 1
            print()
            i += 1

    case 2:
        print("Looping ini Menggunakan For \n======================================")
        for x in range(1, jumlhTangga+1):
            for y in range(0, x):
                print("*", end="")
            print()
    case _:
        print("Salah Input Metode!!")
