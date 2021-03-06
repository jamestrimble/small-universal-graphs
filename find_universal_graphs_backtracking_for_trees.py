import sys

from universalgraphs import Graph, induced_subgraph_isomorphism, from_graph6_bytes

try:
    import igraph
except:
    pass

def read_all_graphs(n):
    with open("graphs/graph{}.g6".format(n), "rb") as f:
        for line in f:
            g = line.strip()
            yield from_graph6_bytes(g)


def read_all_trees(n):
    with open("graphs/tree{}.all.txt".format(n), "r") as f:
        for line in f:
            tokens = [int(tok) for tok in line.strip().split()]
            edges = zip(tokens[::2], tokens[1::2])
            G = Graph(n)
            for v, w in edges:
                G.add_edge(v, w)
            yield G

    
def make_target_graph(nT, nP, vals, small_graph):
    G = Graph(nT)
    for v in range(1, nP):
        G.add_edge(0, v)
    for v, ww in enumerate(vals):
        for i in range(nT - nP):
            if (ww & (1 << i)):
                G.add_edge(v, nT - i - 1)
    for v in range(nT - nP):
        for w in range(v):
            if small_graph._adj_mat[v][w]:
                G.add_edge(v + nP, w + nP)
    return G

    
def to_igraph_graph(G):
    g = igraph.Graph()
    g.add_vertices(G.number_of_nodes())
    for v in range(G.number_of_nodes()):
        for w in range(v):
            if G.adj_row(v)[w]:
                g.add_edges([(v, w)])
    return g


def igraph_induced_subgraph_isomorphism(G, H):
    g = to_igraph_graph(G)
    h = to_igraph_graph(H)
    return h.subisomorphic_lad(g, induced=True)

def iso(P, T):
    result = bool(induced_subgraph_isomorphism(P, T))
    assert result == igraph_induced_subgraph_isomorphism(P, T)
    return result


def isomorphic(G, H):
    if G[1] != H[1]:  # For speed, compare degree sequences first
        return False
    return iso(G[0], H[0])


def try_adding_universal_graph(T, universal_graphs):
    if not any(isomorphic(G, T) for G in universal_graphs):
        universal_graphs.append(T)


def deg_seq(G):
    return sorted([sum(row) for row in G._adj_mat])


def search(nT, nP, patterns, small_graphs, universal_graphs, vals):
    if len(vals) <= 2:
        print(vals)
    n = len(vals)
    if n <= 1:
        for i in range(1 << (nT - nP)):
            search(nT, nP, patterns, small_graphs, universal_graphs, vals + [i])
    elif n < nP:
        for i in range(vals[-1] + 1):
            search(nT, nP, patterns, small_graphs, universal_graphs, vals + [i])
    else:
        for small_graph in small_graphs:
            T = make_target_graph(nT, nP, vals, small_graph)
            if all(iso(P, T) for P in patterns):
                try_adding_universal_graph((T, deg_seq(T)), universal_graphs)


def start():
    if len(sys.argv) < 3:
        print("Usage: python3 {} NP NT".format(sys.argv[0]))
        exit(1)

    nP = int(sys.argv[1])
    nT = int(sys.argv[2])

    patterns = [G for G in read_all_trees(nP)]

    patterns.sort(key=lambda G: -len(induced_subgraph_isomorphism(G, G, True)))

    small_graphs = [G for G in read_all_graphs(nT - nP)]

    universal_graphs = []
    search(nT, nP, patterns, small_graphs, universal_graphs, [])
    print(len(universal_graphs))


if __name__ == "__main__":
    start()
