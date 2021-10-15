import random
import sys

try:
    import igraph
except:
    pass

from universalgraphs import Graph, induced_subgraph_isomorphism, from_graph6_bytes

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

    
def iso(P, T, check_with_igraph):
    counter[0] += 1
    result = bool(induced_subgraph_isomorphism(P, T))
    if check_with_igraph:
        assert result == igraph_induced_subgraph_isomorphism(P, T)
    return result


def check_automorphism_counts(patterns):
    for G in patterns:
        automorphism_count1 = len(induced_subgraph_isomorphism(G, G, True))
        automorphism_count2 = to_igraph_graph(G).count_isomorphisms_vf2()
        if automorphism_count1 != automorphism_count2:
            print("Unexpected automorphism count!")
            exit(2)

def print_usage_and_exit():
    print("Usage: python3 {} tree|graph NP NT".format(sys.argv[0]))
    exit(1)

def print_automorphism_stats_and_exit(nT, patterns):
    print("auto_count deg_score count")
    automorphism_counts = [len(induced_subgraph_isomorphism(G, G, True)) for G in patterns]
    deg_scores = []
    for G in patterns:
        deg_scores.append(abs(
            sum(sum(row) for row in G._adj_mat) - G.number_of_nodes() * (G.number_of_nodes() - 1) // 2
            ))
    # c[i] will be number of targets that contain the i^th pattern as an induced subgraph
    c = [0 for _ in patterns]
    for T, graph6_graph in read_all_graphs(nT):
        for i, P in enumerate(patterns):
            if iso(P, T, False):
                c[i] += 1
    for auto_count, score, count in zip(automorphism_counts, deg_scores, c):
        print("{} {} {}".format(auto_count, score, count))
    exit(0)

def start():
    check_with_igraph = False
    print_automorphism_stats = False
    pattern_order = "automorphisms"

    arg_count = 0
    for arg in sys.argv[1:]:
        if arg == "--check":
            check_with_igraph = True
        elif arg == "--automorphism-stats":
            print_automorphism_stats = True
        elif arg == "--random-pattern-order":
            pattern_order = "random"
        elif arg == "--almost-random-pattern-order":
            pattern_order = "almost-random"
        elif arg == "--degree-pattern-order":
            pattern_order = "degree"
        elif arg.startswith("--seed="):
            random.seed(int(arg[7:]))
        else:
            if arg_count == 0:
                graph_type = arg
            elif arg_count == 1:
                nP = int(arg)
            elif arg_count == 2:
                nT = int(arg)
            else:
                print_usage_and_exit()
            arg_count += 1
    if arg_count != 3:
        print_usage_and_exit()


    if graph_type == "tree":
        patterns = [G for G in read_all_trees(nP)]
    else:
        patterns = [G for G, _ in read_all_graphs(nP)]
        if not isinstance(patterns, list):
            patterns = [patterns]
        if graph_type == "sample-of-graphs":
            random.shuffle(patterns)
            patterns = patterns[:len(patterns) // 2]

    if check_with_igraph:
        check_automorphism_counts(patterns)
        sys.stderr.write('Checked automorphism counts.\n')

    random.shuffle(patterns)
    if pattern_order == "automorphisms":
        patterns.sort(key=lambda G: -len(induced_subgraph_isomorphism(G, G, True)))
    elif pattern_order == "almost-random":
        # Move I_{nP} and K_{nP} to the start
        patterns.sort(
            key=lambda G: sum(sum(row) for row in G._adj_mat) in [0, G.number_of_nodes() * (G.number_of_nodes() - 1)],
            reverse=True
        )
    elif pattern_order == "degree":
        patterns.sort(key=lambda G: -abs(sum(sum(row) for row in G._adj_mat) - G.number_of_nodes() * (G.number_of_nodes() - 1) / 2))

    if print_automorphism_stats:
        print_automorphism_stats_and_exit(nT, patterns)

    for T, graph6_graph in read_all_graphs(nT):
        if all(iso(P, T, check_with_igraph) for P in patterns):
            print(graph6_graph.decode('ascii'))
    sys.stderr.write('{} calls\n'.format(counter[0]))


if __name__ == "__main__":
    start()
