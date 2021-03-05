print('tipe data skalar ==}> tipe data sederhana')
anak1 = 'uno'
anak2 = 'dos'
anak3 = 'tress'
anak4 = 'quatro'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data daftar/list/array')
anak = ['uno', 'dos', 'tress', 'quatro']
print(anak)
anak.append('sinco')
print(anak)

print('\nmenyapa anak ketiga')
print(f'hai {anak[2]}')

print('\nmenyapa semua anak')
for a in anak:
    print(f'hai {a}!')

print('\nsapa semua anak: cara ribet')
for a in range (0, len(anak)):
    print(f'{a+1}. hai {anak [a]}')