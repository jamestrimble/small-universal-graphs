import sys

from universalgraphs import Graph, from_graph6_bytes

def read_all_graphs(filename):
    with open(filename, "rb") as f:
        for line in f:
            g = line.strip()
            yield (from_graph6_bytes(g), g)

    
def start():
    filename = sys.argv[1]
    outfile = sys.argv[2]
    for i, (G, g6) in enumerate(read_all_graphs(filename)):
        with open(outfile.format(i), 'w') as f:
            f.write('graph G {\n')
            f.write('  node[label="", shape=circle]\n')
            for j in range(G.number_of_nodes()):
                f.write('  {};\n'.format(j))
            for v in range(G.number_of_nodes()):
                for w in range(v):
                    if G._adj_mat[v][w]:
                        f.write('  {} -- {};\n'.format(v, w))
            f.write('}\n')


if __name__ == "__main__":
    start()
