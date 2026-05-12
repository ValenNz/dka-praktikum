import random
import math

def fungsi_rastrigin(koordinat):
    dimensi = len(koordinat)
    return 10 * dimensi + sum(nilai**2 - 10 * math.cos(2 * math.pi * nilai) for nilai in koordinat)

def simulated_annealing_rastrigin(jumlah_dimensi, temperatur_awal, temperatur_minimum, laju_pendinginan, iterasi_per_temperatur):
    posisi_saat_ini = [random.uniform(-5.12, 5.12) for _ in range(jumlah_dimensi)]
    biaya_saat_ini = fungsi_rastrigin(posisi_saat_ini)

    posisi_awal = posisi_saat_ini[:]
    biaya_awal = biaya_saat_ini
    posisi_terbaik = posisi_saat_ini[:]
    biaya_terbaik = biaya_saat_ini

    suhu_sekarang = temperatur_awal
    jumlah_total_iterasi = 0
    jumlah_solusi_buruk_diterima = 0
    jumlah_solusi_buruk_ditolak = 0

    while suhu_sekarang > temperatur_minimum:
        for _ in range(iterasi_per_temperatur):
            jumlah_total_iterasi += 1

            posisi_kandidat = posisi_saat_ini[:]
            indeks_dimensi = random.randint(0, jumlah_dimensi - 1)
            jarak_perturbasi = suhu_sekarang * 0.1
            posisi_kandidat[indeks_dimensi] = max(-5.12, min(5.12, posisi_kandidat[indeks_dimensi] + random.uniform(-jarak_perturbasi, jarak_perturbasi)))

            biaya_kandidat = fungsi_rastrigin(posisi_kandidat)

            if biaya_kandidat < biaya_saat_ini:
                posisi_saat_ini, biaya_saat_ini = posisi_kandidat, biaya_kandidat
            elif random.random() < math.exp((biaya_saat_ini - biaya_kandidat) / suhu_sekarang):
                posisi_saat_ini, biaya_saat_ini = posisi_kandidat, biaya_kandidat
                jumlah_solusi_buruk_diterima += 1
            else:
                jumlah_solusi_buruk_ditolak += 1

            if biaya_saat_ini < biaya_terbaik:
                posisi_terbaik = posisi_saat_ini[:]
                biaya_terbaik = biaya_saat_ini

        suhu_sekarang *= laju_pendinginan 
    return posisi_awal, biaya_awal, posisi_terbaik, biaya_terbaik, jumlah_total_iterasi, jumlah_solusi_buruk_diterima, jumlah_solusi_buruk_ditolak

random.seed(42)
jumlah_dimensi = int(input("Jumlah dimensi (n): "))
temperatur_awal = float(input("Temperatur awal (T_init): "))
temperatur_minimum = float(input("Temperatur minimum (T_min): "))
laju_pendinginan = float(input("Cooling rate (alpha): "))
iterasi_per_temperatur = int(input("Jumlah iterasi per level temperatur: "))

posisi_awal, biaya_awal, posisi_terbaik, biaya_terbaik, total_iter, diterima, ditolak = simulated_annealing_rastrigin(
    jumlah_dimensi, temperatur_awal, temperatur_minimum, laju_pendinginan, iterasi_per_temperatur
)

print("\nSIMULATED ANNEALING - FUNGSI RASTRIGIN")
print(f"Dimensi: {jumlah_dimensi}")
print(f"T_init: {temperatur_awal}, T_min: {temperatur_minimum}, Alpha: {laju_pendinginan}")
print(f"Iterasi per temperatur: {iterasi_per_temperatur}")
print(f"Solusi Awal: [{', '.join(f'{x:.6f}' for x in posisi_awal)}]")
print(f"Nilai f(x) Awal: {biaya_awal:.6f}")
print("\nHASIL OPTIMASI")
print(f"Solusi Terbaik: [{', '.join(f'{x:.6f}' for x in posisi_terbaik)}]")
print(f"Nilai f(x) Terbaik: {biaya_terbaik:.6f}")
print(f"Total Iterasi: {total_iter}")
print(f"Solusi Buruk Diterima: {diterima}")
print(f"Solusi Buruk Ditolak: {ditolak}")