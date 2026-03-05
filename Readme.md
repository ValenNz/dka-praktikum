# 🤖 Dasar Kecerdasan Artifisial - Praktikum

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-green.svg)](https://numpy.org/)
[![NetworkX](https://img.shields.io/badge/NetworkX-3.0%2B-orange.svg)](https://networkx.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-red.svg)](https://matplotlib.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Repositori ini berisi **laporan dan kode praktikum** mata kuliah **Dasar Kecerdasan Artifisial (DKA)** Program Studi S1 Informatika, Universitas Telkom.

---

## 📋 Daftar Isi

- [Tentang](#-tentang)
- [Fitur](#-fitur)
- [Struktur Repository](#-struktur-repository)
- [Instalasi](#-instalasi)
- [Cara Menjalankan](#-cara-menjalankan)
- [Modul yang Tersedia](#-modul-yang-tersedia)
- [Contoh Penggunaan](#-contoh-penggunaan)
- [Kontribusi](#-kontribusi)
- [Lisensi](#-lisensi)
- [Kontak](#-kontak)

---

## 📖 Tentang

Repositori ini merupakan kumpulan **kode sumber dan dokumentasi** dari praktikum Dasar Kecerdasan Artifisial. Setiap modul berisi:

- ✅ Kode program Python yang lengkap
- ✅ Screenshot output program
- ✅ Penjelasan konsep dan implementasi
- ✅ Soal latihan dan penyelesaiannya

**Informasi Mata Kuliah:**
| Detail | Keterangan |
|--------|------------|
| **Mata Kuliah** | Dasar Kecerdasan Artifisial |
| **Program Studi** | S1 Informatika |
| **Universitas** | Universitas Telkom |
| **Semester** | Genap 2025/2026 |
| **Laboratorium** | Laboratorium Informatika FIF |

---

## ✨ Fitur

- 🐍 **Python Fundamentals** - Pengenalan dasar pemrograman Python
- 🔢 **NumPy** - Komputasi array dan operasi numerik
- 🕸️ **NetworkX** - Manipulasi dan analisis graf
- 📊 **Matplotlib** - Visualisasi data dan grafik
- 🔍 **Search Algorithms** - BFS, DFS, UCS, A*, Greedy Best-First Search
- 🏔️ **Optimization** - Hill Climbing, Simulated Annealing
- 🧮 **SymPy** - Komputasi simbolik matematika
- 🎯 **Scikit-Fuzzy** - Sistem fuzzy logic

---

## 🛠️ Instalasi

### Prasyarat

- Python 3.8 atau lebih tinggi
- pip (Python Package Installer)
- Anaconda (direkomendasikan)

### Langkah Instalasi

1. **Clone repository ini:**
```bash
git clone https://github.com/username/DKA-Praktikum.git
cd DKA-Praktikum
```

2. **Buat virtual environment (opsional):**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Atau install manual:**
```bash
pip install numpy
pip install networkx
pip install matplotlib
pip install sympy
pip install scikit-fuzzy
```

---

## 🚀 Cara Menjalankan

### Menggunakan VS Code

1. Buka folder project di VS Code
2. Pilih file `.py` yang ingin dijalankan
3. Tekan `F5` atau klik tombol **Run**
4. Lihat output di terminal

### Menggunakan Terminal

```bash
# Contoh menjalankan modul 1
cd "Modul 01 - Pengenalan Python"
python 1_helloworld.py

# Contoh menjalankan modul 2
cd "Modul 02 - Pengenalan Library NumPy"
python 2_1_import_numpy.py
```

### Menggunakan Jupyter Notebook

```bash
jupyter notebook
```
Kemudian buka file `.ipynb` yang tersedia.

---

## 📚 Modul yang Tersedia

| Modul | Topik | Status |
|-------|-------|--------|
| 01 | Pengenalan Python | ✅ Selesai |
| 02 | Library NumPy | ✅ Selesai |
| 03 | Library NetworkX | 🔄 Dalam Progress |
| 04 | Library Matplotlib | 🔄 Dalam Progress |
| 05 | Breadth-First Search | ⏳ Akan Datang |
| 06 | Depth-First Search | ⏳ Akan Datang |
| 07 | Uniform Cost Search | ⏳ Akan Datang |
| 08 | Hill Climbing | ⏳ Akan Datang |
| 09 | Simulated Annealing | ⏳ Akan Datang |
| 10 | Greedy Best-First Search | ⏳ Akan Datang |
| 11 | A* Algorithm | ⏳ Akan Datang |
| 12 | Library SymPy | ⏳ Akan Datang |
| 13 | Library Scikit-Fuzzy | ⏳ Akan Datang |

**Keterangan:**
- ✅ = Selesai
- 🔄 = Dalam Progress
- ⏳ = Akan Datang

---

## 💻 Contoh Penggunaan

### Modul 1 - Hello World
```python
# 1_helloworld.py
print("Hello, peserta praktikum Dasar Kecerdasan Artifisial!")
```

**Output:**
```
Hello, peserta praktikum Dasar Kecerdasan Artifisial!
```

### Modul 2 - NumPy Array
```python
# 2_1_import_numpy.py
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
z = x + y

print(f"Hasil: {z}")
```

**Output:**
```
Hasil: [6 8 10 12]
```

### Modul 3 - NetworkX Graph
```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D')])

nx.draw(G, with_labels=True)
plt.show()
```

---

## 🤝 Kontribusi

Kontribusi sangat diapresiasi! Silakan ikuti langkah berikut:

1. **Fork** repository ini
2. Buat **Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit** perubahan (`git commit -m 'Add some AmazingFeature'`)
4. **Push** ke branch (`git push origin feature/AmazingFeature`)
5. Buka **Pull Request**

### Panduan Kontribusi

- Pastikan kode sudah ditest dan berjalan dengan baik
- Tambahkan dokumentasi untuk fitur baru
- Ikuti style guide Python (PEP 8)
- Sertakan screenshot output jika ada perubahan visual

---

## 📄 Lisensi

Distributed under the **MIT License**. Lihat [`LICENSE`](LICENSE) untuk informasi lebih lanjut.

```
MIT License

Copyright (c) 2026 [Nama Anda]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 📧 Kontak

| Informasi | Detail |
|-----------|--------|
| **Nama** | [Nama Anda] |
| **NIM** | [NIM Anda] |
| **Email** | [email@students.telkomuniversity.ac.id](mailto:email@students.telkomuniversity.ac.id) |
| **LinkedIn** | [linkedin.com/in/username](https://linkedin.com/in/username) |
| **Universitas** | Universitas Telkom |

---

## 🙏 Ucapan Terima Kasih

- **Koordinator MK:** Sabrina Adinda Sari, S.Kom., M.Kom.
- **Kepala Program Studi:** Dr. Mahmud Dwi Sulistiyo, S.T., M.T.
- **Asisten Laboratorium** yang telah membantu
- **Telkom University** - Fakultas Informatika

---

<div align="center">

**Made with ❤️ by [Nama Anda]**

[⬆ Back to Top](#-dasar-kecerdasan-artifisial---praktikum)

</div>