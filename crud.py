import json, os, csv

f_name = 'data.json'

def clear():
    os.system('clear')

# Main Menu
def menu():
    clear()
    print(
'''     === CRUD ===

1. Tambah Mahasiswa
2. Lihat Data Mahasiswa
3. Perbarui Data Mahasiswa
4. Hapus Data Mahasiswa
5. Exit
'''
    )
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

def load():
    with open(f_name, 'r') as data:
            reader = json.load(data)
            return reader

def dump(tmp):
    with open(f_name, 'w') as data:
        writer = json.dump(tmp, data, indent=4)

# Create
def create():
    clear()
    print('=== Tambah Mahasiswwa ===\n')
    tmp, mhs = [], {}
    try:
        get = load()
        tmp = get
    except:
        pass
    mhs['nama'] = input('Masukkan nama: ')
    mhs['nim'] = input('Masukkan NIM: ')
    tmp.append(mhs)
    dump(tmp)
    input('\nEnter untuk kembali')

# Read
def core():
    get = load()
    print('='*40)
    print(f"{'No':^2} {'Nama':^16} {'NIM':^12}")
    print('='*40)
    for i, item in enumerate(get, start=1):
        print(f"{i:^2} {item['nama']:^15} {item['nim']:^15}")
    print('='*40)

def read():
    clear()
    print('=== Data Mahasiswwa ===\n')
    core()
    input('\nEnter untuk kembali')

# Update
def update():
    clear()
    print('=== Update Data ===\n')
    core()
    get = load()
    tanya_update = input('Mahasiswa yang ingin diupdate: ')
    for index, item in enumerate(get):
        if tanya_update == item['nama']:
            tmp = item
            index_mhs = index
    while True:
        clear()
        print('='*40)
        print(f"{'Nama':^16} {'NIM':^12}")
        print('='*40)
        for item in tmp.values():
            print(f"{item:^15}", end='')
        print()
        print('='*40)
        print('1. Nama\n2. NIM\n0. Selesai')
        tanya = input('Data yang ingin diupdate: ')
        if tanya == '0':
            break
        elif tanya == '1':
            tmp['nama'] = input('Masukkan nama: ')
        elif tanya == '2':
            tmp['nim'] = input('Masukkan nim: ')
    yakin = input('Apakah anda yakin ingin mengubah data ini? [y/n] ')
    if yakin == 'y':
        get[index_mhs] = tmp
        dump(get)
    input('Enter untuk kembali')

# Delete
def delete():
    clear()
    print('=== Hapus Mahasiswwa ===\n')
    core()
    get = load()
    tanya = input('Masukkan nama mahasiswa: ')
    for i, item in enumerate(get):
        if tanya == item['nama']:
            get.pop(i)
    yakin = input('Apakah anda yakin ingin mengubah data ini? [y/n] ')
    if yakin == 'y':
        dump(get)
    input('\nEnter untuk kembali') 

while True:
    menu()
