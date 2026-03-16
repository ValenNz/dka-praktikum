import numpy as np

nama_mahasiswa = []
nilai_array = None

def input_data_mahasiswa():
    """Fitur 1: Input Data Mahasiswa"""
    global nama_mahasiswa, nilai_array
    
    jumlah = int(input("Masukkan jumlah mahasiswa: "))
    nama_mahasiswa = []
    data_nilai = []
    
    for i in range(jumlah):
        print(f"\nMahasiswa ke-{i+1}:")
        nama = input("Nama: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        
        nama_mahasiswa.append(nama)
        data_nilai.append([tugas, uts, uas])
    
    nilai_array = np.array(data_nilai)
    print("\n Data berhasil disimpan!")

def tampilkan_array_nilai():
    """Fitur 2: Tampilkan Array Nilai"""
    if nilai_array is None:
        print("\n Data belum ada!")
        return
    
    print("\n=== ARRAY NILAI MAHASISWA ===")
    print(f"{'No':<4} {'Nama':<15} {'Tugas':<8} {'UTS':<8} {'UAS':<8}")
    print("-" * 50)
    for i in range(len(nama_mahasiswa)):
        print(f"{i+1:<4} {nama_mahasiswa[i]:<15} {nilai_array[i][0]:<8.2f} {nilai_array[i][1]:<8.2f} {nilai_array[i][2]:<8.2f}")

def hitung_nilai_akhir():
    """Menghitung nilai akhir"""
    if nilai_array is None:
        return None
    
    nilai_akhir = (0.3 * nilai_array[:, 0]) + (0.3 * nilai_array[:, 1]) + (0.4 * nilai_array[:, 2])
    return nilai_akhir

def tampilkan_nilai_akhir():
    """Fitur 3: Tampilkan Nilai Akhir Mahasiswa"""
    nilai_akhir = hitung_nilai_akhir()
    
    if nilai_akhir is None:
        print("\n Data belum ada!")
        return
    
    print("\n=== NILAI AKHIR MAHASISWA ===")
    print(f"{'No':<4} {'Nama':<15} {'Nilai Akhir':<12}")
    print("-" * 35)
    for i in range(len(nama_mahasiswa)):
        print(f"{i+1:<4} {nama_mahasiswa[i]:<15} {nilai_akhir[i]:<12.2f}")

def analisis_nilai_kelas():
    """Fitur 4: Analisis Nilai Kelas"""
    nilai_akhir = hitung_nilai_akhir()
    
    if nilai_akhir is None:
        print("\n Data belum ada!")
        return
    
    rata_rata = np.mean(nilai_akhir)
    median = np.median(nilai_akhir)
    
    print("\n=== ANALISIS NILAI KELAS ===")
    print(f"Rata-rata nilai akhir: {rata_rata:.2f}")
    print(f"Median nilai akhir: {median:.2f}")
    
    print(f"\nMahasiswa dengan UAS > {median:.2f} (median):")
    for i in range(len(nama_mahasiswa)):
        if nilai_array[i][2] > median:
            print(f"  - {nama_mahasiswa[i]} (UAS: {nilai_array[i][2]:.2f})")

def tampilkan_3_tertinggi():
    """Fitur 5: Tampilkan 3 Nilai Tertinggi"""
    nilai_akhir = hitung_nilai_akhir()
    
    if nilai_akhir is None:
        print("\n Data belum ada!")
        return
    
    # Dapatkan indeks nilai tertinggi
    indeks_tertinggi = np.argsort(nilai_akhir)[::-1][:3]
    
    print("\n=== 3 NILAI TERTINGGI ===")
    print(f"{'Peringkat':<10} {'Nama':<15} {'Nilai Akhir':<12}")
    print("-" * 40)
    for i, idx in enumerate(indeks_tertinggi):
        print(f"{i+1:<10} {nama_mahasiswa[idx]:<15} {nilai_akhir[idx]:<12.2f}")

def cari_mahasiswa():
    """Fitur 6: Cari Data Mahasiswa"""
    if nilai_array is None:
        print("\n Data belum ada!")
        return
    
    nama_cari = input("Masukkan nama mahasiswa yang dicari: ")
    
    found = False
    for i in range(len(nama_mahasiswa)):
        if nama_mahasiswa[i].lower() == nama_cari.lower():
            print(f"\n=== DATA MAHASISWA ===")
            print(f"Nama   : {nama_mahasiswa[i]}")
            print(f"Tugas  : {nilai_array[i][0]:.2f}")
            print(f"UTS    : {nilai_array[i][1]:.2f}")
            print(f"UAS    : {nilai_array[i][2]:.2f}")
            print(f"Nilai Akhir: {(0.3*nilai_array[i][0] + 0.3*nilai_array[i][1] + 0.4*nilai_array[i][2]):.2f}")
            found = True
            break
    
    if not found:
        print(f"\n Mahasiswa '{nama_cari}' tidak ditemukan!")

def update_nilai_mahasiswa():
    """Fitur 7: Update Nilai Mahasiswa"""
    if nilai_array is None:
        print("\n Data belum ada!")
        return
    
    nama_update = input("Masukkan nama mahasiswa yang akan diupdate: ")
    
    for i in range(len(nama_mahasiswa)):
        if nama_mahasiswa[i].lower() == nama_update.lower():
            print(f"\nUpdate nilai untuk {nama_mahasiswa[i]}:")
            nilai_array[i][0] = float(input("Nilai Tugas baru: "))
            nilai_array[i][1] = float(input("Nilai UTS baru: "))
            nilai_array[i][2] = float(input("Nilai UAS baru: "))
            print("\n Data berhasil diupdate!")
            return
    
    print(f"\nMahasiswa '{nama_update}' tidak ditemukan!")

def hapus_mahasiswa():
    """Fitur 8: Hapus Mahasiswa"""
    global nama_mahasiswa, nilai_array
    
    if nilai_array is None:
        print("\n Data belum ada!")
        return
    
    nama_hapus = input("Masukkan nama mahasiswa yang akan dihapus: ")
    
    for i in range(len(nama_mahasiswa)):
        if nama_mahasiswa[i].lower() == nama_hapus.lower():
            nama_mahasiswa.pop(i)
            nilai_array = np.delete(nilai_array, i, axis=0)
            print("\nMahasiswa berhasil dihapus!")
            return
    
    print(f"\nMahasiswa '{nama_hapus}' tidak ditemukan!")

while True:
    print("\n" + "=" * 50)
    print("PROGRAM MANAJEMEN NILAI MAHASISWA")
    print("=" * 50)
    print("1. Input Data Mahasiswa")
    print("2. Tampilkan Array Nilai")
    print("3. Tampilkan Nilai Akhir Mahasiswa")
    print("4. Analisis Nilai Kelas")
    print("5. Tampilkan 3 Nilai Tertinggi")
    print("6. Cari Data Mahasiswa")
    print("7. Update Nilai Mahasiswa")
    print("8. Hapus Mahasiswa")
    print("9. Keluar")
    print("=" * 50)
    
    pilihan = input("Pilih menu (1-9): ")
    
    if pilihan == '1':
        input_data_mahasiswa()
    elif pilihan == '2':
        tampilkan_array_nilai()
    elif pilihan == '3':
        tampilkan_nilai_akhir()
    elif pilihan == '4':
        analisis_nilai_kelas()
    elif pilihan == '5':
        tampilkan_3_tertinggi()
    elif pilihan == '6':
        cari_mahasiswa()
    elif pilihan == '7':
        update_nilai_mahasiswa()
    elif pilihan == '8':
        hapus_mahasiswa()
    elif pilihan == '9':
        print("\nProgram selesai. Terima kasih!")
        break
    else:
        print("\nPilihan tidak valid!")