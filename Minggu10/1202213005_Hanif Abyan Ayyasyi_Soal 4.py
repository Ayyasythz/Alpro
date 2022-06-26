
import numpy as np

A = np.matrix('8 -8 8 -8;2 4 3 -1;1 3 7 0;-3 1 4 1')
B = np.matrix('2 -1 5 11;2 8 9 8;4 -11 -10 -7;-2 4 7 6')

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
        print(np.linalg.inv(A))
        print(np.linalg.inv(B))
    case _:
        print("Tidak Ada Pilihan")