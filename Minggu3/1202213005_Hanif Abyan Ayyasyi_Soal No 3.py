usernameRIL = "C117"
passwordRIL = "HotelWisataLembang"
username = str(input("Masukan Username : "))
password = str(input("Masukan Password : "))

if username == usernameRIL and password == passwordRIL:
    print("Selamat Datang ! Anda Telah Berhasil Login")
elif username == usernameRIL and password != passwordRIL:
    print("Password Salah")
elif username != usernameRIL and password == passwordRIL:
    print("Username Salah")
else:
    print("Username and Password Salah")
