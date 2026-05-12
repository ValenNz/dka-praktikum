import random
import math

def hitung_ackley(koordinat_x, koordinat_y):
    return -20 * math.exp(-0.2 * math.sqrt(0.5 * (koordinat_x**2 + koordinat_y**2))) - \
           math.exp(0.5 * (math.cos(2*math.pi*koordinat_x) + math.cos(2*math.pi*koordinat_y))) + math.e + 20

def jalankan_sa(suhu_awal, suhu_minimum, batas_iterasi, tipe_pendinginan):
    posisi_x = random.uniform(-5, 5)
    posisi_y = random.uniform(-5, 5)
    biaya_saat_ini = hitung_ackley(posisi_x, posisi_y)

    terbaik_x = posisi_x
    terbaik_y = posisi_y
    biaya_terbaik = biaya_saat_ini

    for iterasi in range(batas_iterasi):
        if tipe_pendinginan == 'Linear':
            suhu = suhu_awal - (suhu_awal - suhu_minimum) * (iterasi / batas_iterasi)
        elif tipe_pendinginan == 'Geometrik':
            suhu = suhu_awal * (0.995 ** iterasi)
        else:  
            suhu = suhu_awal / (1 + math.log(1 + iterasi))
            
        suhu = max(suhu, 1e-9)  
        jarak_neighbor = suhu * 0.01  
        
        kandidat_x = max(-5, min(5, posisi_x + random.gauss(0, jarak_neighbor)))
        kandidat_y = max(-5, min(5, posisi_y + random.gauss(0, jarak_neighbor)))
        biaya_baru = hitung_ackley(kandidat_x, kandidat_y)
        
        if biaya_baru < biaya_saat_ini or random.random() < math.exp((biaya_saat_ini - biaya_baru) / suhu):
            posisi_x, posisi_y, biaya_saat_ini = kandidat_x, kandidat_y, biaya_baru
            
        if biaya_saat_ini < biaya_terbaik:
            terbaik_x, terbaik_y, biaya_terbaik = posisi_x, posisi_y, biaya_saat_ini
            
    return terbaik_x, terbaik_y, biaya_terbaik

random.seed(42)
T_init = float(input("Temperatur awal (T_init): "))
T_min = float(input("Temperatur minimum (T_min): "))
jumlah_restart = int(input("Jumlah restart (num_restarts): "))
max_iter = int(input("Jumlah iterasi per run (max_iter_per_run): "))

daftar_schedule = ['Linear', 'Geometrik', 'Logaritmik']
data_hasil = {}
solusi_global = {'nama': '', 'x': 0.0, 'y': 0.0, 'nilai': float('inf')}

print(f"\nSA MULTI-RESTART - FUNGSI ACKLEY 2D")
print(f"T_init: {T_init}, T_min: {T_min}")
print(f"Restarts: {jumlah_restart}, Iterasi per run: {max_iter}")

for nama_schedule in daftar_schedule:
    print(f"\nCOOLING SCHEDULE: {nama_schedule.upper()}")
    biaya_per_restart = []
    
    for no_restart in range(1, jumlah_restart + 1):
        bx, by, bc = jalankan_sa(T_init, T_min, max_iter, nama_schedule)
        biaya_per_restart.append(bc)
        print(f"Restart {no_restart}: f(x,y) terbaik = {bc:.6f} di ({bx:.6f}, {by:.6f})")
        
        if bc < solusi_global['nilai']:
            solusi_global = {'nama': nama_schedule, 'x': bx, 'y': by, 'nilai': bc}
            
    rata_rata = sum(biaya_per_restart) / len(biaya_per_restart)
    minimum = min(biaya_per_restart)
    data_hasil[nama_schedule] = {'rata_rata': rata_rata, 'minimum': minimum}
    print(f"Rata-rata f terbaik ({nama_schedule}): {rata_rata:.6f}")
    print(f"Best f ({nama_schedule}): {minimum:.6f}")

print("\nRANKING COOLING SCHEDULE")
schedule_terurut = sorted(data_hasil.items(), key=lambda item: item[1]['rata_rata'])
for peringkat, (nama, nilai) in enumerate(schedule_terurut, 1):
    print(f"{peringkat}. {nama} - Rata-rata f: {nilai['rata_rata']:.6f}")

print("\nSOLUSI GLOBAL TERBAIK")
print(f"Cooling Schedule: {solusi_global['nama']}")
print(f"Solusi: ({solusi_global['x']:.6f}, {solusi_global['y']:.6f})")
print(f"Nilai f(x,y): {solusi_global['nilai']:.6f}")