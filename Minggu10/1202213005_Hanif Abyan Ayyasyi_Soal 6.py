listBelanjaan = []
sumHarga = 0
listHargaHasilKali = []

jumlahBeli = int(input("Masukan Jumlah Pembelian : "))


def printListASCHarga():
    listSort = sorted(listBelanjaan, key=lambda l: l[3], reverse=True)
    print("NO".ljust(3),"BELANJAAN".ljust(1520),"Jumlah".ljust(20),"Harga Satuan".ljust(20),"Total Harga".ljust(20))
    for y in range(0, len(listSort)):
        print(str(y + 1).ljust(3), listSort[y][0].ljust(20), str(listSort[y][1]).ljust(20),
              str(listSort[y][2]).ljust(20), str(listSort[y][3]).ljust(20))
    print("=============================================================================================")

def printListASCJML():
    listSort = sorted(listBelanjaan, key=lambda l: l[1], reverse=True)
    print("NO".ljust(3), "BELANJAAN".ljust(20), "Jumlah".ljust(20), "Harga Satuan".ljust(20), "Total Harga".ljust(20))
    for y in range(0, len(listSort)):
        print(str(y + 1).ljust(3), listSort[y][0].ljust(20), str(listSort[y][1]).ljust(20),
              str(listSort[y][2]).ljust(20), str(listSort[y][3]).ljust(20))
    print("=============================================================================================")

def printListBelanjaan():
    print("NO".ljust(3), "BELANJAAN".ljust(20), "Jumlah".ljust(20), "Harga Satuan".ljust(20), "Total Harga".ljust(20))
    for y in range(0, len(listBelanjaan)):
        print(str(y + 1).ljust(3), listBelanjaan[y][0].ljust(20), str(listBelanjaan[y][1]).ljust(20),
              str(listBelanjaan[y][2]).ljust(20), str(listBelanjaan[y][3]).ljust(20))
    print("=============================================================================================")


l = True
while l:
    if len(listBelanjaan) == 0:
        for x in range(0, jumlahBeli):
            pembelian = [input(f"Masukan Nama Barang ke {x + 1} :"),
                         int(input(f"Masukan Jumlah Barang ke {x + 1}: ")),
                         int(input(f"Masukan Harga Barang ke {x + 1} :")), 0]
            listBelanjaan.append(pembelian)
            hasilkali = listBelanjaan[x][1] * listBelanjaan[x][2]
            listBelanjaan[x][3] = hasilkali

    else:
        lups = True
        while lups == True:
            print("""
            ===================================
            1. Print Struk
            2. Tambah Belanjaan
            3. Hapus Index
            4. Ganti Jumlah Belanjaan
            5. Struk Sort Harga
            6. Struk Sort Jumlah Belanjaan
            ==================================
            """)
            pilihan = int(input("Masukan Angka Pilihan : "))
            match pilihan:
                case 1:
                    printListBelanjaan()
                    for y in range(0, len(listBelanjaan)):
                        hasilkali = listBelanjaan[y][1] * listBelanjaan[y][2]
                        sumHarga += hasilkali
                    print(f"Total Harga = {sumHarga}")
                    sumHarga = 0
                    lups = False
                    l = False
                case 2:
                    tambahan = [input(f"Masukan Belanjaan Tambahan : "), int(input(f"Masukan Jumlah Belian : ")),
                                int(input(f"Masukan Harga :"))]
                    listBelanjaan.append(tambahan)
                case 3:
                    printListBelanjaan()
                    batal = int(input("Inputkan Index yang akan di Hapus : "))
                    listBelanjaan.pop(batal - 1)
                case 4:
                    printListBelanjaan()
                    indexGanti = int(input("Masukan Index Belian yang akan diganti : "))
                    jumlahGanti = int(input("Masukan Jumlah yang baru : "))
                    listBelanjaan[indexGanti - 1][1] = jumlahGanti
                    print(listBelanjaan)
                case 5:
                    printListASCHarga()
                    lups = False
                    l = False
                case 6:
                    printListASCJML()
                    lups = False
                    l = False
