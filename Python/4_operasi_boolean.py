# Boolean operator
# boolean ini sebenarnya sama kayak operator matematika, cuma kalau operator matematika itu untuk menghasilkan angka sedangkan untuk operator boolean untuk menghasilkan nilai true atau false

# Operator not
# contoh jika "a=true" maka "not a=false", jika "a=false" maka "not a=true"

# Operator and
# contoh:
# "a=true" "b=true" maka "a and b=true"
# "a=false" "b=true" maka "a and b=false"
# "a=true" "b=false" maka "a and b=false"
# "a=false" "b=false" maka "a and b=false"
# Catatan: jika salah satu variable bernilai false maka nanti hasil gabungan and 2 variable akan bernilai false

# Operator or
# contoh:
# "a=true" "b=true" maka "a or b=true"
# "a=false" "b=true" maka "a or b=true"
# "a=true" "b=false" maka "a or b=true"
# "a=false" "b=false" maka "a or b=false"
# Catatan: jika salah satu variable bernilai true maka nanti hasil gabungan and 2 variable akan bernilai true

# Operator Equality
# Digunakan untuk mengecek apakah nilai tersbut itu sama
# Equality menggunakan "= =" atau "==" sama dengan dan "! =" atau "!=" tidak sama dengan
# outputnya akan bernilai true atau false tergantung dari hasilnya
# contoh 1
x = 5
y = 5
print(x==y) # output akan bernilai true karena 5 sama dengan 5

# contoh 2
x = 5
y = 5
print(x!=y) # output akan bernilai false karena seharusnya 5 sama dengan 5

# contoh 3
x = 5
y = 4
print(x==y) # output bernilai false karena seharusnya 5 tidak sama dengan 4

# contoh 4
x = 5
y = 4
print(x!=y) # output bernilai true karena 5 tidak sama denga 4

# contoh 5, jika variablenya adalah integer dan string
x = 5
y = "5"
print(x==y) # false, karena 5 adalah integer dan "5" adalah string maka seharusnya 5 tidak sama dengan "5"

# contoh 6, jika variablenya adalah integer dan string
x = 5
y = "5"
print(x!=y) # true, karena 5 yang integer tidak sama dengan "5" yang string


# Relational operator
# Isinya adalah <; <=(< =); >; >=(> =)
# contoh 7
x = 4
y = 5
print(x > y) # false, karena seharusnya 4 < 5

# contoh 8
x = 4
y = 5
print (x <= y) # true, karena memang 4 <= 5

# contoh 9
x = 4
y = 5
z = 6
print (x >= y and z > y) # false, karena seharusnya 4 <= 5, tapi yang belakang sudah tepat 6 > 5