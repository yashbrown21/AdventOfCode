import numpy as np
import re
import networkx as nx
from matplotlib import pyplot as plt

part1 = False
test = False
filename = r"Day8\test_d8.txt" if test else r"Day8\input_d8.txt"

with open(filename) as f:
    points = np.array([line.rstrip().split(",") for line in f.readlines()], dtype = np.float64)

distances = np.linalg.norm(points[:, None, :] - points[None, :, :], axis=2)

if part1:
    distances[np.tril_indices_from(distances)] = np.inf

    idx_lim = 1000

    # Find idx_lim smallest distances
    flat_idx = np.argpartition(distances.flatten(), idx_lim)[:idx_lim]
    rows, cols = np.unravel_index(flat_idx, distances.shape)
    topN_distances = distances[rows, cols]
    sorted_idx = np.argsort(topN_distances)
    rows = rows[sorted_idx]
    cols = cols[sorted_idx]

    connect_pairs = [(tuple(points[r, :]), tuple(points[c, :])) for r, c in zip(rows, cols)]

    G = nx.Graph();
    G.add_edges_from(connect_pairs)
    components = list(nx.connected_components(G))
    component_sizes = [len(c) for c in components]
    component_sizes = sorted(component_sizes, reverse=True)
    print(f"Part 1: {np.prod(component_sizes[0:3])}")

else:
    np.fill_diagonal(distances, np.inf)

    # Find smallest distance for each point [and the index]
    nearest_distances = np.min(distances, axis=1)
    nearest_indices = np.argmin(distances, axis=1)

    # Find the largest distance in the smallest distance array
    farthest_nearest_index = np.argmax(nearest_distances)

    # Find the closest point to the farthest away point
    nearest_in_farthest = nearest_indices[farthest_nearest_index]

    x0 = points[farthest_nearest_index, 0]
    x1 = points[nearest_in_farthest, 0]

    print(f"Part 2: {x0*x1}")