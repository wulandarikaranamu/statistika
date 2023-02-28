#mean
data = [0,0,1,2,2,2,4]
n = len(data)
jumlahData = 0

for i in data :
    jumlahData += i
    
print("Jumlah Data : ",jumlahData)
print("panjang data :", n)
mean = jumlahData / n
print("Mean :", mean)

print("------------------------")

#median
if n %2 == 0:
    pass
else :
    u = (n +1)/2
    angkaMedian = data[int(u)]
print("nilai median berada pada data ke-",{u})

print("nilai tengahnya adalah : ",angkaMedian)

print("--------------------------")

#modus
# list input
data = [0,0,1,2,2,2,4]

# inisialisasi variabel
n = None
jumlahData = 0

# hitung kemunculan setiap nilai
for i in data:
    count = data.count(i)
    # update variabel modus jika kemunculan lebih besar dari yang sebelumnya
    if count > jumlahData:
        n = i
        jumlahData = count

# cetak hasil
print("Modus dari data adalah:", n)