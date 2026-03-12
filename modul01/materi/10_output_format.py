print("=== FORMAT OUTPUT PYTHON ===\n")

# Print sederhana
print("--- PRINT SEDERHANA ---")
print("Hello, World!")
name = "Fizz"
print("Nama saya adalah", name)
print()

# Format %
print("--- FORMAT % ---")
name = "Fizz"
age = 21
print("Nama saya adalah %s dan saya berumur %d tahun." % (name, age))

pi = 3.14159
print("Nilai pi: %.2f" % pi)
print()

# Metode str.format()
print("--- METODE str.format() ---")
name = "Fizz"
age = 21
print("Nama saya adalah {} dan saya berumur {} tahun.".format(name, age))

# Format dengan indeks
print("Nama saya adalah {1} dan saya berumur {0} tahun.".format(age, name))

# Format dengan nama
print("Nama saya adalah {nama} dan saya berumur {umur} tahun.".format(nama=name, umur=age))
print()

# F-Strings (Python 3.6+)
print("--- F-STRINGS ---")
name = "Fizz"
age = 21
print(f"Nama saya adalah {name} dan saya berumur {age} tahun.")

# F-strings dengan ekspresi
print(f"5 tahun lagi usia saya: {age + 5}")

# Format angka
angka = 1234.5678
print(f"Angka: {angka:.2f}")
print(f"Angka dengan padding: {angka:10.2f}")
print()

# Multiple lines
print("--- MULTI-LINE OUTPUT ---")
print("""
===========================
    SELAMAT DATANG
    DI PRAKTIKUM DKA
===========================
""")