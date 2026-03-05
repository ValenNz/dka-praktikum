Berikut adalah versi **lebih general** yang dapat digunakan sebagai **Template Utama** untuk seluruh repository praktikum Dasar Kecerdasan Artifisial (DKA) selama satu semester. Template ini dirancang agar dapat diterapkan untuk **semua Modul (1-13)** tanpa perlu mengubah struktur secara signifikan.

---

# 📘 Template Repository Praktikum DKA (General)

## 1. Struktur Folder Repository
Agar rapi dan mudah dinavigasi untuk semua modul, gunakan struktur folder berikut:

```
DKA-Praktikum-2026/
├── README.md                  # Panduan umum repository ini
├── LICENSE                    # Lisensi penggunaan kode
├── requirements.txt           # Daftar library yang dibutuhkan (numpy, networkx, dll)
├── Regulations/               # Salinan peraturan praktikum (PDF)
├── Modul-01-Python/           # Folder khusus Modul 1
│   ├── Code/                  # Semua file .py untuk modul ini
│   ├── Screenshots/           # Bukti output program
│   └── Laporan_Modul_01.pdf   # Laporan resmi
├── Modul-02-NumPy/            # Folder khusus Modul 2
│   ├── Code/
│   ├── Screenshots/
│   └── Laporan_Modul_02.pdf
├── Modul-03-NetworkX/         # dst...
├── ...
└── Modul-13-ScikitFuzzy/
```

---

## 2. Template README.md (General)
*Salin ini ke file `README.md` utama repository Anda.*

```markdown
# 🤖 Repositori Praktikum Dasar Kecerdasan Artifisial (DKA)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![University](https://img.shields.io/badge/University-Telkom%20University-orange.svg)](https://telkomuniversity.ac.id/)
[![Semester](https://img.shields.io/badge/Semester-Genap%202025/2026-green.svg)]()

Repository ini berisi kumpulan kode sumber, dokumentasi, dan laporan praktikum mata kuliah **Dasar Kecerdasan Artifisial** Program Studi S1 Informatika, Universitas Telkom.

## 📋 Informasi Mata Kuliah
| Detail | Keterangan |
|--------|------------|
| **Kode MK** | [Isi Kode MK] |
| **Dosen Koordinator** | Sabrina Adinda Sari, S.Kom., M.Kom. |
| **Laboratorium** | Laboratorium Informatika (Gedung TULT Lt. 6 & 7) |
| **Durasi** | 100 Menit per Pertemuan |
| **Pertemuan** | 16 Kali Pertemuan |

## 📚 Daftar Modul Praktikum
Repository ini mencakup 13 Modul Praktikum:

| Modul | Topik | Library Utama | Status |
|-------|-------|---------------|--------|
| 01 | Pengenalan Python | Standard Library | ✅ |
| 02 | Library NumPy | NumPy | ✅ |
| 03 | Library NetworkX | NetworkX | ⏳ |
| 04 | Library Matplotlib | Matplotlib | ⏳ |
| 05 | Breadth-First Search | NetworkX | ⏳ |
| 06 | Depth-First Search | NetworkX | ⏳ |
| 07 | Uniform Cost Search | NetworkX | ⏳ |
| 08 | Hill Climbing | Standard/NumPy | ⏳ |
| 09 | Simulated Annealing | Standard/NumPy | ⏳ |
| 10 | Greedy Best-First Search | NetworkX | ⏳ |
| 11 | A* Algorithm | NetworkX | ⏳ |
| 12 | Library SymPy | SymPy | ⏳ |
| 13 | Library Scikit-Fuzzy | Scikit-Fuzzy | ⏳ |

## 🛠️ Instalasi Environment
1. **Install Anaconda** (Direkomendasikan)
2. **Buat Environment Baru:**
   ```bash
   conda create -n dka-env python=3.9
   conda activate dka-env
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *Isi requirements.txt:*
   ```text
   numpy
   networkx
   matplotlib
   sympy
   scikit-fuzzy
   ```

## 📝 Format Laporan
Setiap modul wajib dikumpulkan dengan format berikut:
1. **Cover** (Nama, NIM, Kelas, Modul)
2. **Tujuan Praktikum** (Diambil dari Modul)
3. **Kode Program** (Screenshot dari VS Code/Jupyter)
4. **Output Program** (Screenshot Terminal/Console)
5. **Analisis & Penjelasan** (Penjelasan per baris kode penting)
6. **Kesimpulan**

## ⚠️ Peraturan Penting
- **Kehadiran:** Minimal 75% dari total pertemuan.
- **Keterlambatan:** 
  - ≤ 5 menit: Diizinkan masuk.
  - ≥ 30 menit: Tidak diizinkan mengikuti praktikum.
- **Susulan:** Maksimal 2 kali modul (dengan syarat administratif: sakit/tugas/musibah).
- **Plagiarisme:** Penyebaran soal/kunci jawaban akan dikenai sanksi nilai 0 atau Komisi Disiplin.
- **Kebersihan:** Wajib menghapus file praktikum setelah selesai (Pengurangan nilai 20% jika lupa).

## 📧 Kontak
| Nama | NIM | Email |
|------|-----|-------|
| [Nama Anda] | [NIM Anda] | [Email Mahasiswa] |

