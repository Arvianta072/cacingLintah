
import random
import os
import datetime as dt
import string

dict_template = {
    'nama':'nama',
    'jenis':'jenis',
    'harga':000000,
    'exp':dt.datetime(1111,11,11),
}

data_produk = {}

while True:
    os.system('cls')
    print(f"{'\nData Produk':^20}")
    print('='*20)

    produk = data_produk.fromkeys(dict_template.keys())

    produk['nama'] = input("Nama Produk: ")
    produk['jenis'] = input("Jenis Produk: ")
    produk['harga'] = int(input("Harga Produk: "))
    
    TAHUN = int(input("Tahun Exp: "))
    BULAN = int(input("Bulan Exp: "))
    TANGGAL = int(input("Tanggal Exp: "))
    produk['exp'] = dt.datetime(TAHUN,BULAN,TANGGAL)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(5)))
    data_produk.update({KEY:produk})

    print(f"{'\nIndex':<7} {'Nama Produk':<20} {'Jenis Produk':<15} {'Harga Produk':<17} {'EXP':<4}")
    print("="*80)
    for produk in data_produk:
        KEY = produk
        
        NAMA = data_produk[KEY]['nama']
        JENIS = data_produk[KEY]['jenis']
        HARGA = data_produk[KEY]['harga']
        EXP = data_produk[KEY]['exp'].strftime('%x')

        print(f"{KEY:<7} {NAMA:<20} {JENIS:<15} {HARGA:<17,} {EXP:<4}")

    islanjut = input("\nApakah lanjut?(y/n)").lower()
    if islanjut == 'n':
        break

print("Sampai Jumpa")












