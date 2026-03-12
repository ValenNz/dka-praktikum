print("=== PERCABANGAN IF-ELIF-ELSE ===\n")

# if-elif-else dasar
print("--- IF-ELIF-ELSE DASAR ---")
x = 8
print(f"x = {x}")
if x < 5:
    print("x kurang dari 5")
elif x < 7:
    print("x kurang dari 7")
elif x < 9:
    print("x kurang dari 9")
else:
    print("x lebih besar atau sama dengan 9")

print()

# Grade nilai
print("--- GRADE NILAI ---")
nilai = float(input("Masukkan nilai (0-100): "))

if nilai >= 85:
    grade = "A"
    predikat = "Sangat Baik"
elif nilai >= 70:
    grade = "B"
    predikat = "Baik"
elif nilai >= 60:
    grade = "C"
    predikat = "Cukup"
elif nilai >= 50:
    grade = "D"
    predikat = "Kurang"
else:
    grade = "E"
    predikat = "Gagal"

print(f"Nilai: {nilai}")
print(f"Grade: {grade}")
print(f"Predikat: {predikat}")

print()

# Konversi angka ke hari
print("--- KONVERSI HARI ---")
hari = int(input("Masukkan angka hari (1-7): "))

if hari == 1:
    print("Hari: Senin")
elif hari == 2:
    print("Hari: Selasa")
elif hari == 3:
    print("Hari: Rabu")
elif hari == 4:
    print("Hari: Kamis")
elif hari == 5:
    print("Hari: Jumat")
elif hari == 6:
    print("Hari: Sabtu")
elif hari == 7:
    print("Hari: Minggu")
else:
    print("Angka tidak valid!")

print()

# Kalkulator sederhana
print("--- KALKULATOR SEDERHANA ---")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operasi = input("Pilih operasi (+, -, *, /): ")

if operasi == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")
elif operasi == "-":
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")
elif operasi == "*":
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil}")
elif operasi == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Error: Pembagian dengan nol!")
else:
    print("Operasi tidak valid!")