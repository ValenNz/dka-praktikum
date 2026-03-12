print("=== TIPE DATA STRING ===\n")

# Pendefinisian string
str1 = "Hello, World!"
print(f"String 1: {str1}")

str2 = 'Python Programming'
print(f"String 2: {str2}")

# Penggabungan string (Concatenation)
print("\n--- PENGGABUNGAN STRING ---")
str_a = "Hello"
str_b = "World"
result_concat = str_a + " " + str_b
print(f"'{str_a}' + ' ' + '{str_b}' = '{result_concat}'")

# Pengulangan string (Repetition)
print("\n--- PENGULANGAN STRING ---")
str_repeat = "Hello"
result_repeat = str_repeat * 3
print(f"'{str_repeat}' * 3 = '{result_repeat}'")

# Mengakses karakter
print("\n--- AKSES KARAKTER ---")
str_dka = "DKA"
first_char = str_dka[0]  # indeks dimulai dari 0
last_char = str_dka[-1]  # indeks -1 adalah indeks terakhir
print(f"String: {str_dka}")
print(f"Karakter pertama [0]: {first_char}")
print(f"Karakter terakhir [-1]: {last_char}")

# String slicing
print("\n--- STRING SLICING ---")
str_slice = "Hello, World!"
sliced = str_slice[0:5]  # Mengambil karakter ke 0-4 (indeks 5 tidak termasuk)
print(f"String: {str_slice}")
print(f"str_slice[0:5] = '{sliced}'")

sliced2 = str_slice[7:12]
print(f"str_slice[7:12] = '{sliced2}'")

# Mengukur panjang string
print("\n--- PANJANG STRING ---")
str_len = "Hello, World!"
panjang = len(str_len)
print(f"String: '{str_len}'")
print(f"Panjang: {panjang} karakter")

# Method bawaan string
print("\n--- METHOD STRING ---")

# Kapitalisasi
str_upper = "Hello, World!"
print(f"Original: {str_upper}")
print(f"Upper: {str_upper.upper()}")

# Huruf kecil
str_lower = "Hello, World!"
print(f"\nOriginal: {str_lower}")
print(f"Lower: {str_lower.lower()}")

# Menghapus spasi
str_strip = "  Hello, World!  "
print(f"\nOriginal: '{str_strip}'")
print(f"Strip: '{str_strip.strip()}'")

# Mengganti bagian string
str_replace = "Hello, World!"
str_replaced = str_replace.replace("World", "Dunia")
print(f"\nOriginal: {str_replace}")
print(f"Replace: {str_replaced}")

# Split string
str_split = "Python,Java,C++,JavaScript"
list_bahasa = str_split.split(",")
print(f"\nString: {str_split}")
print(f"Split: {list_bahasa}")