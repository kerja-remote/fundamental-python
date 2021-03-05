#konstruksi dasar python
#sequential
print('Hello World!')
print('by Bagus')
print('-'*10)

# percabangan: Eksekusi terpilih
ingin_cepat = False
if ingin_cepat:
    print('jalan lurus')
else:
    print('jalan lain')

# perulangan
jumlah_anak = 4

for index_anak in range (1, jumlah_anak+1): #jumlah perulangan = 5 - 1 =4
    print(f'halo anak #{index_anak}')
