menu = [["Nasi Padang", "Makanan", 25000], ["Nasi Pecel", "Makanan", 20000], ["Gado-gado", "Makanan", 15000],
        ["Es Teh Manis", "Minuman", 5000], ["Chat time Boba", "Minuman", 10000], ["Air Mineral", "Minuman", 5000]]
listBayar = []


def printMenu():
    print("========================= MENU =========================")
    for x in range(0, len(menu)):
        print(
            f"{str(x + 1).ljust(3)}| " + f"{menu[x][0].ljust(15)}" + f"{menu[x][1].rjust(15)}" + f"{str(menu[x][2]).rjust(15)}")
    print("========================================================")


def bayar_konvensional(uang, total_bayar):
    global uangTemp
    uangTemp = uang
    uangTemp -= total_bayar
    return uangTemp


def bayar_opay(saldoTemp, total_bayar):
    global saldo
    saldo = saldoTemp
    print(f"Saldo Anda : {saldo}")
    if total_bayar > 25000:
        total_bayar = total_bayar - (total_bayar * (20 / 100))
    elif 25000 > total_bayar > 0:
        total_bayar = total_bayar - (total_bayar * (10 / 100))

    while saldo < total_bayar:
        print("Saldo Anda Kurang!!")
        lups = True
        while lups:
            s = input("Apakah Anda Ingin Top Up ? (y/n) :")
            if s.lower() == "y":
                topUp = int(input("Masukan Saldo Top Up : "))
                saldo += topUp
            elif s.lower() == "n":
                lups = False

    saldo -= total_bayar




def printstruk(total_bayar, jenis_bayar, uangbayar):
    print("========================= STRUK =========================")
    for x in range(0, len(listBayar)):
        print(f"{listBayar[x][0].rjust(5)}" + f"{str(listBayar[x][1]).rjust(13)}")
    print("=========================================================")
    print(f"Total : Rp. {total_bayar}")
    if jenis_bayar == 1:
        a = bayar_konvensional(uangbayar, total_bayar)
        print(f"Kembalian = Rp. {a}")
    elif jenis_bayar == 2:
        print(f"Sisa Saldo = Rp. {saldo}")
    print("========================================================")


def bayar(jenis_bayar):
    global total_bayar
    total_bayar = 0
    for x in range(0, len(listBayar)):
        total_bayar += listBayar[x][1]

    match jenis_bayar:
        case 1:
            print("Anda Memilih Pembayaran Konvensional")
            uangbayar = int(input("Masukan Nominal Uang : "))
            bayar_konvensional(uangbayar, total_bayar)
            printstruk(total_bayar, jenis_bayar, uangbayar)
        case 2:
            print("Anda Memilih Pembayaran Opay")
            saldo_opay = int(input("Masukan Saldo Opay Anda : "))
            bayar_opay(saldo_opay, total_bayar)
            printstruk(total_bayar, jenis_bayar, saldo_opay)


printMenu()
lups = True
while lups:
    pesanMenu = int(input("Masukan Index Menu : "))
    print(f"===== Menu ===".rjust(5) + f"=== Harga =====".rjust(10))
    print(f"{menu[pesanMenu - 1][0].rjust(5)}" + f"{str(menu[pesanMenu - 1][2]).rjust(13)}")
    jumlahBeli = int(input("Beli Berapa : "))
    listBayarTemp = [menu[pesanMenu - 1][0], menu[pesanMenu - 1][2] * jumlahBeli]
    listBayar.append(listBayarTemp)
    lagi = input("Tambah Menu ? (y/n) ").lower()
    match lagi:
        case "y":
            lups = True
        case "n":
            print("==================================================")
            lups = False
        case _:
            print("==================================================")
            lups = False
print("""
    1. Pembayaran Konvensional
    2. Pembayaran O-Pay
""")
jenis_pembayaran = int(input("Jenis Pembayaran (1-2) : "))
bayar(jenis_pembayaran)
