# definisi list
mobil = ["suzuki", "mitsubishi", "honda", "toyota"]
print(mobil)

# 2 cara membuat list
# 1. Dengan kurung siku langsung
a = [4, 5, 6]
print(a)

# 2. Dengan fungsi list() dari tuple
b = list((1, 2, 3))
print(b)

# mengambil elemen dari list
a = [1, 2, 3, 4, 5, 6]
b = a[4]  # ambil elemen ke-5 (karena indeks mulai dari 0)
print(b)

# fungsi dan operasi pada list

# 1. "len" = menghitung panjang/jumlah elemen dalam list
d = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
print(len(d))  # hasilnya 20 karena ada 20 elemen

# 2. "count" = menghitung berapa kali suatu nilai muncul dalam list
e = list(("Jihad", 4, 5, "Anugrah", "Jihad", 10, 12, 15, "Ridho", 45, "Jihad"))
print(e.count("Jihad"))  # menghitung berapa kali kata "Jihad" muncul

# 3. "sort" = mengurutkan elemen list

# a) Urut dari kecil ke besar (ascending)
angka = list((12, 18, 90, 1, 56, 78, 0, -3, -70, -1000))
angka.sort()
print(angka)

# b) Urut dari besar ke kecil (descending)
angka.sort(reverse=True)
print(angka)

# 4. "append" = menambahkan elemen baru ke akhir list
f = ["Anugrah", "Jihad", "Nur"]
f.append("Ridho")  # menambahkan "Ridho" ke akhir list
print(f)

# 5. "pop" = menghapus elemen terakhir dari list
g = ["Anugrah", "Jihad", "Nur", "Ridho", "Ilahi"]
g.pop()  # menghapus "Ilahi"
print(g)

# mengambil sebagian isi list (slice)
h = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11]

i = h[1:3]   # ambil elemen dari indeks 1 sampai sebelum 3 → [2, 3]
j = h[1:]    # ambil dari indeks 1 sampai akhir → [2, 3, ..., 11]
k = h[1]     # ambil elemen indeks ke-1 saja → 2
l = h[:3]    # ambil elemen dari awal sampai sebelum indeks 3 → [1, 2, 3]

print(i)
print(j)
print(k)
print(l)