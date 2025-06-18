# Bagian 1: Pengenalan python

# Contoh error konversi tipe
# a = float("10.8")
# b = int("10,5")  # Salah: Python tidak menerima koma (harus titik)
# print(a + b)     
# Output: Error karena "10,5" bukan format angka yang valid di Python

# Operasi matematika campuran
a = (2**3) + 5 % 2
print(a)  # Output: 8 + 1 = 9
# Penjelasan: 2**3 = 8, 5 % 2 = 1, lalu 8 + 1 = 9

# ========================

# Bagian 2: Control Structure

# 1. Logika Boolean
a = True
b = False
c = True
d = (a and b) or (not(c) and b) and a
print(d)  # Output: False
# Penjelasan:
# a and b = False
# not(c) = False, False and b = False
# False or False = False

# 2. Perbandingan
a = 25
b = 30
c = 36
d = (a <= b) or (c > b)
print(d)  # Output: True
# Penjelasan: 25 <= 30 = True → langsung True (or cukup satu True)

# 3. If-Else Bertingkat
a = 31
if a < 30:
    if a < 25:
        print("cold")
    else:
        print("warm")
else:
    if a > 35:
        print("very hot")
    else:
        print("hot")
# Output: hot
# Penjelasan: 31 tidak < 30 → masuk ke else, dan 31 tidak > 35 → "hot"

# 4. While + Continue (lewati bilangan genap)
a = 10
i = -1
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
# Output: 1, 3, 5, 7, 9
# Penjelasan: hanya cetak bilangan ganjil

# 5. Nested While (Perulangan bersarang)
i = 0
count = 0
while i < 10:
    j = 0
    while j < 10:
        count += 1
        j += 1
    i += 1
print(count)  # Output: 100
# Penjelasan: 10 x 10 perulangan = 100

# 6. Nested For Loop
count = 0
for i in range(3, 5):         # 2 kali: i = 3 dan i = 4
    for j in range(0, 10):    # 10 kali untuk tiap i
        count += 1
print(count)  # Output: 20
# Penjelasan: 2 x 10 = 20

# 7. For + Break
con = 5
b = 20
for a in range(0, b):
    if a - con == -3:
        break
    print(a)
# Output: 0, 1
# Penjelasan: a - 5 == -3 → a == 2 → break saat a == 2

# ========================

# Bagian 3: Compound Stucture Data Type

# 1. Penjumlahan List
a = [0, 1, 2]
b = [2, 1, 0]
c = a + b
print(c)  # Output: [0, 1, 2, 2, 1, 0]
# Penjelasan: list bisa dijumlahkan langsung → elemen digabung

# 2. While + Append + Continue
i = 0
a = []
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    a.append(i)
print(a)  # Output: [1, 2, 4, 5, 7, 8, 10]
# Penjelasan: angka kelipatan 3 dilewati (3, 6, 9)

# 3. Slicing String
s = "halo halo jakarta"
print(s[:7])  # Output: halo ha
# Penjelasan: ambil karakter dari indeks 0 sampai sebelum 7