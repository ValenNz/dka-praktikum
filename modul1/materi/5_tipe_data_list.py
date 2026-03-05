print("=== TIPE DATA LIST ===\n")

# Pendefinisian list
print("--- DEFINISI LIST ---")
list_numbers = [1, 3, 5, 10]
print(f"List angka: {list_numbers}")

list_strings = ["dasar", "kecerdasan", "artifisial"]
print(f"List string: {list_strings}")

list_mixed = [1, "hello", ["ini", "list"]]
print(f"List mixed: {list_mixed}")

# Mengakses elemen list
print("\n--- AKSES ELEMEN LIST ---")
my_list = [1, 3, 5, "DKA", True]
print(f"List: {my_list}")
print(f"my_list[0]: {my_list[0]}")
print(f"my_list[1]: {my_list[1]}")
print(f"my_list[-1]: {my_list[-1]}")
print(f"my_list[-2]: {my_list[-2]}")

# List slicing
print("\n--- LIST SLICING ---")
elms = my_list[1:4]
print(f"my_list[1:4]: {elms}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\nList: {numbers}")
first_five = numbers[:5]
print(f"5 elemen pertama [:5]: {first_five}")

last_three = numbers[-3:]
print(f"3 elemen terakhir [-3:]: {last_three}")

# Mengubah nilai list
print("\n--- MENGUBAH NILAI LIST ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {numbers}")
numbers[0] = 24
print(f"Setelah numbers[0] = 24: {numbers}")

# List Comprehension
print("\n--- LIST COMPREHENSION ---")

# Membuat list dari range
squares = [x**2 for x in range(10)]
print(f"Kuadrat 0-9: {squares}")

# List comprehension dengan kondisi
even_nums = [x for x in range(10) if x % 2 == 0]
print(f"Bilangan genap 0-9: {even_nums}")

# List comprehension dengan operasi string
fruits = ["apple", "banana", "cherry"]
uppercased = [fruit.upper() for fruit in fruits]
print(f"\nBuah: {fruits}")
print(f"Huruf besar: {uppercased}")

# Nested list comprehension
pairs = [(x, y) for x in range(3) for y in range(3)]
print(f"\nPasangan koordinat: {pairs}")

# Operasi pada list
print("\n--- OPERASI LIST ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Gabung list
combined = list1 + list2
print(f"{list1} + {list2} = {combined}")

# Append
list1.append(4)
print(f"Setelah append(4): {list1}")

# Insert
list1.insert(1, 100)
print(f"Setelah insert(1, 100): {list1}")

# Remove
list1.remove(100)
print(f"Setelah remove(100): {list1}")

# Pop
popped = list1.pop()
print(f"Setelah pop(): {list1}, nilai yang di-pop: {popped}")

# Length
print(f"Panjang list: {len(list1)}")