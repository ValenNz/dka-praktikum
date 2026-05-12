import random
import math

def hitung_cost_knapsack(solusi_biner, daftar_item, kapasitas_maks):
    total_berat = sum(daftar_item[i][0] for i in range(len(solusi_biner)) if solusi_biner[i])
    total_nilai = sum(daftar_item[i][1] for i in range(len(solusi_biner)) if solusi_biner[i])
    return -total_nilai + 100 * max(0, total_berat - kapasitas_maks)

def simulated_annealing_knapsack(jumlah_item, kapasitas_maks, daftar_item, temperatur_awal, laju_pendinginan, batas_iterasi):
    solusi_saat_ini = [random.randint(0, 1) for _ in range(jumlah_item)]
    cost_saat_ini = hitung_cost_knapsack(solusi_saat_ini, daftar_item, kapasitas_maks)

    solusi_terbaik = solusi_saat_ini[:]
    cost_terbaik = cost_saat_ini
    suhu = temperatur_awal
    
    for i in range(batas_iterasi):
        solusi_baru = solusi_saat_ini[:]
        indeks_acak = random.randint(0, jumlah_item - 1)
        solusi_baru[indeks_acak] = 1 - solusi_baru[indeks_acak]
        cost_baru = hitung_cost_knapsack(solusi_baru, daftar_item, kapasitas_maks)
        
        if cost_baru < cost_saat_ini or random.random() < math.exp((cost_saat_ini - cost_baru) / max(suhu, 1e-9)):
            solusi_saat_ini, cost_saat_ini = solusi_baru, cost_baru
            
        if cost_saat_ini < cost_terbaik:
            solusi_terbaik, cost_terbaik = solusi_saat_ini[:], cost_terbaik
            
        if (i + 1) % 100 == 0:
            nilai_terkini = sum(daftar_item[j][1] for j in range(jumlah_item) if solusi_terbaik[j])
            print(f"Iterasi {i+1}: Nilai Terbaik = {nilai_terkini}")
            
        suhu *= laju_pendinginan
        
    return solusi_terbaik

random.seed(42)
jumlah_item = int(input("Jumlah item (n): "))
kapasitas_maks = int(input("Kapasitas knapsack (W): "))
daftar_item = [(int(input(f"Item {i+1} weight: ")), int(input(f"Item {i+1} value: "))) for i in range(jumlah_item)]
temperatur_awal = float(input("Temperatur awal (T_init): "))
laju_pendinginan = float(input("Cooling rate (alpha): "))
batas_iterasi = int(input("Jumlah iterasi maksimum (max_iter): "))

print("\nSA KNAPSACK 0/1")
print(f"Jumlah Item: {jumlah_item}, Kapasitas: {kapasitas_maks}")
print("Data Item:")
for i, (berat, nilai) in enumerate(daftar_item, 1):
    print(f"Item {i}: berat={berat}, nilai={nilai}")

solusi_akhir = simulated_annealing_knapsack(jumlah_item, kapasitas_maks, daftar_item, temperatur_awal, laju_pendinginan, batas_iterasi)

indeks_item_terpilih = [i+1 for i, status in enumerate(solusi_akhir) if status]
berat_akhir = sum(daftar_item[i][0] for i in range(jumlah_item) if solusi_akhir[i])
nilai_akhir = sum(daftar_item[i][1] for i in range(jumlah_item) if solusi_akhir[i])

print("\nHASIL AKHIR")
print(f"Solusi Biner: {solusi_akhir}")
print(f"Item Terpilih: {indeks_item_terpilih}")
print(f"Total Nilai: {nilai_akhir}")
print(f"Total Berat: {berat_akhir}")
print(f"Kapasitas: {kapasitas_maks}")
print(f"Status: {'VALID' if berat_akhir <= kapasitas_maks else 'TIDAK VALID'}")