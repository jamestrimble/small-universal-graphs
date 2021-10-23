import sys

from universalgraphs import Graph, induced_subgraph_isomorphism

def read_all_trees(n):
    with open("graphs/tree{}.all.txt".format(n), "r") as f:
        for line in f:
            tokens = [int(tok) for tok in line.strip().split()]
            edges = zip(tokens[::2], tokens[1::2])
            G = Graph(n)
            for v, w in edges:
                G.add_edge(v, w)
            yield G

    
def initial_graph(n, nP):
    G = Graph(n)
    for v in range(1, nP):
        G.add_edge(0, v)
    return G

    
def iso(P, T):
    return induced_subgraph_isomorphism(P, T)


def isomorphic(G, H):
    if G[1] != H[1]:  # For speed, compare degree sequences first
        return False
    return iso(G[0], H[0])


def try_adding_universal_graph(T, universal_graphs):
    if not any(isomorphic(G, T) for G in universal_graphs):
        universal_graphs.append(T)


def deg_seq(G):
    return sorted([sum(row) for row in G._adj_mat])


def search(nT, nP, patterns, universal_graphs, vals):
    if len(vals) <= 2:
        print(vals)
    n = len(vals)
    if n == nT - 1:
        T = initial_graph(nT, nP)
        for v, ww in enumerate(vals):
            if v == 0:
                for i in range(ww):
                    T.add_edge(v, nT - i - 1)
            else:
                for i in range(nT - nP):
                    if (ww & (1 << i)):
                        T.add_edge(v, nT - i - 1)
        if all(iso(P, T) for P in patterns):
            try_adding_universal_graph((T, deg_seq(T)), universal_graphs)
        return
    if n == 0:
        top = nT - nP + 1
    elif n == 1:
        top = 1 << (nT - nP)
    elif n < nP:
        top = vals[-1] + 1
    else:
        top = 1 << (nT - n - 1)
    for i in range(top):
        vals.append(i)
        search(nT, nP, patterns, universal_graphs, vals)
        vals.pop()


def start():
    if len(sys.argv) < 3:
        print("Usage: python3 {} NP NT".format(sys.argv[0]))
        exit(1)

    nP = int(sys.argv[1])
    nT = int(sys.argv[2])

    patterns = [G for G in read_all_trees(nP)]

    patterns.sort(key=lambda G: -len(induced_subgraph_isomorphism(G, G, True)))

    universal_graphs = []
    search(nT, nP, patterns, universal_graphs, [])
    print(len(universal_graphs))


if __name__ == "__main__":
    start()
