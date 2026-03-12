# File: matematika.py
"""
Module matematika - Berisi fungsi-fungsi matematika dasar
"""

def tambah(a, b):
    """Menjumlahkan dua bilangan"""
    return a + b

def kurang(a, b):
    """Mengurangi dua bilangan"""
    return a - b

def kali(a, b):
    """Mengalikan dua bilangan"""
    return a * b

def bagi(a, b):
    """Membagi dua bilangan"""
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian dengan nol"

def pangkat(a, n):
    """Memangkatkan bilangan"""
    return a ** n

def faktorial(n):
    """Menghitung faktorial"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)