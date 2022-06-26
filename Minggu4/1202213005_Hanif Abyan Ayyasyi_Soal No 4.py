
matpel = ("Matematika","Fisika","Bahasa Indonesia","Bahasa Inggris","Kimia")
sum = 0
for x in range(0, len(matpel)):
    while True :
        nilai = int(input("Masukan Nilai {} = ".format(matpel[x])))
        if nilai not in range(0, 100):
            print("Nilai 0 - 100")
            continue
        else:
            sum += nilai
            break

mean = sum / len(matpel)
print("================================")
print("Rata - Rata Nilai = {}".format(mean))