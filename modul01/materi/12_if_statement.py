print("=== PERCABANGAN IF ===\n")

# if tunggal
print("--- IF TUNGGAL ---")
x = 10
print(f"x = {x}")
if x > 5:
    print("x lebih besar dari 5")

print()

# Multiple if
print("--- MULTIPLE IF ---")
x = 10
print(f"x = {x}")
if x > 3:
    print("x lebih besar dari 3")
if x > 5:
    print("x lebih besar dari 5")
if x > 8:
    print("x lebih besar dari 8")

print()

# if dengan kondisi kompleks
print("--- KONDISI KOMPLEKS ---")
nilai = 85
print(f"Nilai: {nilai}")

if nilai >= 80:
    print("Grade: A")
if nilai >= 70 and nilai < 80:
    print("Grade: B")
if nilai >= 60 and nilai < 70:
    print("Grade: C")

print()

# if dengan input
print("--- IF DENGAN INPUT ---")
angka = int(input("Masukkan angka: "))
if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap")
if angka > 0:
    print(f"{angka} adalah bilangan positif")