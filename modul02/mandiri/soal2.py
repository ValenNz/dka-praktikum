import numpy as np
import random
nama_pelanggan = []
kode_undian = []
data_pelanggan = None  

def generate_kode():
    """Generate kode undian UND-XXXX unik"""
    while True:
        kode = f"UND-{random.randint(1000, 9999)}"
        if kode not in kode_undian:
            return kode

def input_data():
    """Input data pelanggan"""
    global nama_pelanggan, kode_undian, data_pelanggan
    
    jumlah = int(input("Jumlah pelanggan: "))
    nama_pelanggan = []
    kode_undian = []
    data_list = []
    
    for i in range(jumlah):
        print(f"\nPelanggan {i+1}:")
        nama = input("  Nama: ")
        belanja = float(input("  Total Belanja (Rp): "))
        transaksi = int(input("  Jumlah Transaksi: "))
        
        nama_pelanggan.append(nama)
        kode_undian.append(generate_kode()) 
        data_list.append([belanja, transaksi])
    
    data_pelanggan = np.array(data_list)
    print("\n Data tersimpan!")

def tampilkan_data():
    """Tampilkan semua data pelanggan"""
    if data_pelanggan is None:
        print("\n Data belum ada!")
        return
    
    print("\n=== DATA PELANGGAN ===")
    print(f"{'No':<4} {'Kode':<12} {'Nama':<15} {'Belanja':<15} {'Transaksi':<10}")
    print("-" * 60)
    for i in range(len(nama_pelanggan)):
        print(f"{i+1:<4} {kode_undian[i]:<12} {nama_pelanggan[i]:<15} {data_pelanggan[i][0]:<15,.2f} {int(data_pelanggan[i][1]):<10}")

def hitung_rata_rata():
    """Hitung rata-rata total belanja"""
    if data_pelanggan is None:
        return 0
    
    rata_rata = np.mean(data_pelanggan[:, 0])
    print(f"\nRata-rata Total Belanja: Rp {rata_rata:,.2f}")
    return rata_rata

def pelanggan_prioritas():
    """Tampilkan pelanggan prioritas (belanja > rata-rata)"""
    if data_pelanggan is None:
        return []
    
    rata_rata = np.mean(data_pelanggan[:, 0])
    prioritas = []
    
    print(f"\n=== PELANGGAN PRIORITAS (>Rp {rata_rata:,.2f}) ===")
    for i in range(len(nama_pelanggan)):
        if data_pelanggan[i][0] > rata_rata:
            prioritas.append(i)
            print(f"  - {nama_pelanggan[i]}: Rp {data_pelanggan[i][0]:,.2f}")
    
    return prioritas

def peserta_undian():
    """Tampilkan peserta undian (transaksi ≥ 3)"""
    if data_pelanggan is None:
        return []
    
    peserta = []
    print("\n=== PESERTA UNDIAN (Transaksi ≥ 3) ===")
    for i in range(len(nama_pelanggan)):
        if data_pelanggan[i][1] >= 3:
            peserta.append(i)
            print(f"  - {nama_pelanggan[i]}: {int(data_pelanggan[i][1])} transaksi")
    
    return peserta

def hitung_slot(idx, prioritas_list):
    """Hitung slot undian per pelanggan"""
    belanja = data_pelanggan[idx][0]
    
    if belanja < 300000:
        slot = 1
    elif belanja <= 700000:
        slot = 2
    else:
        slot = 3
    
    if idx in prioritas_list:
        slot += 2
    
    return slot

def undian():
    """Lakukan undian 2 pemenang (SATU PELANGGAN HANYA BISA MENANG 1 KALI)"""
    if data_pelanggan is None:
        print("\n Data belum ada!")
        return
    
    peserta = peserta_undian()
    prioritas = pelanggan_prioritas()
    
    if len(peserta) == 0:
        print("\n Tidak ada peserta!")
        return
    
    pool = []
    for idx in peserta:
        slot = hitung_slot(idx, prioritas)
        pool.extend([idx] * slot)  
    
    print(f"\nTotal slot dalam pool: {len(pool)}")
    
    if len(pool) < 2:
        print("\n Tidak cukup peserta untuk undian!")
        return
    
    pemenang = []
    pool_copy = pool.copy()  
    
    for i in range(2):
        if len(pool_copy) == 0:
            break
        
        idx_terpilih = random.choice(pool_copy)
        pemenang.append(idx_terpilih)
        
        pool_copy = [idx for idx in pool_copy if idx != idx_terpilih]
    
    print("\n" + "=" * 50)
    print("HASIL UNDIAN")
    print("=" * 50)
    for i, idx in enumerate(pemenang):
        print(f"\nPemenang {i+1}:")
        print(f"  Kode Undian: {kode_undian[idx]}")
        print(f"  Nama: {nama_pelanggan[idx]}")
        print(f"  Total Belanja: Rp {data_pelanggan[idx][0]:,.2f}")

def cari_pelanggan():
    """Cari pelanggan berdasarkan kode undian (FLEKSIBEL)"""
    if data_pelanggan is None:
        print("\n Data belum ada!")
        return
    
    kode_input = input("Masukkan kode undian (contoh: UND-9188 atau 9188): ")
    
    kode_input = kode_input.upper().strip()
    if kode_input.startswith("UND-"):
        kode_cari = kode_input
    else:
        kode_cari = f"UND-{kode_input}"
    
    found = False
    for i in range(len(kode_undian)):
        if kode_undian[i] == kode_cari or kode_undian[i] == f"UND-{kode_input}":
            print(f"\n=== DATA DITEMUKAN ===")
            print(f"Kode Undian   : {kode_undian[i]}")
            print(f"Nama          : {nama_pelanggan[i]}")
            print(f"Total Belanja : Rp {data_pelanggan[i][0]:,.2f}")
            print(f"Jumlah Transaksi: {int(data_pelanggan[i][1])}")
            found = True
            break
    
    if not found:
        print(f"\n Kode '{kode_input}' tidak ditemukan!")

while True:
    print("\n" + "=" * 50)
    print("PROGRAM UNDIAN PELANGGAN E-COMMERCE")
    print("=" * 50)
    print("1. Input Data Pelanggan")
    print("2. Tampilkan Data")
    print("3. Hitung Rata-rata Belanja")
    print("4. Pelanggan Prioritas")
    print("5. Peserta Undian")
    print("6. Lakukan Undian")
    print("7. Cari Pelanggan")
    print("8. Keluar")
    print("=" * 50)
    
    pilih = input("Menu (1-8): ")
    
    if pilih == '1':
        input_data()
    elif pilih == '2':
        tampilkan_data()
    elif pilih == '3':
        hitung_rata_rata()
    elif pilih == '4':
        pelanggan_prioritas()
    elif pilih == '5':
        peserta_undian()
    elif pilih == '6':
        undian()
    elif pilih == '7':
        cari_pelanggan()
    elif pilih == '8':
        print("\n Program selesai!")
        break
    else:
        print("\n Pilihan tidak valid!")