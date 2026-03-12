print("=== FUNGSI LAMBDA ===\n")

# Lambda sederhana
print("--- LAMBDA SEDERHANA ---")
add = lambda x, y: x + y
print(f"add(3, 4) = {add(3, 4)}")
print(f"add(10, 20) = {add(10, 20)}")
print()

# Lambda untuk operasi matematika
print("--- LAMBDA MATEMATIKA ---")
kuadrat = lambda x: x ** 2
print(f"kuadrat(5) = {kuadrat(5)}")
print(f"kuadrat(10) = {kuadrat(10)}")

pangkat = lambda x, n: x ** n
print(f"\npangkat(2, 3) = {pangkat(2, 3)}")
print(f"pangkat(5, 2) = {pangkat(5, 2)}")
print()

# Lambda dengan filter
print("--- LAMBDA DENGAN FILTER ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"List: {numbers}")

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Bilangan genap: {even_numbers}")

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Bilangan ganjil: {odd_numbers}")
print()

# Lambda dengan map
print("--- LAMBDA DENGAN MAP ---")
numbers = [1, 2, 3, 4, 5]
print(f"List: {numbers}")

squares = list(map(lambda x: x ** 2, numbers))
print(f"Kuadrat: {squares}")

cubes = list(map(lambda x: x ** 3, numbers))
print(f"Pangkat 3: {cubes}")
print()

# Lambda dengan sorted
print("--- LAMBDA DENGAN SORTED ---")
students = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
print(f"Data: {students}")

# Sort berdasarkan nama
sorted_by_name = sorted(students, key=lambda x: x[0])
print(f"Sort berdasarkan nama: {sorted_by_name}")

# Sort berdasarkan umur
sorted_by_age = sorted(students, key=lambda x: x[1])
print(f"Sort berdasarkan umur: {sorted_by_age}")