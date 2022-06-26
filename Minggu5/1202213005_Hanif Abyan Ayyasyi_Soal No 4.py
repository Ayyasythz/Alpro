def eliminasi(mean):
    if mean >= 3.5 and mean <= 4:
        print("Siap menjadi mahasiswa berprestasi")
    elif mean >= 3 and mean < 3.5:
        print("Tingkatkan lagi belajar nya")
    elif mean >= 2 and mean < 3:
        print("Jangan banyak main")
    elif mean >= 0 and mean < 2:
        print("Jangan Banyak Rebahan")
    else:
        print("ANJA* DO")


matpel = ("Alpro", "Matvek", "KKI", "Probstat", "Praktikum Alpro", "Perilaku Organisasi", "B. Indonesia", "PPKn")
nilai = [["A", 4], ["AB", 3.5], ["B", 3], ["BC", 2.5], ["C", 2], ["D", 1.5], ["E", 1]]
sum = 0.0
for x in range(0, len(matpel)):
    nilais = str(input("Masukan Index Nilai {} = ".format(matpel[x]))).upper()
    for y in range(0, len(nilai)):
        if nilai[y][0] == nilais:
            sum += nilai[y][1]

mean = sum / len(matpel)
print("================================")
print("IPS anda Semester ini : {:.2f} ".format(mean))
eliminasi(mean)
