listBuah = []

print("======== PROGRAM DATA STOK BUAH ========")
jumlahStok = int(input("Masukan Jumlah Stok :"))
for x in range(0,jumlahStok):
    masukanBuah = input(f"Masukan Nama Stok Buah ke-{x+1} : ")
    listBuah.append(masukanBuah)

print(f"Stok Buah: {listBuah}")

