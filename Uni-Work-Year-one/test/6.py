import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

a = pd.read_csv('ClusterDs1.csv')

plt.scatter('x', 'y', data = a)
plt.show()

km = KMeans(
    n_clusters = 3,
    init = 'random',
    n_init = 10,
    max_iter = 300,
    random_state = 0
)

p = km.fit_predict(a)

plt.scatter(
    a[p == 0, 0], a[p == 0, 1],
    s = 50, c='lightgreen',
    marker='s', edgecolor='black',
    label='cluster1'

)
plt.scatter(
    a[p == 1, 0], a[p == 1, 1],
    s = 50, c='red',
    marker='o', edgecolor='black',
    label='cluster2'

)
plt.scatter(
    a[p == 2, 0], a[p == 2, 1],
    s = 50, c='yellow',
    marker='v', edgecolor='black',
    label='cluster3'

)
