# while loop
a = 1               # Menyimpan nilai angka ke dalam variabel a
while a < 6:        # Selama nilai a kurang dari 6, lakukan perulangan
    print(a)        # Menampilkan nilai
    a += 2          # Menambahkan nilai a dengan angka 2 (a = a + 2)
                    # output = 1, 3, 5. karena 1 + 2 = 3; 3 + 2 = 5, lalu 5 < 6, tetapi 5 + 2 = 7 > 6 → berhenti

print("")

# while break
b = 1               # Inisialisasi variabel b dengan nilai 1
while b < 10:       # Perulangan akan terus berjalan selama nilai b kurang dari 10
    print(b)        # Menampilkan nilai b ke layar
    if b == 5:      # Jika b sama dengan 5, maka:
        break       # Keluar dari perulangan (loop berhenti)
    b += 1          # Jika belum break, tambahkan nilai b dengan 1 (b = b + 1)
                    # output = 1, 2, 3, 4, 5. karena perulangan berhenti setelah mencetak 5
                    
print("")

# while continue
c = 0               # Inisialisasi variabel c dengan nilai 0
while c < 10:       # Perulangan akan berjalan selama nilai c kurang dari 10
    c += 1          # Tambahkan 1 ke dalam c (c = c + 1)
    if c == 5:      # Jika c bernilai 5, maka:
        continue    # Lewati proses di bawah (yaitu print), dan lanjut ke iterasi berikutnya
    print(c)        # Menampilkan nilai c ke layar, kecuali saat c == 5
                    # output = 1, 2, 3, 4, 6, 7, 8, 9, 10
                    # karena saat c == 5, perintah print dilewati oleh continue