import numpy as np
import skfuzzy as fuzz

print("=== FUZZY ROBOT PENGHINDAR HALANGAN ===")

kiri = float(input("Masukkan jarak sensor kiri (0-200 cm): "))
kanan = float(input("Masukkan jarak sensor kanan (0-200 cm): "))

print("\nINPUT:")
print(f"Jarak Kiri: {kiri:.2f} cm")
print(f"Jarak Kanan: {kanan:.2f} cm")

x_sensor = np.linspace(0, 200, 401)
x_kecepatan = np.linspace(0, 100, 201)
x_arah = np.linspace(-90, 90, 361)

dekat = fuzz.trapmf(x_sensor, [0, 0, 20, 60])
sedang = fuzz.trimf(x_sensor, [40, 100, 160])
jauh = fuzz.trapmf(x_sensor, [140, 180, 200, 200])

lambat = fuzz.trapmf(x_kecepatan, [0, 0, 15, 35])
normal = fuzz.trimf(x_kecepatan, [25, 50, 75])
kencang = fuzz.trapmf(x_kecepatan, [65, 85, 100, 100])

belok_kiri_tajam = fuzz.trapmf(x_arah, [-90, -90, -70, -30])
belok_kiri = fuzz.trimf(x_arah, [-50, -25, 0])
lurus = fuzz.trimf(x_arah, [-15, 0, 15])
belok_kanan = fuzz.trimf(x_arah, [0, 25, 50])
belok_kanan_tajam = fuzz.trapmf(x_arah, [30, 70, 90, 90])

mu_dekat_kiri = fuzz.interp_membership(x_sensor, dekat, kiri)
mu_sedang_kiri = fuzz.interp_membership(x_sensor, sedang, kiri)
mu_jauh_kiri = fuzz.interp_membership(x_sensor, jauh, kiri)

mu_dekat_kanan = fuzz.interp_membership(x_sensor, dekat, kanan)
mu_sedang_kanan = fuzz.interp_membership(x_sensor, sedang, kanan)
mu_jauh_kanan = fuzz.interp_membership(x_sensor, jauh, kanan)

print("\n=== FUZZIFIKASI ===")

print(f"Sensor Kiri ({kiri:.0f} cm):")
print(f"Dekat : {mu_dekat_kiri:.6f}")
print(f"Sedang: {mu_sedang_kiri:.6f}")
print(f"Jauh  : {mu_jauh_kiri:.6f}")

print(f"\nSensor Kanan ({kanan:.0f} cm):")
print(f"Dekat : {mu_dekat_kanan:.6f}")
print(f"Sedang: {mu_sedang_kanan:.6f}")
print(f"Jauh  : {mu_jauh_kanan:.6f}")

r1 = min(mu_dekat_kiri, mu_dekat_kanan)
r2 = min(mu_dekat_kiri, mu_sedang_kanan)
r3 = min(mu_dekat_kiri, mu_jauh_kanan)

r4 = min(mu_sedang_kiri, mu_dekat_kanan)
r5 = min(mu_sedang_kiri, mu_sedang_kanan)
r6 = min(mu_sedang_kiri, mu_jauh_kanan)

r7 = min(mu_jauh_kiri, mu_dekat_kanan)
r8 = min(mu_jauh_kiri, mu_sedang_kanan)
r9 = min(mu_jauh_kiri, mu_jauh_kanan)

print("\n=== FIRING STRENGTH ===")
print(f"R1: {r1:.6f}")
print(f"R2: {r2:.6f}")
print(f"R3: {r3:.6f}")
print(f"R4: {r4:.6f}")
print(f"R5: {r5:.6f}")
print(f"R6: {r6:.6f}")
print(f"R7: {r7:.6f}")
print(f"R8: {r8:.6f}")
print(f"R9: {r9:.6f}")

rule_kec_1 = np.fmin(r1, lambat)
rule_kec_2 = np.fmin(r2, lambat)
rule_kec_3 = np.fmin(r3, normal)

rule_kec_4 = np.fmin(r4, lambat)
rule_kec_5 = np.fmin(r5, normal)
rule_kec_6 = np.fmin(r6, normal)

rule_kec_7 = np.fmin(r7, normal)
rule_kec_8 = np.fmin(r8, normal)
rule_kec_9 = np.fmin(r9, kencang)

rule_arah_1 = np.fmin(r1, lurus)
rule_arah_2 = np.fmin(r2, belok_kanan)
rule_arah_3 = np.fmin(r3, belok_kanan_tajam)

rule_arah_4 = np.fmin(r4, belok_kiri)
rule_arah_5 = np.fmin(r5, lurus)
rule_arah_6 = np.fmin(r6, belok_kanan)

rule_arah_7 = np.fmin(r7, belok_kiri_tajam)
rule_arah_8 = np.fmin(r8, belok_kiri)
rule_arah_9 = np.fmin(r9, lurus)

aggregated_kec = np.fmax(rule_kec_1,
                 np.fmax(rule_kec_2,
                 np.fmax(rule_kec_3,
                 np.fmax(rule_kec_4,
                 np.fmax(rule_kec_5,
                 np.fmax(rule_kec_6,
                 np.fmax(rule_kec_7,
                 np.fmax(rule_kec_8, rule_kec_9))))))))

aggregated_arah = np.fmax(rule_arah_1,
                  np.fmax(rule_arah_2,
                  np.fmax(rule_arah_3,
                  np.fmax(rule_arah_4,
                  np.fmax(rule_arah_5,
                  np.fmax(rule_arah_6,
                  np.fmax(rule_arah_7,
                  np.fmax(rule_arah_8, rule_arah_9))))))))

hasil_kecepatan = fuzz.defuzz(x_kecepatan, aggregated_kec, 'centroid')
hasil_arah = fuzz.defuzz(x_arah, aggregated_arah, 'centroid')

print("\n=== DEFUZZIFIKASI (Centroid) ===")
print(f"Kecepatan: {hasil_kecepatan:.2f} cm/s")
print(f"Arah Belok: {hasil_arah:.2f} derajat")

if hasil_arah < -15:
    arah = "Kiri"
elif hasil_arah > 15:
    arah = "Kanan"
else:
    arah = "Lurus"

if hasil_kecepatan <= 35:
    kecepatan = "Lambat"
elif hasil_kecepatan <= 75:
    kecepatan = "Normal"
else:
    kecepatan = "Kencang"

print(f"Interpretasi: Belok {arah} dengan kecepatan {kecepatan}")