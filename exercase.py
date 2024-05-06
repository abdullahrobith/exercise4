nama = input('Nama Karyawan : ').capitalize()
jabatan = input('Jabatan [Design/Programmer/Resource]: ').capitalize()
status = input('Status Pernikahan [Y/T]: ').upper()

if jabatan == 'Design':
   gaji_pokok = 5000000
elif jabatan == 'Programmer':
   gaji_pokok = 10000000
elif jabatan == 'Resource':
    gaji_pokok = 5000000
else :
   print('Jabatan tidak terdeteksi')
   exit()

if status == 'Y':
   tunjangan_keluarga = gaji_pokok * 0.20

gaji_kotor = gaji_pokok + tunjangan_keluarga
pajak = gaji_kotor * 0.10
total_pendapatan = gaji_kotor - pajak
print(30*'=')
print(f'Nama Karyawan : {nama}')
print(f'Status Pernikahan : {status}')
print(f'Gaji Pokok Karyawan : {gaji_pokok}')
if tunjangan_keluarga != 0:
   print(f'Tunjangan Keluarga : {tunjangan_keluarga}')
print(f'Gaji Kotor : {gaji_kotor}')
print(f'Pajak : {pajak}')
print(f'Total Pendapatan : {total_pendapatan}')
print(30*'=')