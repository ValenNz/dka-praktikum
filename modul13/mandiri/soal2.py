import numpy as np
import skfuzzy as fuzz

print("=== FUZZY SUGENO ORDE-0 ===")
print("=== Estimasi Tip Restoran ===")

makanan = float(input("Masukkan kualitas makanan (0-10): "))
pelayanan = float(input("Masukkan kualitas pelayanan (0-10): "))

print("\nINPUT:")
print(f"Kualitas Makanan: {makanan:.2f} / 10")
print(f"Kualitas Pelayanan: {pelayanan:.2f} / 10")

x = np.linspace(0, 10, 1001)

buruk_m = fuzz.trapmf(x, [0, 0, 2, 4])
biasa_m = fuzz.trimf(x, [3, 5, 7])
enak_m = fuzz.trapmf(x, [6, 8, 10, 10])

buruk_p = fuzz.trapmf(x, [0, 0, 2, 4])
biasa_p = fuzz.trimf(x, [3, 5, 7])
baik_p = fuzz.trapmf(x, [6, 8, 10, 10])

mu_buruk_m = fuzz.interp_membership(x, buruk_m, makanan)
mu_biasa_m = fuzz.interp_membership(x, biasa_m, makanan)
mu_enak_m = fuzz.interp_membership(x, enak_m, makanan)

mu_buruk_p = fuzz.interp_membership(x, buruk_p, pelayanan)
mu_biasa_p = fuzz.interp_membership(x, biasa_p, pelayanan)
mu_baik_p = fuzz.interp_membership(x, baik_p, pelayanan)

print("\n=== FUZZIFIKASI ===")

print("Makanan:")
print(f"Buruk : {mu_buruk_m:.6f}")
print(f"Biasa : {mu_biasa_m:.6f}")
print(f"Enak  : {mu_enak_m:.6f}")

print("\nPelayanan:")
print(f"Buruk : {mu_buruk_p:.6f}")
print(f"Biasa : {mu_biasa_p:.6f}")
print(f"Baik  : {mu_baik_p:.6f}")

z1 = 5
z2 = 8
z3 = 12
z4 = 8
z5 = 15
z6 = 18
z7 = 12
z8 = 18
z9 = 25

r1 = min(mu_buruk_m, mu_buruk_p)
r2 = min(mu_buruk_m, mu_biasa_p)
r3 = min(mu_buruk_m, mu_baik_p)

r4 = min(mu_biasa_m, mu_buruk_p)
r5 = min(mu_biasa_m, mu_biasa_p)
r6 = min(mu_biasa_m, mu_baik_p)

r7 = min(mu_enak_m, mu_buruk_p)
r8 = min(mu_enak_m, mu_biasa_p)
r9 = min(mu_enak_m, mu_baik_p)

print("\n=== EVALUASI ATURAN ===")
print(f"R1: w={r1:.6f}, z={z1}")
print(f"R2: w={r2:.6f}, z={z2}")
print(f"R3: w={r3:.6f}, z={z3}")
print(f"R4: w={r4:.6f}, z={z4}")
print(f"R5: w={r5:.6f}, z={z5}")
print(f"R6: w={r6:.6f}, z={z6}")
print(f"R7: w={r7:.6f}, z={z7}")
print(f"R8: w={r8:.6f}, z={z8}")
print(f"R9: w={r9:.6f}, z={z9}")

numerator = (
    (r1 * z1) + (r2 * z2) + (r3 * z3) +
    (r4 * z4) + (r5 * z5) + (r6 * z6) +
    (r7 * z7) + (r8 * z8) + (r9 * z9)
)

denominator = (
    r1 + r2 + r3 +
    r4 + r5 + r6 +
    r7 + r8 + r9
)

hasil = numerator / denominator

print("\n=== DEFUZZIFIKASI SUGENO ===")
print(f"Numerator: Σ(wi×zi) = {numerator:.6f}")
print(f"Denominator: Σ(wi) = {denominator:.6f}")
print(f"Tip = {hasil:.2f}%")

if hasil < 10:
    kategori = "Rendah"
elif hasil < 15:
    kategori = "Sedang"
elif hasil < 20:
    kategori = "Tinggi"
else:
    kategori = "Sangat Tinggi"

print(f"Kategori: {kategori}")