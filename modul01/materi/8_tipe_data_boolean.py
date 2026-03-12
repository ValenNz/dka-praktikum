print("=== TIPE DATA BOOLEAN ===\n")

# Nilai Boolean sederhana
print("--- NILAI BOOLEAN ---")
is_student = True
informatics_student = False
print(f"is_student: {is_student}, Tipe: {type(is_student)}")
print(f"informatics_student: {informatics_student}, Tipe: {type(informatics_student)}")

# Boolean sebagai angka
print(f"\nTrue sebagai angka: {int(True)}")
print(f"False sebagai angka: {int(False)}")

# Operasi perbandingan
print("\n--- OPERASI PERBANDINGAN ---")
x = 10
y = 20
print(f"x = {x}, y = {y}")
print(f"x < y: {x < y}")
print(f"x > y: {x > y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x <= 10: {x <= 10}")
print(f"x >= 15: {x >= 15}")

# Operasi logika
print("\n--- OPERASI LOGIKA ---")
a = True
b = False
print(f"a = {a}, b = {b}")
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")
print(f"not b: {not b}")

# Kombinasi operasi
print("\n--- KOMBINASI OPERASI ---")
p = 5
q = 10
r = 15

hasil1 = (p < q) and (q < r)
print(f"({p} < {q}) and ({q} < {r}) = {hasil1}")

hasil2 = (p > q) or (q < r)
print(f"({p} > {q}) or ({q} < {r}) = {hasil2}")

# Menggunakan Boolean dalam kondisi
print("\n--- BOOLEAN DALAM KONDISI ---")
is_raining = True
if is_raining:
    print("Bawa payung!")
else:
    print("Tidak perlu payung.")

is_sunny = False
if is_sunny:
    print("Pakai kacamata hitam!")
else:
    print("Tidak perlu kacamata hitam.")