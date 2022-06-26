print("1. Menggunakan While Loop \n2. Menggunakan For Loop")
inputMetode = int(input("Gunakan Metode yang mana ? (1 / 2)"))
print("===================================================")

match inputMetode:
    case 1:
        print("Looping ini Menggunakan While \n======================================")
        i = 15
        while i > 0:
            j = 3
            while j < i:
                if (j % 2) != 0 :
                    print(j, end=" ")
                j+=1
            print("\r")
            i-=1


    case 2:
        print("Looping ini Menggunakan For \n======================================")
        for x in range(15,0,-1):
            for y in range(3,x,2):
                print(y, end=" ")
            print("")








    case _:
        print("Salah Input Metode!!")
