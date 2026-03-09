nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

nilai_akhir = (tugas * 0.20) + (uts * 0.35) + (uas * 0.45)

print(f"Nama Mahasiswa : {nama}")
print(f"Nilai Tugas    : {tugas:.1f}")
print(f"Nilai UTS      : {uts:.1f}")
print(f"Nilai UAS      : {uas:.1f}")
print("------------------------------")
print(f"Nilai Akhir {nama} : {nilai_akhir:.2f}")