print("=== FUNGSI DALAM PYTHON ===\n")

# Fungsi tanpa parameter
print("--- FUNGSI TANPA PARAMETER ---")
def hello_world():
    print("Hello, World!")

hello_world()
print()

# Fungsi dengan parameter
print("--- FUNGSI DENGAN PARAMETER ---")
def greet(name):
    print(f"Halo, {name}!")

greet("Fizz")
greet("Buzz")
print()

# Fungsi dengan return value
print("--- FUNGSI DENGAN RETURN ---")
def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")
print(f"add(10, 20) = {add(10, 20)}")
print()

# Fungsi dengan multiple return
print("--- MULTIPLE RETURN ---")
def operasi_matematika(a, b):
    jumlah = a + b
    kurang = a - b
    kali = a * b
    bagi = a / b if b != 0 else 0
    return jumlah, kurang, kali, bagi

hasil = operasi_matematika(10, 5)
print(f"Hasil: {hasil}")
print(f"Tipe: {type(hasil)}")

jumlah, kurang, kali, bagi = operasi_matematika(20, 4)
print(f"\n20 + 4 = {jumlah}")
print(f"20 - 4 = {kurang}")
print(f"20 * 4 = {kali}")
print(f"20 / 4 = {bagi}")