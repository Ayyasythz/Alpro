jam = int(input("Masukan Jam : "))
menit = int(input("Masukan Menit : "))
durasi = int(input("Durasi Kegiatan (Menit) : "))

tambah_menit = int(menit) + durasi
tambah_jam = tambah_menit / 60

menit = tambah_menit % 60
jam = jam + tambah_jam
jam = jam % 24

print(int(jam), ":",menit)