# Antrian (Queue) menggunakan list
queue = []

# Enqueue (tambah ke belakang)
def enqueue(item):
    queue.append(item)

# Dequeue (ambil dari depan)
def dequeue():
    if not is_empty():
        return queue.pop(0)
    return None

# Cek apakah antrian kosong
def is_empty():
    return len(queue) == 0

# Cek isi antrian
def display_queue():
    print("Queue:", queue)
