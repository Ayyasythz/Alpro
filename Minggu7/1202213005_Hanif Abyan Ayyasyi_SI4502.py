
harga = [["Nasi Padang", 25000], ["Jus", 15000]]
uangDewi = 5000
inputJmlNP = int(input("Ingin Beli Nasi Padang Berapa Bungkus = "))
jumlahJmlJUS = int(input("Ingin Beli Jus Berapa Bungkus = "))


sumHarga = (harga[0][1] * inputJmlNP) + (harga[1][1] * jumlahJmlJUS)

print(f"Total Harga : {sumHarga}")
print("""
    1. Pembayaran Konvensional
    2. Pembayaran O-Pay
""")
pembayaran = int(input("Masukan Jenis Pembayaran (1 / 2) : "))

match pembayaran:
    case 1:
        print("Anda Memilih Pembayaran Konvensional")
        jumlahUang = int(input("Masukan Jumlah Uang : "))
        jumlahUang -= sumHarga
        print("=== Transaksi Berhasil ===")
        print(f"Kembalian : {jumlahUang}")
    case 2:
        print("Anda Memilih Pembayaran O-Pay")
        print(f"Saldo Anda : {uangDewi}")
        jumlahUang = int(input("Masukan Jumlah Saldo O-Pay : "))
        uangDewi += jumlahUang
        if sumHarga > 25000:
            sumHarga = sumHarga - (sumHarga * (20/100))
        elif 25000 > sumHarga > 0:
            sumHarga = sumHarga - (sumHarga * (10/100))

        if uangDewi < sumHarga:
            print("Saldo Anda Kurang!!")
            lups = True
            while lups:
                s = input("Apakah Anda Ingin Top Up ? (y/n) :")
                if s.lower() == "y":
                    topUp = int(input("Masukan Saldo Top Up : "))
                    uangDewi += topUp
                    print(f"Saldo Anda : {uangDewi}")
                elif s.lower() == "n":
                    lups = False
            uangDewi -= sumHarga
            print("=== Transaksi Berhasil ===")
            print(f"Kembalian : {uangDewi}")
        else:
            print("=== Transaksi Berhasil ===")
            uangDewi -= sumHarga
            print(f"Kembalian : {uangDewi}")
    case _:
        print("Tidak Ada Metode Pembayaran")
