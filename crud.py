import json, os, csv

os.system('clear')

f_name = 'data.json'

def clear():
    os.system('cls')

def menu():
    clear()
    print('''=== Mahasiswa Unej ===    
1. Tambah data mahasiswa
2. Lihat data mahasiswa
3. Update data mahasiswa
4. Hapus data mahasiswa
5. Exit
''')
    tanya = input('Pilih menu: ')
    if tanya == '1':
        create()
    elif tanya == '2':
        read()
    elif tanya == '3':
        update()
    elif tanya == '4':
        delete()
    elif tanya == '5':
        exit()

def create():
    clear()
    print('=== Tambah Mahasiswa ===')
    tmp, mhs = [], {}

    try:
        with open(f_name, 'r') as data:
            reader = json.load(data)
            tmp = reader
    except:
        pass

    mhs['nama'] = input('Masukkan nama: ')
    mhs['nim'] = input('Masukkan nim: ')
    tmp.append(mhs)

    with open(f_name, 'w') as data:
        writer = json.dump(tmp, data, indent=4)

    input('Enter untuk kembali')

def read():
    clear()
    print('=== Data Mahasiswa ===')

    try:
        with open(f_name, 'r') as data:
            reader = json.load(data)
    except:
        print('File tidak ada')
        input('Enter untuk kembali')
        menu()

    print('='*35)
    print(f"{'No.':^3} {'Nama':^15} {'NIM':^12}")
    print('='*35)
    for index, i in enumerate(reader, start=1):
        print(f"{index:^3} {i['nama']:^15} {i['nim']:^12}")
    print('='*35)
    input('Enter untuk kembali')

def delete():
    clear()
    print('=== Hapus Mahasiswa ===')

    try:
        with open(f_name, 'r') as data:
            reader = json.load(data)
    except:
        print('File tidak ada')
        input('Enter untuk kembali')
        menu()
    
    print('='*35)
    print(f"{'No.':^3} {'Nama':^15} {'NIM':^12}")
    print('='*35)
    for index, i in enumerate(reader, start=1):
        print(f"{index:^3} {i['nama']:^15} {i['nim']:^12}")
    print('='*35)
    
    tanya = int(input('Index mahasiswa: '))
    for index, i in enumerate(reader, start=1):
        if index == tanya:
            yakin = input('apakah anda yakin: [y/n] ')
            if yakin == 'y':
                reader.pop(index - 1)
                with open(f_name, 'w') as data:
                    writer = json.dump(reader, data, indent=4)
    input('Enter untuk kembali')

def update():
    clear()
    print('=== Update Data ===')

    try:
        with open(f_name, 'r') as data:
            reader = json.load(data)
    except:
        print('File tidak ada')
        input('Enter untuk kembali')
        menu()
    
    print('='*35)
    print(f"{'No.':^3} {'Nama':^15} {'NIM':^12}")
    print('='*35)
    for index, i in enumerate(reader, start=1):
        print(f"{index:^3} {i['nama']:^15} {i['nim']:^12}")
    print('='*35)

    tmp = []
    tanya = input('No mahasiswa: ')
    for index, i in enumerate(reader, start=1):
        if int(tanya) == index:
            tmp = i
            ind = index

    while True:
        clear()
        print('='*35)
        print(f"{'Nama':^15} {'NIM':^12}")
        print('='*35)
        for i in tmp.values():
            print(f"{i:^15}", end='')
        print()
        print('='*35)
        print('1. Nama\n2. NIM\n0. Simpan')
        ubah = input('Data yang ingin diubah: ')
        if ubah == '1':
            tmp['nama'] = input('Masukkan nama: ')
        elif ubah == '2':
            tmp['nim'] = input('Masukkan nim: ')
        elif ubah == '0':
            break
    yakin = input('apakah anda yakin? [y/n] ')
    if yakin == 'y':
        clear()
        print('Data berhasil diubah')
        reader[ind - 1] = tmp
        with open(f_name, 'w') as data:
            writer = json.dump(reader, data, indent=4)
    input('Enter untuk kembali')

while True:
    menu()
