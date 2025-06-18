print("INPUT DAN OUTPUT")
print()

# Bagian Input
print("1. INPUT")
x = int(input("Masukkan angka pertama: "))
y = int(input("Masukkan angka kedua: "))
z = x + y
print(f"Hasil dari {x} + {y} adalah {z}")

print() # ini adlah output blank untuk memberikan jarak

# Bagian Output
print("2. OUTPUT")

# Output biasa (tanpa variabel)
print("Anugrah Jihad Nur Ridho")

# Output menggunakan variabel (contoh 1)
nama = "Jihad"
print("Halo, nama saya {0}, saya adalah seorang {1}.".format(nama, "mahasiswa"))

# Output menggunakan variabel dan f-string (contoh 2)
nama2 = "Ridho"
asal = "Yogyakarta"
umur = 20
print(f"Halo, nama saya {nama2}, saya berasal dari {asal}, umur saya {umur}.")
