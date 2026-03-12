print("=== PARAMETER DAN ARGUMEN ===\n")

# Parameter default
print("--- PARAMETER DEFAULT ---")
def greet(name, message="Selamat datang!"):
    print(f"{message}, {name}")

greet("Fizz")
greet("Buzz", "Halo")
print()

# Parameter dengan *args
print("--- ARGS (Argument Positional) ---")
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")
print(f"sum_all(10, 20) = {sum_all(10, 20)}")
print()

# Parameter dengan **kwargs
print("--- KWARGS (Keyword Arguments) ---")
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("Info mahasiswa:")
print_info(nama="Fizz", umur=21, universitas="Telkom University")
print("\nInfo buku:")
print_info(judul="Python Programming", penulis="John Doe", tahun=2024)
print()

# Kombinasi parameter
print("--- KOMBINASI PARAMETER ---")
def contoh_fungsi(pos1, pos2, *args, default="default", **kwargs):
    print(f"Positional 1: {pos1}")
    print(f"Positional 2: {pos2}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

contoh_fungsi("a", "b", 1, 2, 3, default="custom", x=10, y=20)