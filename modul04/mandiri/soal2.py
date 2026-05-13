import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('soal2.csv')

fig, ax = plt.subplots(1, 2, figsize=(12,5))

ax[0].hist(
    [df['math score'], df['reading score']],
    bins=10,
    label=['Math', 'Reading'],
    color=['skyblue', 'orange'],   
    edgecolor='black',             
    alpha=0.7                      
)

ax[0].set_title('Histogram Nilai')
ax[0].legend()

box = ax[1].boxplot(
    [df['math score'], df['reading score']],
    labels=['Math', 'Reading'],
    patch_artist=True
)

colors = ['lightgreen', 'salmon']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for median in box['medians']:
    median.set_color('black')

ax[1].set_title('Boxplot Nilai')

plt.tight_layout()
plt.show()