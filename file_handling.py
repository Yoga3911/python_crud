import json, os, csv

os.system('clear')

f_name = 'data.json'

# === Membuka File ===

# open <> with open
# write, read, readline/s & close
# w = write (menulis ulang file yang dibuka)
# a = append (menambah)
# r = read (membaca)
# readline = menampilkan 1 line dari file yang dibuka
# readlines = menampilkan seluruh text yang ada pada file
# berupa list

# data = open(f_name, 'rw')
# data.write('selamat malam')
# print(data.readlines())
# data.close()
# print(data.readline())

# with open(f_name, 'r') as data:
#     reader = data.readlines()
#     print(reader)

# === JSON ===
# dump <> dumps
# dump = menuliskan data ke dalam file json
# dumps = menampilkan data berupa string dari json object
# load = membaca data berupa json object
# loads = membaca data berupa string

# load <> loads
# nama = [
#     {"nama":"ahmad"},
#     {"nama":"budi"},
# ]
# tmp, tampungan = [], {}
# with open(f_name, 'r') as data:
#     reader = json.load(data)
#     tmp = reader

# nama = input('Masukkan nama: ')
# tampungan['nama'] = nama
# tmp.append(tampungan)
# tmp.pop(0)
# print(tmp)

# with open(f_name, 'w') as data:
#     writer = json.dump(tmp, data, indent=4, sort_keys=True)

        
# print(reader)
# print(json.loads(reader))
# print(type(reader))



# === CSV ===
# writer & reader

# with open(f_name, 'a') as data:
#     writer = csv.writer(data, delimiter=',')

#     writer.writerow(['selamat malam', 'apel'])


# with open(f_name, 'r') as data:
#     reader = csv.reader(data)
#     for i in reader:
#         print(i[0], i[1])


# DictWriter, DictReader, Writeheader & Writerow/s
# with open(f_name, 'a') as data:
#     field = ['nama', 'umur', 'jenis_kelamin']
#     writer = csv.DictWriter(data, fieldnames=field)

    # # writer.writeheader()
    # writer.writerow({'nama':'rani', 'umur':24, 'jenis_kelamin':'P'})

# with open(f_name, 'r') as data:
    # field = ['nama', 'umur', 'jenis_kelamin']
    # reader = csv.DictReader(data)
    # for i in reader:
    #     print(i['umur'])

# Try, Except, Finally
# try:
#     with open('data.json', 'r') as data:
#         reader = json.load(data)
# except:
#     print('File tidak ada')
# finally:
#     print('Program selesai')
# try:
#     x = input('Masukkan nilai: ')
#     if x > 0:
#         print('halo dunia')
# except:
#     print('Tipe data tidak sesuai')
# print('Selesai')
