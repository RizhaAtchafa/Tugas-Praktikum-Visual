abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

key = int(input('Masukkan Berapa angka pengacak: '))
def encode(jua,chiper_key):
    jua = jua.lower()
    hasil_encode = ''
    for usa in jua :
        if usa in abjad :
            index_lama = abjad.index(usa)
            index_baru = (index_lama + chiper_key) % len(abjad)
            abjad_baru = abjad[index_baru]
            hasil_encode = hasil_encode + abjad_baru
    else:
                hasil_encode = hasil_encode + ''
                return hasil_encode


jua = input('Masukkan Kalimat yang ingin di acak :')
jua_hasil = encode(jua,key) 
print('Hasil Pengacakan adalah',jua_hasil)

  