print("=== TIPE DATA NUMERIK ===\n")

# Integer (bilangan bulat)
angka_bulat = 10
print(f"Integer: {angka_bulat}, Tipe: {type(angka_bulat)}")

angka_negatif = -5
print(f"Integer negatif: {angka_negatif}, Tipe: {type(angka_negatif)}")

nol = 0
print(f"Nol: {nol}, Tipe: {type(nol)}")

# Float (bilangan desimal)
angka_desimal = 3.14
print(f"\nFloat: {angka_desimal}, Tipe: {type(angka_desimal)}")

angka_kecil = -0.001
print(f"Float kecil: {angka_kecil}, Tipe: {type(angka_kecil)}")

# Complex (bilangan kompleks)
bilangan_kompleks = 1 + 2j
print(f"\nComplex: {bilangan_kompleks}, Tipe: {type(bilangan_kompleks)}")

bilangan_kompleks2 = 3j
print(f"Complex: {bilangan_kompleks2}, Tipe: {type(bilangan_kompleks2)}")

# Operasi pada bilangan kompleks
c1 = 2 + 3j
c2 = 1 + 4j
print(f"\nOperasi complex:")
print(f"{c1} + {c2} = {c1 + c2}")
print(f"{c1} * {c2} = {c1 * c2}")