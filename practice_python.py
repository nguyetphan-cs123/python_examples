import sys
import os

# Extract Shortest Path unique id from network edges

# edges = [(1, 2, 12), (1, 3, 13), (2, 4, 24), (3, 4, 34), (4, 5, 45)]
# nodes = [1, 2, 4, 5]
#
# result_edges = [(nodes[i], nodes[i + 1]) for i in range(len(nodes) - 1)]
#
# shortest_edges = [edge[2] for edge in edges if (edge[0], edge[1]) in
#                   [(result_edge[0], result_edge[1]) for result_edge in result_edges]]

properties = ["name", "age"]
values = ["Test Phan", 12]
p_dict = dict(zip(properties, values))
print(p_dict)


