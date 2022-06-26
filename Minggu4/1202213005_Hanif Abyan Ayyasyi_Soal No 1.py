list = []
jumlahN = int(input("Masukan Jumlah Nilai yang akan dibandingkan = "))
for x in range(0, jumlahN) :
    nilai = [int(input("Nilai ke {} = ".format(x+1)))]
    list.append(nilai)

nilaiMax = list[0]

for x in range(0, len(list)):
    if list[x] > nilaiMax :
        nilaiMax = list[x]

print("Nilai Max = {}".format(nilaiMax[0]))