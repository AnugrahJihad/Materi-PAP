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