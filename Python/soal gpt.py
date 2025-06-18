celcius = float(input("Masukkan suhu dalam Celcius: "))
fahrenheit = (celcius * 9/5) + 32
print(f"Suhu dalam Fahrenheit: {fahrenheit}")

ganjil = int(input("Masukkan bilangan bulat: "))
if ganjil % 2 != 0:
    print(f"{ganjil} adalah bilangan ganjil.")
else:
    print(f"{ganjil} adalah bilangan genap.")

lebar = int(input("Masukkan lebar persegi panjang: "))
panjang = int(input("Masukkan panjang persegi panjang: "))
luas = lebar * panjang
keliling = 2 * (lebar + panjang)
print(f"Luas persegi panjang: {luas}")
print(f"Keliling persegi panjang: {keliling}")

