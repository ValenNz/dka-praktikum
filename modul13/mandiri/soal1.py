import numpy as np
import skfuzzy as fuzz

print("=== FUZZY INFERENCE SYSTEM MAMDANI ===")
print("=== Kontrol Kecepatan Kipas AC ===")

suhu = float(input("Masukkan suhu ruangan (0-50 °C): "))
kelembaban = float(input("Masukkan kelembaban ruangan (0-100 %): "))

print("\nINPUT:")
print(f"Suhu: {suhu:.2f} °C")
print(f"Kelembaban: {kelembaban:.2f} %")

x_suhu = np.linspace(0, 50, 1001)
x_kelembaban = np.linspace(0, 100, 1001)
x_kipas = np.linspace(0, 100, 1001)

dingin = fuzz.trapmf(x_suhu, [0, 0, 10, 20])
sejuk = fuzz.trimf(x_suhu, [15, 22, 30])
panas = fuzz.trapmf(x_suhu, [25, 35, 50, 50])

kering = fuzz.trapmf(x_kelembaban, [0, 0, 30, 50])
normal = fuzz.trimf(x_kelembaban, [35, 50, 65])
lembab = fuzz.trapmf(x_kelembaban, [55, 70, 100, 100])

mati = fuzz.trapmf(x_kipas, [0, 0, 10, 25])
pelan = fuzz.trimf(x_kipas, [15, 35, 55])
sedang = fuzz.trimf(x_kipas, [40, 55, 70])
cepat = fuzz.trimf(x_kipas, [55, 75, 90])
maksimal = fuzz.trapmf(x_kipas, [80, 90, 100, 100])

mu_dingin = fuzz.interp_membership(x_suhu, dingin, suhu)
mu_sejuk = fuzz.interp_membership(x_suhu, sejuk, suhu)
mu_panas = fuzz.interp_membership(x_suhu, panas, suhu)

mu_kering = fuzz.interp_membership(x_kelembaban, kering, kelembaban)
mu_normal = fuzz.interp_membership(x_kelembaban, normal, kelembaban)
mu_lembab = fuzz.interp_membership(x_kelembaban, lembab, kelembaban)

print("\n=== FUZZIFIKASI ===")

print("Suhu:")
print(f"Dingin : {mu_dingin:.6f}")
print(f"Sejuk  : {mu_sejuk:.6f}")
print(f"Panas  : {mu_panas:.6f}")

print("\nKelembaban:")
print(f"Kering : {mu_kering:.6f}")
print(f"Normal : {mu_normal:.6f}")
print(f"Lembab : {mu_lembab:.6f}")

r1 = np.fmin(mu_dingin, mu_kering)
r2 = np.fmin(mu_dingin, mu_normal)
r3 = np.fmin(mu_dingin, mu_lembab)

r4 = np.fmin(mu_sejuk, mu_kering)
r5 = np.fmin(mu_sejuk, mu_normal)
r6 = np.fmin(mu_sejuk, mu_lembab)

r7 = np.fmin(mu_panas, mu_kering)
r8 = np.fmin(mu_panas, mu_normal)
r9 = np.fmin(mu_panas, mu_lembab)

print("\n=== FIRING STRENGTH (9 Aturan) ===")

print(f"R1 (Dingin AND Kering -> Mati)      : {r1:.6f}")
print(f"R2 (Dingin AND Normal -> Mati)      : {r2:.6f}")
print(f"R3 (Dingin AND Lembab -> Pelan)     : {r3:.6f}")

print(f"R4 (Sejuk AND Kering -> Pelan)      : {r4:.6f}")
print(f"R5 (Sejuk AND Normal -> Sedang)     : {r5:.6f}")
print(f"R6 (Sejuk AND Lembab -> Cepat)      : {r6:.6f}")

print(f"R7 (Panas AND Kering -> Sedang)     : {r7:.6f}")
print(f"R8 (Panas AND Normal -> Cepat)      : {r8:.6f}")
print(f"R9 (Panas AND Lembab -> Maksimal)   : {r9:.6f}")

rule1 = np.fmin(r1, mati)
rule2 = np.fmin(r2, mati)
rule3 = np.fmin(r3, pelan)

rule4 = np.fmin(r4, pelan)
rule5 = np.fmin(r5, sedang)
rule6 = np.fmin(r6, cepat)

rule7 = np.fmin(r7, sedang)
rule8 = np.fmin(r8, cepat)
rule9 = np.fmin(r9, maksimal)

aggregated = np.fmax(rule1,
             np.fmax(rule2,
             np.fmax(rule3,
             np.fmax(rule4,
             np.fmax(rule5,
             np.fmax(rule6,
             np.fmax(rule7,
             np.fmax(rule8, rule9))))))))

hasil = fuzz.defuzz(x_kipas, aggregated, 'centroid')

print("\n=== DEFUZZIFIKASI ===")
print("Metode: Centroid (1001 titik)")
print(f"Kecepatan Kipas: {hasil:.2f} %")

if hasil <= 25:
    kategori = "Mati"
elif hasil <= 55:
    kategori = "Pelan"
elif hasil <= 70:
    kategori = "Sedang"
elif hasil <= 90:
    kategori = "Cepat"
else:
    kategori = "Maksimal"

print(f"Interpretasi: {kategori}")