print("=== RANGE STATEMENT ===\n")

# Range dasar
print("--- RANGE DASAR ---")
numbers = list(range(10))
print(f"range(10): {numbers}")

numbers2 = list(range(5))
print(f"range(5): {numbers2}")
print()

# Range dengan start dan stop
print("--- RANGE DENGAN START DAN STOP ---")
numbers = list(range(3, 8))
print(f"range(3, 8): {numbers}")

numbers2 = list(range(1, 10, 2))
print(f"range(1, 10, 2): {numbers2}")
print()

# Range dengan step
print("--- RANGE DENGAN STEP ---")
numbers = list(range(0, 20, 3))
print(f"range(0, 20, 3): {numbers}")

# Range dengan langkah negatif
print("\n--- RANGE NEGATIF ---")
numbers = list(range(10, 0, -1))
print(f"range(10, 0, -1): {numbers}")

numbers2 = list(range(5, -5, -2))
print(f"range(5, -5, -2): {numbers2}")
print()

# Range dalam for loop
print("--- RANGE DALAM FOR LOOP ---")
fruits = ["apple", "orange", "tomato", "papaya", "pear"]
print(f"Buah: {fruits}")
print("Buah dengan indeks genap:")
for i in range(0, len(fruits), 2):
    print(f"  Indeks {i}: {fruits[i]}")

print("\nHitung mundur:")
for i in range(3, 0, -1):
    print(i)
print("Go!")