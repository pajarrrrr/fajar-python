nilai = int(input:('Masukkan nilai anda:'))
usia = int(input:('Masukkan usia anda:'))

if nilai >= 75:
    if (usia < 15):
        print('Selamat adek, kamu lulus:')
    else:
        print('Selamat kakak, kamu lulus :')
else:
    if (usia < 15):
        print('Mohon maaf adek, kamu tidak lulus:')
    else:
        print('Mohon maaf kakak, kamu tidak lulus :')