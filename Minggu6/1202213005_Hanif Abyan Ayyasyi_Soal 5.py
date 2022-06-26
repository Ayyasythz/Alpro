username, pasaword = "telkom", "kampusterbaik"

print("1. Menggunakan While Loop \n2. Menggunakan For Loop")
inputMetode = int(input("Gunakan Metode yang mana ? (1 / 2)"))
print("===================================================")

match inputMetode:
    case 1:
        i = 1
        while i <= 3:
            inputUsername = str(input("Masukan Username : "))
            inputPassword = str(input("Masukan Password : "))
            if inputUsername != username and inputPassword != pasaword:
                print("Username dan Password Salah")
                i += 1
            else:
                print("Welcome, Bos ! Anda berhasil Login")
                break

    case 2:
        for x in range(1, 4):
            inputUsername = str(input("Masukan Username : "))
            inputPassword = str(input("Masukan Password : "))
            if inputUsername != username and inputPassword != pasaword:
                print("Username dan Password Salah")
                continue
            else:
                print("Welcome, Bos ! Anda berhasil Login")
                break
