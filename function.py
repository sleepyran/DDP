print("Nomor 1.")
def profil(nama, alamat, gender, umur, hobi):
    print("Nama saya adalah", nama)
    print("Saya berdomisili", alamat)
    print("Saya adalah seorang", gender)
    print("Saya berusia", umur)
    print("Hobi saya adalah", hobi)

profil("Aulia Maharani", "Bogor", "Perempuan", "19tahun", "Bermain alat musik tradisional")
print( )
print("Nomor 2.")
def nilaikelulusan(nilai):
    if(nilai < 60):
        print("Gagal")
    elif(nilai >=61 and nilai <=70):
        print("Baik")
    elif(nilai >=71 and nilai <=80):
        print("Sangat baik")
    elif(nilai >= 81 and nilai <=100):
        print("Istemewa")
    else:
        print("Nilai tidak ada")

nilaikelulusan(68)
print( )
print("Nomor 3.")
def bilangan (ganjil):
    for i in range (ganjil):
        if (i%2 !=0):
            print(i, end = " ")
bilangan(100)