def cekUmur(umur):
    if 0 < umur <= 5:
        print("Masa Balita")
    elif 5 < umur <= 12:
        print("Masa Kanak-kanak")
    elif 12 < umur <= 25:
        print("Masa Remaja")
    elif 25 < umur <= 45:
        print("Masa Dewasa")
    elif 45 < umur <= 65:
        print("Masa Lansia")
    else:
        print("Masa Manula")


def cekBMI(berat, tinggi):
    bmi = berat / (tinggi ** 2)
    kategori = ""
    if bmi < 18.5:
        kategori = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        kategori = "Normal"
    elif 25 <= bmi <= 29.9:
        kategori = "Overweight"
    elif 30 <= bmi <= 34.9:
        kategori = "Obese"
    elif 45 <= bmi <= 39.9:
        kategori = "Very Obese"
    else:
        kategori = "Extremely Obese"

    print(f"Nilai BMI anda adalah {bmi} termasuk kategori {kategori}")


print(">>>>* KATEGORI UMUR *<<<<")
umur = int(input("Masukan Umur anda = "))
print("Anda berada pada : ")
print("=================================")
cekUmur(umur)
beratBadan = float(input("Masukan berat badan (kg): "))
tinggiBadan = float(input("Masukan tinggi badan (m) : "))
cekBMI(beratBadan, tinggiBadan)
