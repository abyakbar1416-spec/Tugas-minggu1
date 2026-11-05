# MODUL: operasi3.py
# Modul fungsi mandiri (def) dengan nilai kembalian (return)

def tambah(a, b):
    """Mengembalikan hasil penjumlahan a + b"""
    return a + b

def kurang(a, b):
    """Mengembalikan hasil pengurangan a - b"""
    return a - b

def kali(a, b):
    """Mengembalikan hasil perkalian a * b"""
    return a * b

def bagi(a, b):
    """Mengembalikan hasil pembagian a / b. Menangani pencegahan pembagian nol."""
    if b == 0:
        return "Error: Tidak bisa dibagi nol"
    return a / b
