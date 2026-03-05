print("=== LATIHAN 1: CEK TAHUN KABISAT ===\n")

def isKabisat(tahun):
    """
    Fungsi untuk menentukan apakah suatu tahun adalah tahun kabisat
    Parameter: tahun (integer)
    Return: boolean (True jika kabisat, False jika bukan)
    """
    if (tahun % 400 == 0):
        return True
    elif (tahun % 100 == 0):
        return False
    elif (tahun % 4 == 0):
        return True
    else:
        return False

# Program utama
print("Program Cek Tahun Kabisat")
print("=" * 40)

tahun = int(input("Masukkan tahun: "))

if isKabisat(tahun):
    print(f"Tahun {tahun} adalah tahun KABISAT")
    print("Februari memiliki 29 hari")
else:
    print(f"Tahun {tahun} bukan tahun kabisat")
    print("Februari memiliki 28 hari")

print()

# Test beberapa tahun
print("Test beberapa tahun:")
test_tahun = [2000, 2024, 2023, 1900, 2004]
for t in test_tahun:
    hasil = "Kabisat" if isKabisat(t) else "Bukan Kabisat"
    print(f"  {t}: {hasil}")