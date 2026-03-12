import numpy as np

print("=" * 50)
print("SISTEM DATA MAHASISWA")
print("=" * 50)

jumlah = int(input("Masukkan jumlah mahasiswa: "))

nama = np.array([])
nim = np.array([])
nilai = np.array([])
tahun = np.array([])

for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}")
    n = input("Nama: ")
    id = input("NIM: ")
    nl = float(input("Nilai: "))
    th = int(input("Tahun Masuk: "))
    
    nama = np.append(nama, n)
    nim = np.append(nim, id)
    nilai = np.append(nilai, nl)
    tahun = np.append(tahun, th)

print("\n" + "=" * 50)
print("DATA SEMUA MAHASISWA")
print("=" * 50)
for i in range(len(nama)):
    print(f"{i+1}. {nama[i]} | NIM: {nim[i]} | Nilai: {nilai[i]} | Tahun: {tahun[i]}")

print("\n" + "=" * 50)
print("STATISTIK NILAI")
print("=" * 50)
print(f"Nilai Tertinggi: {np.max(nilai)}")
print(f"Nilai Terendah: {np.min(nilai)}")
print(f"Nilai Rata-rata: {np.mean(nilai):.2f}")

print("\n" + "=" * 50)
print("PENCARIAN MAHASISWA")
print("=" * 50)
pilihan = input("Cari berdasarkan (1) NIM atau (2) Nama? ")

if pilihan == "1":
    cari = input("Masukkan NIM: ")
    idx = np.where(nim == cari)[0]
elif pilihan == "2":
    cari = input("Masukkan Nama: ")
    idx = np.where(nama == cari)[0]

if len(idx) > 0:
    i = idx[0]
    print(f"\nData Ditemukan:")
    print(f"Nama: {nama[i]}")
    print(f"NIM: {nim[i]}")
    print(f"Nilai: {nilai[i]}")
    print(f"Tahun Masuk: {tahun[i]}")
else:
    print("\nData tidak ditemukan!")