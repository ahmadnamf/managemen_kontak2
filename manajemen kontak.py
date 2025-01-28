#manajemen kontak

class kontak:
    def __init__(self):
        self.kontak = []

    def melihat_kontak(self):
        # Melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["hp"]}, {item["email"]})')
        else:
            print('Kontak maih kosong!')
            return 1

    def menambah_kontak(self):
        # Menambah kontak
        nama = input('Masukkan Nama kontak baru : ')
        hp = input('Masukkan HP kontak baru : ')
        email = input('Masukkan Email KOntak baru : ')
        kontakbaru = {'nama': nama, 'hp': hp, 'email': email}
        self.kontak.append(kontakbaru)
        print('Kontak Berhasil Ditambahkan!')

    def menghapus_kontak(self):
        if self.melihat_kontak() == 1:
            return
        else:
            i_hapus = int(input('masukkan no kontak yang ingin dihapus: '))
            del self.kontak[i_hapus - 1]
            print('Kontak Berhasil dihapus!')

kontak_kantor = kontak()
kontak_keluarga = kontak ()

while True:
    print("\nMenu Manajemen Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambah Kontak")
    print("3. Menghapus Kontak")
    print("4. Keluar")

    pilihan = input("Masukkan Pilihan menu (1, 2, 3, atau 4) : ")
    print('')
    if pilihan == '1':
        kontak_kantor.melihat_kontak()
    elif pilihan == '2':
        kontak_kantor.menambah_kontak()
    elif pilihan == '3':
        #Menghapus kontak
        kontak_kantor.menghapus_kontak()

    elif pilihan == '4':
        #Keluar
        break
    else:
        print("Anda memasukkan pilihan yang salah")