---
**Made with ❤️ for Telkom University Informatics Practicum**
```

---

## 3. Template Laporan Praktikum (General)
*Gunakan struktur ini untuk membuat laporan PDF setiap modul.*

### **HALAMAN JUDUL**
```
LAPORAN PRAKTIKUM DASAR KECERDASAN ARTIFISIAL
MODUL [X]: [JUDUL MODUL]

Disusun Oleh:
Nama    : [Nama Lengkap]
NIM     : [NIM]
Kelas   : [Kelas Praktikum]
Asisten : [Nama Asisten]

LABORATORIUM INFORMATIKA
FAKULTAS INFORMATIKA
UNIVERSITAS TELKOM
2026
```

### **BAB 1: PENDAHULUAN**
**1.1 Tujuan Praktikum**
*(Salin tujuan dari PDF Modul yang bersangkutan)*
1. ...
2. ...

**1.2 Dasar Teori**
*(Jelaskan singkat teori yang digunakan, misal: "NumPy adalah library untuk komputasi numerik...")*

### **BAB 2: IMPLEMENTASI**
**2.1 Kode Program**
*(Tempelkan screenshot kode dari VS Code/Jupyter. Pastikan terlihat jelas)*
![Screenshot Kode](../Modul-X/Screenshots/code_1.png)

**2.2 Output Program**
*(Tempelkan screenshot hasil running program)*
![Screenshot Output](../Modul-X/Screenshots/output_1.png)

**2.3 Penjelasan Kode**
*(Jelaskan bagian kode yang krusial)*
- **Baris 1:** Import library...
- **Baris 5:** Mendefinisikan array...
- **Baris 10:** Melakukan operasi matematika...

### **BAB 3: ANALISIS & SOAL LATIHAN**
**3.1 Analisis Hasil**
*(Apa yang terjadi jika input diubah? Apakah output sesuai ekspektasi?)*

**3.2 Jawaban Soal Latihan**
*(Kerjakan soal latihan yang ada di akhir setiap modul PDF)*
- **Soal 1:** [Jawaban & Screenshot]
- **Soal 2:** [Jawaban & Screenshot]

### **BAB 4: KESIMPULAN**
*(Ringkasan apa yang dipelajari dari modul ini)*
1. Mahasiswa mampu...
2. Mahasiswa memahami...

---

## 4. Panduan Umum Pengerjaan (Workflow)
*Ikuti langkah ini untuk setiap modul (1-13):*

1. **Persiapan (Sebelum Lab):**
   - Baca PDF Modul yang akan dipraktikumkan.
   - Pastikan Anaconda/VS Code sudah terinstall.
   - Siapkan folder sesuai struktur repository.

2. **Pelaksanaan (Saat Lab):**
   - Hadir tepat waktu (Max terlambat 5 menit).
   - Gunakan seragam sesuai aturan institusi.
   - Kerjakan contoh kode di modul terlebih dahulu.
   - **Screenshot setiap perubahan kode** untuk bukti laporan.
   - Kerjakan Soal Latihan di akhir modul.

3. **Pasca Lab:**
   - Rapikan kode (beri komentar).
   - Susun laporan sesuai template.
   - **Hapus file sementara** di komputer lab (Wajib!).
   - Upload ke Repository GitHub/IGracias sesuai deadline.

4. **Komplain (Jika ada kendala):**
   - Melalui **IGracias**: Menu Masukan & Komplain -> Input Tiket -> FIF -> Urusan Lab -> Praktikum.
   - Melalui **Website**: informatics.labs.telkomuniversity.ac.id -> Feedback.

---

## 5. Checklist Library per Modul
*Pastikan library berikut terinstall sesuai modul yang dikerjakan:*

| Modul | Library Wajib | Cara Install |
|-------|---------------|--------------|
| 1 | `python` (Bawaan) | - |
| 2 | `numpy` | `pip install numpy` |
| 3 | `networkx`, `matplotlib` | `pip install networkx matplotlib` |
| 4 | `matplotlib` | `pip install matplotlib` |
| 5-7, 10-11 | `networkx`, `matplotlib` | `pip install networkx matplotlib` |
| 8-9 | `numpy`, `random`, `math` | (Bawaan Python) |
| 12 | `sympy` | `pip install sympy` |
| 13 | `scikit-fuzzy`, `numpy` | `pip install scikit-fuzzy` |

---

## 6. Tips Sukses Praktikum DKA
1. **Backup Kode:** Selalu push ke GitHub setiap selesai satu sub-bab.
2. **Pahami Konsep:** Jangan hanya copy-paste. Pahami alur algoritma (terutama Modul 5-11 tentang Search & Optimization).
3. **Perhatikan Tipe Data:** Kesalahan umum terjadi pada tipe data (int vs float vs string) terutama di NumPy dan Fuzzy Logic.
4. **Visualisasi:** Untuk modul NetworkX dan Matplotlib, pastikan grafik muncul dengan jelas (gunakan `plt.show()`).
5. **Jaga Etika:** Dilarang menyebarkan soal/kunci jawaban ke angkatan bawah atau teman luar kelas (Sanksi Berat).

---

*Dokumen ini bersifat general dan dapat digunakan sebagai panduan standar untuk seluruh rangkaian praktikum Dasar Kecerdasan Artifisial Semester Genap 2025/2026.*