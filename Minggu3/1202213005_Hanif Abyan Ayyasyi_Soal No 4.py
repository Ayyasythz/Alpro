from datetime import datetime

hari = datetime.now().weekday()
list = []
sum = 0

inputJumlahBelian = int(input("Masukan Jumlah Beli : "))

for x in range(0, inputJumlahBelian):
    barang = [input("Barang ke {} : ".format(x + 1)), int(input("Harga Barang ke {} : ".format(x + 1)))]
    list.append(barang)

if hari == 0 or hari == 2:
    for z in range(0, len(list)):
        if list[z][0].lower() == "sayuran" or list[z][0] == "buah - buahan":
            list[z][1] = list[z][1] - (list[z][1] * (15 / 100))

for y in range(0, len(list)):
    sum += list[y][1]

if sum > 300000:
    sum = sum - (sum * (5 / 100))

print("=============================================")
for x in range(0, len(list)):
    print(list[x][0], "= Rp.", int(list[x][1]))
print("=============================================")
print("Total Harga = Rp.", int(sum))
