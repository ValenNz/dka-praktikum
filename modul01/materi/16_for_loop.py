print("=== PERULANGAN FOR ===\n")

# for dengan list
print("--- FOR DENGAN LIST ---")
fruits = ["apple", "banana", "cherry"]
print(f"Buah: {fruits}")
for fruit in fruits:
    print(f"  - {fruit}")

print()

# for dengan string
print("--- FOR DENGAN STRING ---")
for char in "DKA":
    print(f"  Karakter: {char}")

print()

# for dengan range
print("--- FOR DENGAN RANGE ---")
print("range(5):")
for i in range(5):
    print(f"  i = {i}")

print("\nrange(1, 6):")
for i in range(1, 6):
    print(f"  i = {i}")

print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(f"  i = {i}")

print()

# for dengan enumerate
print("--- FOR DENGAN ENUMERATE ---")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"  Indeks {index}: {fruit}")

print()

# for dengan zip
print("--- FOR DENGAN ZIP ---")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"  {name} berumur {age} tahun")

print()

# Nested for
print("--- NESTED FOR ---")
print("Tabel perkalian 1-3:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i*j}")
    print()

# for dengan break dan continue
print("--- FOR DENGAN BREAK/CONTINUE ---")
print("Break pada 3:")
for i in range(5):
    if i == 3:
        break
    print(f"  i = {i}")

print("\nContinue pada 3:")
for i in range(5):
    if i == 3:
        continue
    print(f"  i = {i}")

print()

# for untuk menghitung
print("--- FOR UNTUK MENGHITUNG ---")
total = 0
for i in range(1, 11):
    total += i
print(f"Jumlah 1-10: {total}")

# Faktorial
n = 5
faktorial = 1
for i in range(1, n+1):
    faktorial *= i
print(f"Faktorial {n}: {faktorial}")