import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from universalgraphs import Graph, from_graph6_bytes

def read_all_graphs(filename):
    with open(filename, "rb") as f:
        for line in f:
            g = line.strip()
            yield (from_graph6_bytes(g), g)

    
def start():
    filename = sys.argv[1]
    for i, (G, g6) in enumerate(read_all_graphs(filename)):
        degrees = []
        for v in range(G.number_of_nodes()):
            degree = sum(G._adj_mat[v])
            degrees.append(degree)
        print(sum(degrees) // 2, " ".join(str(d) for d in sorted(degrees)), g6.decode('ascii'))


if __name__ == "__main__":
    start()
