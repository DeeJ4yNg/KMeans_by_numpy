import numpy as np
from matplotlib import pyplot as plt
import random

#data = [[random.randint(1,1000),random.randint(1,1000)] for i in range(1000)]
data = [[7,7],[2,3],[6,8],[1,4],[1,2],[3,1],[8,8],[9,10],[10,7],[5,5],[7,6],[9,3],[2,8],[5,11],[5,2]]
def distance(data1, data2):
    return np.linalg.norm(np.array(data1) - np.array(data2))

def KMeans(k, data, epochs):
    centres = []
    for i in range(k):
        centres.append(data[i])

    for epoch in range(epochs):
        clusters = [[] for i in range(k)]
        for j in data:
            ds = []
            for c in centres:
                d = distance(j, c)
                ds.append(d)
            clusters[ds.index(min(ds))].append(j)
#            np.append(clusters[ds.index(min(ds))], j)
        for l in range(k):
            centres.append((np.mean(clusters[l][:][0]), np.mean(clusters[l][:][1])))
        centres = centres[k:]
    return clusters, centres

cluster_res, centres_res = KMeans(2,data,300)
n = np.array([np.array(i) for i in cluster_res])
plt.scatter(n[0][:,0], n[0][:,1], c='red')
plt.scatter(n[1][:,0], n[1][:,1], c='blue')
#plt.scatter(n[2][:,0], n[2][:,1], c='green')
plt.scatter(centres_res[0][0], centres_res[0][1], c='black')
plt.scatter(centres_res[1][0], centres_res[1][1], c='black')
#plt.scatter(centres_res[2][0], centres_res[2][1], c='black')
plt.show()

