#manajemen kontak

def melihat_kontak():
    # Melihat semua kontak
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'{num}. {item["nama"]} ({item["hp"]}, {item["email"]})')
    else:
        print('Kontak maih kosong!')
        return 1
def menambah_kontak():
    # Menambah kontak
    nama = input('Masukkan Nama kontak baru : ')
    hp = input('Masukkan HP kontak baru : ')
    email = input('Masukkan Email KOntak baru : ')
    kontakbaru = {'nama': nama, 'hp': hp, 'email': email}
    kontak.append(kontakbaru)
    print('Kontak Berhasil Ditambahkan!')

def menghapus_kontak():
    if melihat_kontak() == 1:
        return
    else:
        i_hapus = int(input('masukkan no kontak yang ingin dihapus: '))
        del kontak[i_hapus - 1]
        print('Kontak Berhasil dihapus!')

kontak1 = {'nama':'Ahmad','hp' : '082246936269', 'email' : 'ahmad@gmail.com'}
kontak2 = {'nama':'Novan','hp' : '085280081076', 'email' : 'Novan@gmail.com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Manajemen Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambah Kontak")
    print("3. Menghapus Kontak")
    print("4. Keluar")

    pilihan = input("Masukkan Pilihan menu (1, 2, 3, atau 4) : ")
    print('')
    if pilihan == '1':
        melihat_kontak()
    elif pilihan == '2':
        menambah_kontak()
    elif pilihan == '3':
        #Menghapus kontak
        menghapus_kontak()

    elif pilihan == '4':
        #Keluar
        break
    else:
        print("Anda memasukkan pilihan yang salah")

