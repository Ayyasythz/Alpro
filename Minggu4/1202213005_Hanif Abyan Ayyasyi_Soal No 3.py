nama = str(input("Masukan Nama Anda : "))
panjangTanah = int(input("Masukan Panjang Tanah = "))
lebarTanah = int(input("Masukan Lebar Tabah = "))
luas_tanah = panjangTanah * lebarTanah
harga_tanah = luas_tanah * 895000
if nama.lower() == "rudi" :
    harga_tanah = harga_tanah - (harga_tanah * (12.5/100))

print("==================================")
print("Nama = {} \nUang yang Harus Dikeluarkan = Rp. {}".format(nama,harga_tanah))
