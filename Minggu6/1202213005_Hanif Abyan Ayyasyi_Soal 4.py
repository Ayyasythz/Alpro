print("====== Россия ======")
brpUraa = int(input("Berapa URAAAA : "))
print("1. Menggunakan While Loop \n2. Menggunakan For Loop")
inputMetode = int(input("Gunakan Metode yang mana ? (1 / 2) "))
print("===================================================")

match inputMetode:
    case 1:
        print("Looping ini Menggunakan While \n======================================")
        i = 1
        while i <= brpUraa:
            print("brazikowaz sinyom illikipadiedie: URAAAAAAAA")
            i += 1
    case 2:
        print("Looping ini Menggunakan For \n======================================")
        for x in range(0, brpUraa):
            print("brazikowaz sinyom illikipadiedie: URAAAAAAAA")
    case _:
        print("Salah Input Metode!!")