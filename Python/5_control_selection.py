# contoh if
name = True
if(name):
    print("Anugrah Jihad Nur Ridho") # karena name = True maka akan menampilkan Anugrah Jihad Nur Ridho
#output = Anugrah Jihad Nur Ridho
  
name = False
if(name):
    print("Anugrah Jihad Nur Ridho") # tidak akan menampilkan apapun karena name bernilai False
#output = *kosong*
  
    
# contoh else
name = False
if(name):
    print("Anugrah Jihad Nur Ridho") #jika name = True akan menampilkan "Anugrah Jihad Nur Ridho"
else:
    print("Unknown Person") # jika name = False akan menampilkan "Unknwon Person"
#output = Unknown Person


# contoh elif
name = False
age = True
if(name):
    print("Anugrah Jihad Nur Ridho") # tidak akan ditampilkan karena name = False
elif(age):
    print("20") # akan menampilkan 20 karena age = True
else:
    print("Unknown Person") # tidak akan menampilkan apapun
# output = 20