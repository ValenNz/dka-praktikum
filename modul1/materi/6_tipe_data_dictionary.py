print("=== TIPE DATA DICTIONARY ===\n")

# Pendefinisian dictionary
print("--- DEFINISI DICTIONARY ---")
my_dict = {
    "nama": "Fizz",
    "umur": 21,
    "kota": "Bandung",
    "universitas": "Telkom University"
}
print(f"Dictionary: {my_dict}")
print(f"my_dict['nama']: {my_dict['nama']}")
print(f"my_dict['kota']: {my_dict['kota']}")

# Menambahkan atau memperbarui nilai
print("\n--- MENAMBAHKAN/MEMPERBARUI NILAI ---")
my_dict = {
    "nama": "Fizz",
    "umur": 21,
    "kota": "Bandung",
    "universitas": "Telkom University"
}

# Menambahkan item baru
my_dict["negara"] = "Indonesia"
print("Setelah ditambah data negara:")
print(my_dict)

# Memperbarui nilai
my_dict["umur"] = 23
print("\nSetelah nilai umur diperbarui:")
print(my_dict)

# Menghapus elemen
print("\n--- MENGHAPUS ELEMEN ---")
my_dict = {
    "nama": "Fizz",
    "umur": 21,
    "kota": "Bandung",
    "universitas": "Telkom University"
}

# Cara 1: del
del my_dict["kota"]
print("Setelah del my_dict['kota']:")
print(my_dict)

# Cara 2: pop
my_dict["kota"] = "Bandung"  # tambah lagi
kota = my_dict.pop("kota")
print(f"\nSetelah pop('kota'), nilai yang di-pop: {kota}")
print(my_dict)

# Mengakses keys dan values
print("\n--- AKSES KEYS DAN VALUES ---")
my_dict = {
    "nama": "Fizz",
    "umur": 21,
    "kota": "Bandung",
    "universitas": "Telkom University"
}

kunci = my_dict.keys()
nilai = my_dict.values()
print(f"Keys: {list(kunci)}")
print(f"Values: {list(nilai)}")

# Iterasi dalam dictionary
print("\n--- ITERASI DICTIONARY ---")
for key, value in my_dict.items():
    print(f"Nilai dari {key} adalah {value}")

# Memeriksa keberadaan key
print("\n--- CEK KEY ---")
if "nama" in my_dict:
    print("Kunci 'nama' ditemukan")
else:
    print("Kunci 'nama' tidak ditemukan")

if "negara" in my_dict:
    print("Kunci 'negara' ditemukan")
else:
    print("Kunci 'negara' tidak ditemukan")

# Get method (aman untuk key yang mungkin tidak ada)
print("\n--- GET METHOD ---")
umur = my_dict.get("umur")
print(f"Umur: {umur}")

negara = my_dict.get("negara", "Tidak ada")
print(f"Negara: {negara}")