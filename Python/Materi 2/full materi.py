# Stack sebagai list
stack = []

# Operasi Stack
def push(item):
    stack.append(item)
    print(f"{item} telah ditambahkan ke stack.")

def pop():
    if not stack:
        print("Stack kosong. Tidak bisa melakukan pop.")
    else:
        removed = stack.pop()
        print(f"{removed} telah dihapus dari stack.")

def peek():
    if not stack:
        print("Stack kosong. Tidak ada item untuk dilihat.")
    else:
        print(f"Item paling atas di stack adalah: {stack[-1]}")

def tampilkan_stack():
    if not stack:
        print("Stack kosong.")
    else:
        print("Isi stack saat ini:", stack)

# Menu Interaktif
while True:
    print("\nMenu Stack:")
    print("1. Push (Tambah data)")
    print("2. Pop (Ambil data)")
    print("3. Peek (Lihat paling atas)")
    print("4. Tampilkan Stack")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        data = input("Masukkan data yang ingin ditambahkan: ")
        push(data)
    elif pilihan == "2":
        pop()
    elif pilihan == "3":
        peek()
    elif pilihan == "4":
        tampilkan_stack()
    elif pilihan == "5":
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")    


# ----- STOP!!! KELAS B UJIANNYA INI -----
# Antrian sebagai list
queue = []

# Fungsi operasi queue
def enqueue(item):
    queue.append(item)
    print(f"{item} telah ditambahkan ke antrian.")

def dequeue():
    if not queue:
        print("Antrian kosong. Tidak bisa menghapus.")
    else:
        removed = queue.pop(0)
        print(f"{removed} telah dihapus dari antrian.")

def peek():
    if not queue:
        print("Antrian kosong.")
    else:
        print(f"Item paling depan di antrian: {queue[0]}")

def tampilkan_antrian():
    if not queue:
        print("Antrian kosong.")
    else:
        print("Isi antrian saat ini:", queue)

# Menu Interaktif
while True:
    print("\nMenu Antrian:")
    print("1. Enqueue (Tambah data)")
    print("2. Dequeue (Ambil data)")
    print("3. Peek (Lihat paling depan)")
    print("4. Tampilkan Antrian")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        data = input("Masukkan data yang ingin ditambahkan ke antrian: ")
        enqueue(data)
    elif pilihan == "2":
        dequeue()
    elif pilihan == "3":
        peek()
    elif pilihan == "4":
        tampilkan_antrian()
    elif pilihan == "5":
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        
# ----- SAMPAI SINI ------


# Struktur graph menggunakan dictionary
graph = {}

def tambah_teman(nama1, nama2):
    if nama1 not in graph:
        graph[nama1] = []
    if nama2 not in graph:
        graph[nama2] = []
    
    # Tambahkan teman dua arah
    if nama2 not in graph[nama1]:
        graph[nama1].append(nama2)
    if nama1 not in graph[nama2]:
        graph[nama2].append(nama1)
    
    print(f"{nama1} dan {nama2} sekarang berteman.")

def lihat_teman(nama):
    if nama not in graph:
        print(f"{nama} belum memiliki teman.")
    else:
        teman = graph[nama]
        print(f"Teman-teman {nama}: {', '.join(teman)}")

def tampilkan_graph():
    if not graph:
        print("Belum ada pertemanan yang tercatat.")
    else:
        print("Daftar pertemanan:")
        for orang, teman in graph.items():
            print(f"{orang}: {', '.join(teman)}")

# Menu interaktif
while True:
    print("\nMenu Pertemanan:")
    print("1. Tambah Pertemanan")
    print("2. Lihat Teman Seseorang")
    print("3. Tampilkan Semua Pertemanan")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        nama1 = input("Masukkan nama orang pertama: ")
        nama2 = input("Masukkan nama orang kedua: ")
        tambah_teman(nama1, nama2)
    elif pilihan == "2":
        nama = input("Masukkan nama yang ingin dilihat temannya: ")
        lihat_teman(nama)
    elif pilihan == "3":
        tampilkan_graph()
    elif pilihan == "4":
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        
# Struktur data family tree
family_tree = {}

