import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('soal2.csv')

fig, ax = plt.subplots(1, 2, figsize=(12,5))

ax[0].hist([df['math score'], df['reading score']], bins=10, label=['Math', 'Reading'])
ax[0].set_title('Histogram Nilai')
ax[0].legend()

ax[1].boxplot([df['math score'], df['reading score']], labels=['Math', 'Reading'])
ax[1].set_title('Boxplot Nilai')

plt.show()