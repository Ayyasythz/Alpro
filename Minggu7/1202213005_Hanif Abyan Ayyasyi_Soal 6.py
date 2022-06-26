inpS = input("Masukan Kata :")

print("1. Menggunakan While Loop \n2. Menggunakan For Loop")
inputMetode = int(input("Gunakan Metode yang mana ? (1 / 2)"))
print("===================================================")

match inputMetode:
    case 1:
        print("Looping ini Menggunakan While \n======================================")
        i = 0
        while i < len(inpS):
            print(inpS[i:len(inpS)])
            i+=1

    case 2:
        print("Looping ini Menggunakan For \n======================================")
        for x in range(0, len(inpS), 1):
            print(inpS[x:len(inpS)])
    case _:
        print("Salah Input Metode!!")


