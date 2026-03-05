print("=== PEMROGRAMAN MODULAR ===\n")

# Import module
import matematika

print("--- MENGGUNAKAN MODULE MATEMATIKA ---")
print(f"tambah(5, 3) = {matematika.tambah(5, 3)}")
print(f"kurang(10, 4) = {matematika.kurang(10, 4)}")
print(f"kali(6, 7) = {matematika.kali(6, 7)}")
print(f"bagi(20, 4) = {matematika.bagi(20, 4)}")
print(f"pangkat(2, 8) = {matematika.pangkat(2, 8)}")
print(f"faktorial(5) = {matematika.faktorial(5)}")

print()

# Import dengan alias
print("--- IMPORT DENGAN ALIAS ---")
import matematika as mat

print(f"mat.tambah(10, 20) = {mat.tambah(10, 20)}")
print(f"mat.kali(5, 6) = {mat.kali(5, 6)}")

print()

# Import fungsi tertentu
print("--- IMPORT FUNGSI TERTENTU ---")
from matematika import tambah, kurang

print(f"tambah(100, 50) = {tambah(100, 50)}")
print(f"kurang(100, 50) = {kurang(100, 50)}")

print()

# Import semua fungsi
print("--- IMPORT SEMUA ---")
from matematika import *

print(f"kali(3, 9) = {kali(3, 9)}")