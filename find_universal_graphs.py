import sys

from universalgraphs import Graph, induced_subgraph_isomorphism, from_graph6_bytes

counter = [0]

def read_all_graphs(n):
    with open("graphs/graph{}.g6".format(n), "rb") as f:
        for line in f:
            g = line.strip()
            yield (from_graph6_bytes(g), g)

    
def read_all_trees(n):
    with open("graphs/tree{}.all.txt".format(n), "r") as f:
        for line in f:
            tokens = [int(tok) for tok in line.strip().split()]
            edges = zip(tokens[::2], tokens[1::2])
            G = Graph(n)
            for v, w in edges:
                G.add_edge(v, w)
            yield G

    
def iso(P, T):
    counter[0] += 1
    return induced_subgraph_isomorphism(P, T)


def start():
    if len(sys.argv) != 4:
        print("Usage: python3 {} tree|graph NP NT".format(sys.argv[0]))
        exit(1)

    graph_type = sys.argv[1]
    nP = int(sys.argv[2])
    nT = int(sys.argv[3])

    if graph_type == "tree":
        patterns = [G for G in read_all_trees(nP)]
    else:
        patterns = [G for G, _ in read_all_graphs(nP)]
        if not isinstance(patterns, list):
            patterns = [patterns]

    patterns.sort(key=lambda G: -len(induced_subgraph_isomorphism(G, G, True)))
    #patterns.sort(key=lambda G: -abs(sum(sum(row) for row in G._adj_mat) - G.number_of_nodes() * (G.number_of_nodes() - 1) / 2))

    for T, graph6_graph in read_all_graphs(nT):
        if all(iso(P, T) for P in patterns):
            print(graph6_graph.decode('ascii'))
    sys.stderr.write('{} calls\n'.format(counter[0]))


if __name__ == "__main__":
    start()
