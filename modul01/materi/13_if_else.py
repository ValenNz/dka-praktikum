print("=== PERCABANGAN IF-ELSE ===\n")

# if-else sederhana
print("--- IF-ELSE SEDERHANA ---")
x = 10
print(f"x = {x}")
if x < 5:
    print("x kurang dari 5")
else:
    print("x lebih besar atau sama dengan 5")

print()

# Cek ganjil-genap
print("--- CEK GANJIL-GENAP ---")
angka = int(input("Masukkan angka: "))
if angka % 2 == 0:
    print(f"{angka} adalah bilangan GENAP")
else:
    print(f"{angka} adalah bilangan GANJIL")

print()

# Nilai lulus/tidak
print("--- LULUS/TIDAK ---")
nilai = float(input("Masukkan nilai (0-100): "))
if nilai >= 60:
    print(f"Nilai {nilai}: LULUS")
else:
    print(f"Nilai {nilai}: TIDAK LULUS")

print()

# if-else dengan kondisi kompleks
print("--- KONDISI KOMPLEKS ---")
x = 10
print(f"x = {x}")
if x < 5:
    print("x kurang dari 5")
elif x < 7:
    print("x kurang dari 7")
else:
    print("x lebih besar atau sama dengan 7")