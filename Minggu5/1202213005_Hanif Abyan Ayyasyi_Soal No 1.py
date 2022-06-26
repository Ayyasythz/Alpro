jurusanSMA = str(input("Anda Berasal dari jurusan apa ? (IPA/IPS) \n"))
jurusanIPA = ("Fakultas Rekayasa Industri", "Fakultas Informastika", "Fakultas Ilmu Terapan", "Fakultas Teknik Elektro")
jurusanIPS = ("Fakultas Komunikasi dan Bisnis", "Fakultas Ekonomi dan Bisnis", "Fakultas Industri Kreatif")

match jurusanSMA.lower() :
    case "ipa":
        for x in range(0,len(jurusanIPA)):
            print(f"{x+1}. {jurusanIPA[x]}")
    case "ips":
        for x in range(0, len(jurusanIPS)):
            print(f"{x+1}. {jurusanIPS[x]}")
    case _:
        print("Tidak ada dalam Pilihan")