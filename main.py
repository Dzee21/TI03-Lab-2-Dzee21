# DDP LAB-2

# SOAL 1 - Mencetak bilangan
# Tuliskan program untuk Soal 1 di bawah ini
for i in range(100,0,-2):
  print(i)
print( )

# SOAL 2 - Menghitung rata-rata
# Tuliskan program untuk Soal 2 di bawah ini

bilangan = eval(input("Masukkan Banyak Bilangan "))
jumlah = 0
for c in range(bilangan):
  b = eval(input("Masukkan Bilagan "))
  jumlah = jumlah + b
print("Hasil rata-rata:", jumlah/bilangan)
print( )
# SOAL 3 - Mencetak persegi
# Tuliskan program untuk Soal 3 di bawah ini

a = int(input("Masukkan Bilangan "))
for x in range(a):
  print("#" * a, sep=' ')



