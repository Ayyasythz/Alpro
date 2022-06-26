list = []
sum = 0
lups = True
jumlahMatkul = int(input("Masukan Jumlah Pelajaran yang akan di input pada Semester ini : "))

for x in range(0, jumlahMatkul):
        matkul = [input("Nama Matkul ke {} : ".format(x + 1)), float(input("Nilai Matkul ke {} : ".format(x + 1)))]
        list.append(matkul)

for y in range(0, len(list)):
    sum += list[y][1]

hasilIPS = sum / len(list)

print("=================================")
for z in range(0, len(list)):
    print(list[z][0])
    print("  Nilai = ", list[z][1])
print("=================================")
print("IPS anda semester ini = ", hasilIPS)
if hasilIPS >= 3.5 :
    print("Selamat anda bisa mendaftar Beasiswa")
else:
    print("Jangan banyak rebahan")
