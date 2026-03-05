print("=== INPUT DAN OUTPUT PADA PYTHON ===\n")

# Input sederhana
print("--- INPUT SEDERHANA ---")
name = input("Masukkan nama Anda: ")
print(f"Halo, {name}!")
print()

# Input dengan konversi tipe data
print("--- INPUT DENGAN KONVERSI ---")
age = int(input("Masukkan usia Anda: "))
print(f"Tahun depan, usia Anda akan menjadi: {age + 1}")
print()

# Input float
height = float(input("Masukkan tinggi badan (cm): "))
print(f"Tinggi badan Anda: {height} cm")
print()

# Multiple input
print("--- MULTIPLE INPUT ---")
data = input("Masukkan nama dan kota (pisahkan dengan spasi): ")
nama, kota = data.split()
print(f"Nama: {nama}, Kota: {kota}")