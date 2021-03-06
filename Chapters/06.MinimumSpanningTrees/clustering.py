"""
Created on Saturday 17 March 2018
Last update: -

@author: Michiel Stock
michielfmstock@gmail.com

Simple clustering using MST
"""

from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
from minimumspanningtrees import *
from sklearn.metrics.pairwise import pairwise_distances

n = 200
# generate example data
X, y = make_moons(n_samples=n, random_state=1, noise=0.12)

fig, ax = plt.subplots()
ax.scatter(X[:,0], X[:,1], s=50, color=green)
fig.savefig('Figures/scatter_plot.png')

# make distance
D = pairwise_distances(X)

if __name__ == '__main__':



    # make edges
    edges = []
    vertices = []
    for i in range(n):
        vertices.append(i)
        for j in range(n):
            if i != j:
                edges.append((D[i,j], i, j))

    edges_mst, cost_mst = kruskal(vertices, edges)

    fig, ax = plt.subplots()
    # plot with links
    ax.scatter(X[:,0], X[:,1], s=50, color=green, zorder=2)
    for i, j in edges_mst:
        ax.plot([X[i,0], X[j,0]], [X[i,1], X[j,1]], color=red, zorder=1, lw=2)

    fig.savefig('Figures/scatter_plot_clustered.png')
