import random
import string
import os

dict_template = {
    'nama' : 'nama',
    'umur' : 'umur',
    'jenis_kelamin' : 'jenis_kelamin',
    'golongan' : 'golongan',
    'gaji' : 1
}

data_karyawan = {}



def hitung_gaji(gaji_awal,gaji_per_jam):
    gaji = gaji_awal
    gaji_lembur = 1.5 * gaji_per_jam

    jam_kerja = int(input("Berapa jam anda bekerja: "))
    if jam_kerja > 150:
        jam_lembur = jam_kerja - 150
        total_gaji = int((jam_lembur * gaji_lembur) + gaji)
        jam_lembur = jam_kerja - 150
        total_gaji = int((jam_lembur * gaji_lembur) + gaji)

    elif jam_kerja == 150:
        total_gaji = gaji_awal

    return total_gaji

def golongan():
    golongan = input("Masukkan golongan anda: ")

    return golongan

def output(total_gaji):
    print(f"Total Gaji Anda: Rp{total_gaji:,}")

while True:
    os.system('cls')

    print(f"{'Gaji Karyawan':^20}")
    print('='*20)

    karyawan = dict.fromkeys(dict_template.keys())

    karyawan['nama'] = input("Nama: ").upper()
    karyawan['umur'] = input("Umur: ")
    karyawan['jenis_kelamin'] = input("Jenis_Kelamin: ").upper()
    karyawan['golongan'] = input("Golongan: ")
    if karyawan['golongan'] == '1':
        karyawan['gaji'] = hitung_gaji(4000000,100000)
    
    elif karyawan['golongan'] == '2':
        karyawan['gaji'] = hitung_gaji(5000000,150000)
    
    elif karyawan['golongan'] == '3':
        karyawan['gaji'] = hitung_gaji(6000000,200000)

    KEY = ''.join((random.choice(string.ascii_uppercase)for i in range(5)))
    data_karyawan.update({KEY:karyawan})

    print(f"{'\nNo':<7} {'Nama':<20} {'Umur':<4} {'Jenis Kelamin':^19} {'Golongan':^10} {'Gaji':^10}")
    print("="*86)

    for index,karyawan in enumerate(data_karyawan):
        KEY = karyawan

        NAMA = data_karyawan[KEY]['nama']
        UMUR = data_karyawan[KEY]['umur']
        JENIS_KELAMIN = data_karyawan[KEY]['jenis_kelamin']
        GOLONGAN = data_karyawan[KEY]['golongan']
        GAJI = data_karyawan[KEY]['gaji']

        print(f"{index+1:<7} {NAMA:<20} {UMUR:<4} {JENIS_KELAMIN:^19} {GOLONGAN:^10} Rp{GAJI:^10,}")

    isLanjut = input("\nApakah ingin lanjut(y/n): ").lower()
    if isLanjut == 'n':
        break
