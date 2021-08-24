import sys
import random

from universalgraphs import Graph, induced_subgraph_isomorphism, from_graph6_bytes

counter = [0]

def read_all_graphs(n):
    with open("graphs/graph{}.g6".format(n), "rb") as f:
        for line in f:
            g = line.strip()
            yield (from_graph6_bytes(g), g)

    
def random_graph(n, nP):
    G = Graph(n)
    for v in range(n):
        for w in range(v):
            if v < nP and w < nP:
                G.add_edge(v, w)
            elif v >= nP-1 and w >= nP-1 and v < nP*2-1 and w < nP*2-1:
                pass
            elif random.random() < .5:
                G.add_edge(v, w)
    return G

    
def iso(P, T):
    counter[0] += 1
    return induced_subgraph_isomorphism(P, T)


def start():
    if len(sys.argv) != 5:
        print("Usage: python3 {} NP NT iters seed".format(sys.argv[0]))
        exit(1)

    nP = int(sys.argv[1])
    nT = int(sys.argv[2])
    iters = int(sys.argv[3])
    random.seed(int(sys.argv[4]))

    patterns = [G for G, _ in read_all_graphs(nP)]
    if not isinstance(patterns, list):
        patterns = [patterns]

    patterns.sort(key=lambda G: -len(induced_subgraph_isomorphism(G, G, True)))

    for i in range(iters):
        T = random_graph(nT, nP)
        if all(iso(P, T) for P in patterns):
            for row in T._adj_mat:
                print(" ".join(str(int(x)) for x in row))
            print('success', nP, nT, i)
            exit(0)
    print("no luck", nP, nT)


if __name__ == "__main__":
    start()
