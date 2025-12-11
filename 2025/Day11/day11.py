import networkx as nx
import re
import sys
import matplotlib.pyplot as plt
from itertools import permutations
from functools import cache

part1 = False
test = False
testfile = r"Day11\test_d11.txt" if part1 else r"Day11\test_d11_2.txt"
filename = testfile if test else r"Day11\input_d11.txt"

network = {}

with open(filename) as f:
    data = f.readlines()

    for line in data:
        node1, connections = line.split(": ")
        network[node1] = connections.split()

G = nx.DiGraph()
G.add_edges_from((k, v) for k, vals in network.items() for v in vals)

if part1:
    pos_paths = nx.algorithms.simple_paths.all_simple_paths(G, "you", "out")
    num_paths = sum(1 for _ in pos_paths)

else:
    required_paths = frozenset(["fft", "dac"])

    @cache
    def dfs(current, req_paths):
        req_paths = req_paths.difference([current])

        if current == "out":
            return 1 if not req_paths else 0
        
        total = 0

        for succ in G.successors(current):
            total += dfs(succ, req_paths)

        return total
    

    num_paths = dfs("svr", required_paths)

    """ for first_node, second_node in permutations(required_paths):

        print(f"Finding server to {first_node}")
        svr_to_first = list(nx.algorithms.simple_paths.all_simple_paths(G, "svr", first_node))
        print(f"Finding {first_node} to {second_node}")
        first_to_second = list(nx.algorithms.simple_paths.all_simple_paths(G, first_node, second_node))
        print(f"Finding {second_node} to out")
        second_to_out = list(nx.algorithms.simple_paths.all_simple_paths(G, second_node, "out"))
        
        # first_to_second = nx.algorithms.simple_paths.all_simple_paths(G, first_node, second_node)
        # second_to_out = nx.algorithms.simple_paths.all_simple_paths(G, second_node, "out")

        num_paths += len(svr_to_first)*len(first_to_second)*len(second_to_out)

    pos_paths = nx.algorithms.simple_paths.all_simple_paths(G, "svr", "out")
    filtered_paths = [p for p in pos_paths if required_paths.issubset(p)]
    num_paths = sum(1 for _ in filtered_paths) """

print(num_paths)