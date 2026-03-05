print("=== PERULANGAN WHILE ===\n")

# while dasar
print("--- WHILE DASAR ---")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

print()

# while dengan kondisi kompleks
print("--- WHILE DENGAN KONDISI ---")
number = 10
while number > 0:
    number -= 1
    if number == 5:
        print("Berhenti pada 5")
        break
    print(f"Number: {number}")

print()

# while dengan else
print("--- WHILE-ELSE ---")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
else:
    print("Loop selesai secara normal")

print()

# while dengan continue
print("--- WHILE DENGAN CONTINUE ---")
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(f"Num: {num}")

print()

# Input validasi dengan while
print("--- VALIDASI INPUT ---")
password = ""
while password != "python123":
    password = input("Masukkan password: ")
    if password != "python123":
        print("Password salah, coba lagi!")
print("Akses diterima!")

print()

# while untuk menghitung
print("--- MENGHITUNG JUMLAH ---")
total = 0
count = 1
while count <= 10:
    total += count
    count += 1
print(f"Jumlah 1 sampai 10: {total}")