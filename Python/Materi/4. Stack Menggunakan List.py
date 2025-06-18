stack = []

# Push (tambah ke atas stack)
def push(item):
    stack.append(item)

# Pop (ambil dari atas stack)
def pop():
    if not is_empty():
        return stack.pop()
    return None

# Cek apakah stack kosong
def is_empty():
    return len(stack) == 0

# Lihat isi stack
def display_stack():
    print("Stack:", stack)
