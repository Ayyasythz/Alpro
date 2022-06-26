jumlahAngka = int(input("Masukan Tinggi Tangga : "))

print("1. Menggunakan While Loop \n2. Menggunakan For Loop")
inputMetode = int(input("Gunakan Metode yang mana ? (1 / 2)"))
print("===================================================")

match inputMetode:
    case 1:
        print("Looping ini Menggunakan While \n======================================")
        i = jumlahAngka+1
        while i > 0:
            j = 0
            while j < i:
                print(j, end="")
                j+= 1
            print()
            i-=1


    case 2:
        print("Looping ini Menggunakan For \n======================================")
        for x in range(jumlahAngka+1,0,-1):
            for y in range(0,x):
                print(y, end="")
            print('')


    case _:
        print("Salah Input Metode!!")
