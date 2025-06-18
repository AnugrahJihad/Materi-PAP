# Stack untuk menyimpan teks
teks_stack = []

print("Editor Teks Sederhana")
print("Menu:")
print("1. Ketik")
print("2. Undo")
print("3. Lihat")
print("4. Selesai")

while True:
    pilihan = input("\nPilih menu (1-4): ")

    if pilihan == "1":
        teks = input("Tulis teks: ")
        teks_stack.append(teks)
        print("Teks ditambahkan.")
    
    elif pilihan == "2":
        if teks_stack:
            undo_teks = teks_stack.pop()
            print(f"'{undo_teks}' dihapus (undo).")
        else:
            print("Tidak ada teks untuk di-undo.")
    
    elif pilihan == "3":
        if teks_stack:
            print("\nTeks saat ini:")
            for baris in teks_stack:
                print(baris)
        else:
            print("Belum ada teks.")
    
    elif pilihan == "4":
        print("Terima kasih. Program selesai.")
        break
    
    else:
        print("Pilihan tidak valid.")
