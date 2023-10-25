kendaraan = ['Sepeda motor', 'Vario', '125cc', 'merah', 'roda 2']
print(kendaraan)

kendaraan = ['Sepeda motor', 'Vario', '125cc', 'merah', 'roda 2']
kendaraan.append ('20 juta rupiah')
print(kendaraan)

kendaraan = ['Sepeda motor', 'Vario', '125cc', 'merah', 'roda 2']
kendaraan.append ('20 juta rupiah')
kendaraan.append('matic')
print(kendaraan)

kendaraan = ['Sepeda motor', 'Vario', '125cc', 'merah', 'roda 2']
kendaraan.append ('20 juta rupiah')
kendaraan.append('matic')
kendaraan.insert(2,'honda')
print(kendaraan)

print ('''Selamat datang, silahkan masukan pilihan:
1. Menghitung luas persegi
2. Menghitung luas lingkaran
3. Menghitung luas segitiga
''')

pilihan = int(input ('masukan pilihan'))

match pilihan:
    case 1:
        print('1 untuk menghitung luas persegi')
        sisi = int(input('masukan sisi persegi'))
        LPersegi = sisi * sisi
        print ('Luas persegi dengan sisi', sisi, 'yaitu', LPersegi)
    case 2:
        print('2 untuk menghitung luas lingkaran')
        r = float(input('masukan jari - jari lingkaran'))
        LLingkaran = 3.14 * r * r
        print ('Luas lingkaran dengan jari - jari', r, 'yaitu', int(LLingkaran))
    case 3:
        print('3 untuk menghitung luas segitiga')
        alas = int(input('masukan alas segitiga'))
        tinggi = int(input('masukan tinggi segitiga'))
        LSegitiga = 1/2 * alas * tinggi
        print ('Luas segitiga yaitu', LSegitiga)
    case _:
        print('salah memilih pilihan')
