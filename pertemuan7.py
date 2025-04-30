# Buat nested dictionary
nilaimhs = {
    'mhs1': {
        'nama': 'budi',
        'nim': 86
    },
    'mhs2': {
        'nama': 'sari',
        'nim': 92
    },
    'mhs3': {
        'nama': 'andi',
        'nim': 75
    }
}

# Tampilkan seluruh nested dictionary
print(nilaimhs)
print('---------------------')

# Tampilkan data mhs2
print('mhs2:', nilaimhs['mhs2'])
print('---------------------')

# Tampilkan nama mhs2
print('Nama mhs2:', nilaimhs['mhs2']['nama'])
print('---------------------')

# FUNCTION
def hitung(p, l):
    luas = p * l
    return luas

print('Luas tanah (function)   :', hitung(5, 4))

# LAMBDA
# cara 1 : use variabel
luas = lambda p, l: p * l
print('Luas tanah (lambda 1)   :', luas(5, 4))

# cara 2 : directly
print('Luas tanah (lambda 2)   :', (lambda p, l: p * l)(5, 4))
