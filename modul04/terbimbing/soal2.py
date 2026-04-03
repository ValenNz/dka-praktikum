import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title('Graf Peta')
ax.axis('off')

cities = {
    'Jakarta': (50, 200),
    'Bandung': (150, 120),
    'Cirebon': (250, 220),
    'Yogyakarta': (400, 80),
    'Semarang': (450, 200),
    'Surakarta': (500, 140),
    'Surabaya': (650, 200),
    'Malang': (700, 100)
}

edges = [
    ('Jakarta', 'Cirebon', 327),
    ('Jakarta', 'Bandung', 270),
    ('Bandung', 'Cirebon', 120),
    ('Bandung', 'Yogyakarta', 373),
    ('Cirebon', 'Semarang', 305),
    ('Cirebon', 'Yogyakarta', 210),
    ('Yogyakarta', 'Semarang', 109),
    ('Yogyakarta', 'Surakarta', 60),
    ('Semarang', 'Surakarta', 97),
    ('Semarang', 'Surabaya', 369),
    ('Surakarta', 'Malang', 370),
    ('Surabaya', 'Malang', 94)
]

for name, (x, y) in cities.items():
    ax.plot(x, y, 'o')
    ax.text(x, y+10, name, ha='center')

for a, b, d in edges:
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    
    ax.plot([x1, x2], [y1, y2])
    
    ax.text((x1+x2)/2, (y1+y2)/2, str(d))

plt.show()