# Tambah hubungan orang tua-anak
def tambah_keluarga(anak, orang_tua):
    if anak not in family_tree:
        family_tree[anak] = {"orang_tua": [], "anak": []}
    if orang_tua not in family_tree:
        family_tree[orang_tua] = {"orang_tua": [], "anak": []}
    
    if orang_tua not in family_tree[anak]["orang_tua"]:
        family_tree[anak]["orang_tua"].append(orang_tua)
        family_tree[orang_tua]["anak"].append(anak)
    
    print(f"Hubungan ditambahkan: {orang_tua} adalah orang tua dari {anak}.")

def tampilkan_orang_tua(nama):
    if nama in family_tree and family_tree[nama]["orang_tua"]:
        print(f"Orang tua dari {nama}: {', '.join(family_tree[nama]['orang_tua'])}")
    else:
        print(f"Tidak ada data orang tua untuk {nama}.")

def tampilkan_anak(nama):
    if nama in family_tree and family_tree[nama]["anak"]:
        print(f"Anak-anak dari {nama}: {', '.join(family_tree[nama]['anak'])}")
    else:
        print(f"Tidak ada data anak untuk {nama}.")

def tampilkan_semua():
    if not family_tree:
        print("Belum ada data keluarga.")
    else:
        print("Struktur Family Tree:")
        for nama, data in family_tree.items():
            ortu = ', '.join(data['orang_tua']) if data['orang_tua'] else 'Tidak ada'
            anak = ', '.join(data['anak']) if data['anak'] else 'Tidak ada'
            print(f"{nama} -> Orang tua: {ortu} | Anak: {anak}")

# Menu Interaktif
while True:
    print("\nMenu Family Tree:")
    print("1. Tambah Hubungan (Orang Tua - Anak)")
    print("2. Lihat Orang Tua")
    print("3. Lihat Anak")
    print("4. Tampilkan Semua Data")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        anak = input("Masukkan nama anak: ")
        ortu = input("Masukkan nama orang tua: ")
        tambah_keluarga(anak, ortu)
    elif pilihan == "2":
        nama = input("Masukkan nama yang ingin dilihat orang tuanya: ")
        tampilkan_orang_tua(nama)
    elif pilihan == "3":
        nama = input("Masukkan nama yang ingin dilihat anaknya: ")
        tampilkan_anak(nama)
    elif pilihan == "4":
        tampilkan_semua()
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
        
# Fungsi rekursif merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Basis rekursi: array berisi 1 atau 0 elemen sudah urut

    # Bagi array menjadi dua bagian
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# Fungsi untuk menggabungkan dua array terurut
def merge(left, right):
    result = []
    i = j = 0

    # Bandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Tambahkan sisa elemen (jika ada)
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- INTERAKSI DENGAN PENGGUNA ---

# Minta jumlah data
n = int(input("Masukkan jumlah elemen yang ingin diurutkan: "))

# Minta data elemen satu per satu
data = []
print("Masukkan", n, "angka (dipisah dengan Enter):")
for i in range(n):
    angka = int(input(f"Elemen ke-{i+1}: "))
    data.append(angka)

# Proses pengurutan
hasil = merge_sort(data)

# Tampilkan hasil
print("\nData sebelum diurutkan :", data)
print("Data setelah diurutkan :", hasil)

# Fungsi rekursif untuk binary search
def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Data tidak ditemukan

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)  # Cari di sebelah kiri
    else:
        return binary_search(arr, target, mid + 1, high)  # Cari di sebelah kanan

# ================================
# ✨ Bagian Utama Program
# ================================

print("Program Binary Search Rekursif")
try:
    angka_input = input("Masukkan daftar angka (terurut, pisahkan dengan spasi): ")
    data = list(map(int, angka_input.split()))

    if data != sorted(data):
        print("❌ Data harus sudah terurut. Silakan urutkan terlebih dahulu.")
    else:
        cari = int(input("Masukkan angka yang ingin dicari: "))

        # Proses pencarian
        hasil = binary_search(data, cari, 0, len(data) - 1)

        # Tampilkan hasil
        if hasil != -1:
            print(f"✅ Angka {cari} ditemukan pada indeks ke-{hasil}")
        else:
            print(f"❌ Angka {cari} tidak ditemukan dalam data.")

except ValueError:
    print("❌ Input tidak valid! Harap masukkan angka saja.")
