import numpy as np

# Program Inventaris Gudang dengan NumPy
print("=" * 50)
print("SISTEM INVENTARIS GUDANG")
print("=" * 50)

# Input jumlah barang
jumlah = int(input("Masukkan jumlah jenis barang: "))

# Inisialisasi array untuk menyimpan data
nama_barang = np.array([])
kode_barang = np.array([])
jumlah_barang = np.array([])
harga = np.array([])

# Input data barang
for i in range(jumlah):
    print(f"\nBarang ke-{i+1}")
    nama = input("Nama Barang: ")
    kode = input("Kode Barang: ")
    jml = int(input("Jumlah: "))
    hrg = float(input("Harga per Unit: "))
    
    nama_barang = np.append(nama_barang, nama)
    kode_barang = np.append(kode_barang, kode)
    jumlah_barang = np.append(jumlah_barang, jml)
    harga = np.append(harga, hrg)

# Hitung total nilai inventaris
nilai_per_barang = jumlah_barang * harga
total_nilai = np.sum(nilai_per_barang)

# Tampilkan semua data
print("\n" + "=" * 60)
print("DATA INVENTARIS")
print("=" * 60)
print(f"{'No':<4} {'Nama':<15} {'Kode':<10} {'Jumlah':<8} {'Harga':<12} {'Total':<12}")
print("-" * 60)

for i in range(len(nama_barang)):
    print(f"{i+1:<4} {nama_barang[i]:<15} {kode_barang[i]:<10} {int(jumlah_barang[i]):<8} {harga[i]:<12.2f} {nilai_per_barang[i]:<12.2f}")

print("-" * 60)
print(f"{'TOTAL NILAI INVENTARIS:':<49} Rp {total_nilai:.2f}")

# Pencarian barang
print("\n" + "=" * 50)
print("PENCARIAN BARANG")
print("=" * 50)
pilihan = input("Cari berdasarkan (1) Kode atau (2) Nama? ")

if pilihan == "1":
    cari = input("Masukkan Kode Barang: ")
    idx = np.where(kode_barang == cari)[0]
elif pilihan == "2":
    cari = input("Masukkan Nama Barang: ")
    idx = np.where(nama_barang == cari)[0]

if len(idx) > 0:
    i = idx[0]
    print(f"\nData Ditemukan:")
    print(f"Nama Barang: {nama_barang[i]}")
    print(f"Kode Barang: {kode_barang[i]}")
    print(f"Jumlah: {int(jumlah_barang[i])}")
    print(f"Harga per Unit: Rp {harga[i]:.2f}")
    print(f"Total Nilai: Rp {nilai_per_barang[i]:.2f}")
else:
    print("\nBarang tidak ditemukan!")