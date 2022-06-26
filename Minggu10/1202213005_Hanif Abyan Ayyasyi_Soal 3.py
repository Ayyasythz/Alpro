
import numpy as np

A = np.matrix('1 -2;4 2;-1 1')
B = np.matrix('-3 4;-2 1;3 6')

print("""
     1. A + B
     2. A - B
     3. A x B
     4. A / D
     5. Inverse
 """)

pilih = int(input("Masukan Pilihan : "))

match pilih:
    case 1 :
        a = A + B
        print(a)
    case 2 :
        a = A - B
        print(a)
    case 3 :
        a = A * B
        print(a)
    case 4:
        a = A / B
        print(a)
    case 5:
        arr11 = np.array([[1,-2],[4,2]])
        arr22 = np.array([[-3, 4], [-2, 1]])
        print(np.linalg.inv(arr11))
        print(np.linalg.inv(arr22))
    case _:
        print("Tidak Ada Pilihan")


