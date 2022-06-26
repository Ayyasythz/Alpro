while True:
    try:
        inputTahun = int(input("Masukan Tahun yang akan di cek : "))
        if (inputTahun % 4) == 0:
            if (inputTahun % 100) == 0:
                if (inputTahun % 400) == 0:
                    print ("Tahun Kabisat")
                else:
                    print ("Bukan Tahun Kabisat")
            else:
                print ("Tahun Kabisat")
        else:
            print ("Bukan Tahun Kabisat")

    except ValueError:
        print("Salah Input!")



