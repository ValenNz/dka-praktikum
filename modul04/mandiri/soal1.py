import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('soal1.csv')

fig, ax = plt.subplots(1, 2, figsize=(10,5))

df.groupby(['Pclass','Sex']).size().unstack().plot(kind='bar', ax=ax[0])
ax[0].set_title("Jumlah Penumpang")
ax[0].set_xlabel("Pclass")
ax[0].set_ylabel("Jumlah")

ax[1].boxplot([
    df[df['Survived']==0]['Age'].dropna(),
    df[df['Survived']==1]['Age'].dropna()
], labels=['Tidak', 'Selamat'])
ax[1].set_title("Distribusi Usia")

plt.tight_layout()
plt.show()