barang = ["Komputer Linivi", "Laptop Msu", "Hp Sumsum"]
for x in range(0, len(barang)):
    print(f"{x + 1}. {barang[x]}")

beli = int(input("Anda Ingin Membeli Apa ? \n"))

for x in range(0, len(barang)):
    if beli == x:
        print(f"Barang yang Anda Pilih \n ->{barang[x - 1]} <-")
        checkout = str(input("Apakah Anda Yakin ingi  Checkout ? (y/n) "))
        match checkout:
            case "y":
                print(f"Anda Berhasil Checkout {barang[x - 1]}")
            case "n":
                print(f"Anda Tidak Berhasil Checkout {barang[x - 1]}")
            case _:
                print("Mau beli apa enggak!!")
        print("Terima Kasih!!!")
        break
    if beli > x:
        print("Tidak Ada Product dengan nama itu")
