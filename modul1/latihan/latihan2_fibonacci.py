print("=== LATIHAN 2: BILANGAN FIBONACCI ===\n")

def fibonacci_fungsi(n):
    """
    Fungsi untuk menghitung bilangan Fibonacci ke-n
    Parameter: n (integer)
    Return: bilangan Fibonacci ke-n
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

def fibonacci_prosedur(n):
    """
    Prosedur untuk mencetak barisan Fibonacci dari suku ke-1 hingga ke-n
    Parameter: n (integer)
    """
    print(f"Barisan Fibonacci (1 hingga {n}):")
    a, b = 0, 1
    for i in range(1, n + 1):
        print(f"  F({i}) = {a}")
        a, b = b, a + b

# Program utama
print("Program Bilangan Fibonacci")
print("=" * 40)

n = int(input("Masukkan nilai n: "))

print()
print("--- Menggunakan Fungsi ---")
hasil = fibonacci_fungsi(n)
print(f"Bilangan Fibonacci ke-{n} adalah: {hasil}")

print()
print("--- Menggunakan Prosedur ---")
fibonacci_prosedur(n)

print()
print("--- Test Fungsi ---")
for i in range(1, 11):
    print(f"F({i:2d}) = {fibonacci_fungsi(i):3d}")