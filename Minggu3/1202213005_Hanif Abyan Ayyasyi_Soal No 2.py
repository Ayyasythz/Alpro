lups = True
while lups:
    try:
        inputNumber = int(input("Masukan Angka : "))
        if (inputNumber < 0):
            print(inputNumber, "Merupakan Bialngan Negatif")
            lups = False
        else:
            print(inputNumber , "Merupakan Bilangan Positif")
            lups = False

    except ValueError:
        print("Masukan Angka!!")
