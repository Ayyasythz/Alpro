indexNilai = ""

while True:
    nilai = int(input("Inputkan Nilaimu: "))
    if nilai not in range(0, 100):
        print("Nilai rentang 0 - 100")
        continue
    else:
        if nilai in range(0, 41):
            indexNilai = "E"
        elif nilai in range(41, 51):
            indexNilai = "D"
        elif nilai in range(51, 61):
            indexNilai = "C"
        elif nilai in range(61, 66):
            indexNilai = "BC"
        elif nilai in range(66, 71):
            indexNilai = "B"
        elif nilai in range(71, 81):
            indexNilai = "AB"
        else:
            indexNilai = "A"
    break

print("Grade: {}".format(indexNilai))
