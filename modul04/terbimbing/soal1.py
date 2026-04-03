import matplotlib.pyplot as plt

data = [
    ("Budi",81.24,73.66,95.89,2023),
    ("Siti",98.52,84.86,88.7,2024),
    ("Asep",91.96,71.03,79.93,2022),
    ("Dewi",87.96,97.28,71.91,2024),
    ("Andi",74.68,77.76,79.33,2023),
    ("Lestari",74.68,89.88,79.76,2022),
    ("Joko",71.74,79.35,91.89,2022),
    ("Rina",95.99,85.6,89.13,2022),
    ("Fajar",88.03,86.4,96.62,2024),
    ("Indah",91.24,75.55,84.17,2023),
    ("Agus",70.62,99.09,73.59,2022),
    ("Fitri",99.1,93.25,91.4,2022),
    ("Rudi",94.97,98.18,92.82,2022),
    ("Maya",76.37,96.84,86.84,2024),
    ("Hadi",75.45,87.94,93.13,2024),
    ("Sri",75.5,97.66,84.81,2023),
    ("Wawan",79.13,72.65,85.68,2024),
    ("Yuni",85.74,75.88,82.83,2022),
    ("Bambang",82.96,71.36,70.76,2023),
    ("Ayu",78.74,79.76,73.24,2022)
]

angkatan = {}

for nama, algo, matdis, dka, tahun in data:
    nilai = (algo + matdis + dka) / 3
    if tahun not in angkatan:
        angkatan[tahun] = []
    angkatan[tahun].append(nilai)

tahun_list = sorted(angkatan.keys())

maksimum = []
minimum = []
rata_rata = []

for tahun in tahun_list:
    nilai = angkatan[tahun]
    
    maksimum.append(max(nilai))
    minimum.append(min(nilai))
    
    total = 0
    for n in nilai:
        total += n
    rata_rata.append(total / len(nilai))
    
plt.plot(tahun_list, maksimum, 'o-', label='Max')
plt.plot(tahun_list, minimum, 'o-', label='Min')
plt.plot(tahun_list, rata_rata, 'o-', label='Avg')

plt.xticks(tahun_list)

plt.title("Statistik Nilai")
plt.xlabel("Tahun")
plt.ylabel("Nilai")
plt.legend()

plt.show()