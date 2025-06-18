class Person:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print("  " * level + self.name)
        for child in self.children:
            child.display(level + 1)

# Contoh penggunaan:
# root = Person("Kakek")
# ayah = Person("Ayah")
# anak = Person("Anak")
# root.add_child(ayah)
# ayah.add_child(anak)
# root.display()
