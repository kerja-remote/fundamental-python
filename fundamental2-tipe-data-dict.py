"""
tipe data dictionary sekedar menghubungkan antara key dan value
KVP = Key Value Pair
dictionary = kamus
"""

kamus_ind_eng = {'anak': 'son', 'istri': 'wifi', 'suami': 'husband', 'ibu': 'mother', 'ayah': 'father'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['istri'])

print('\ndata ini dikirimkan oleh server gojek untuk memberikan info driver disekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2021-03-03',
    'driver_list': [
        {'nama': 'uno', 'jarak': 10},
        {'nama': 'dos', 'jarak': 30},
        {'nama': 'tress', 'jarak': 50},
        {'nama': 'quatro', 'jarak': 150}
    ]
}
print(data_dari_server_gojek)
print(f"\nDriver disekitar anda {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"driver terdekat bernama {data_dari_server_gojek['driver_list'][0]['nama']} berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")