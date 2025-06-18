# Definisi String
# Ingat bahwa string adalah seperti array (seperti list), dan penulisan 'hello' atau "hello" itu sama saja
a = "Hello World!"
print(a)         # mencetak string secara keseluruhan
print(a[1])      # mencetak karakter kedua (indeks 1) → "e"

# Operasi pada String

# 1. Slicing (memotong bagian dari string)
b = "Hello World!"  # ya, spasi juga dihitung sebagai karakter dalam string
print(b[1:5])       # ambil karakter dari indeks 1 sampai sebelum 5 → "ello"

# 2. Ubah huruf ke kecil dan besar
c = "Anugrah Jihad NR"
print(c.lower())    # mengubah semua huruf menjadi huruf kecil → "anugrah jihad nr"
print(c.upper())    # mengubah semua huruf menjadi huruf besar → "ANUGRAH JIHAD NR"

# 3. Menggabungkan (concat) string
w = "Anugrah"
x = "Jihad"
y = "Nur"
z = "Ridho"
d = w + x + y + z    # menggabungkan semua string tanpa spasi
print(d)             # hasil: "AnugrahJihadNurRidho"

# 4. Mengecek apakah sebuah kata/substring ada dalam string
e = "Anugrah Jihad Nur Ridho adalah seorang mahasiswa Informatika di UIN Sunan Kalijaga"
print("Sunan" in e)  # hasilnya True karena kata "Sunan" ada dalam string e

# Tambahan: Mengecek apakah dua kata yang berjauhan ada dalam string
print("Jihad" in e and "Kalijaga" in e)  # True jika keduanya ada dalam string
