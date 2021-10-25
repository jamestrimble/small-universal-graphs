import sys
import random

from universalgraphs import Graph, induced_subgraph_isomorphism, from_graph6_bytes

counter = [0]

tikz_template = r"""{{\begin{{tikzpicture}}[>=latex',line join=bevel]
  \tikzstyle{{every node}}=[draw, circle, inner sep=1pt, minimum size=.1cm]
  \pgfsetlinewidth{{.5bp}}
  {}
  {}
\end{{tikzpicture}}}}"""

tikz_node_template = "\\node[{}] at ({},{}) ({}) {{}};\n"

tikz_edge_template = "\\draw[{}] ({}) -- ({});\n"

highlight_colour = "uofgheather"

def read_all_trees(n):
    with open("graphs/tree{}.all.txt".format(n), "r") as f:
        for line in f:
            tokens = [int(tok) for tok in line.strip().split()]
            edges = zip(tokens[::2], tokens[1::2])
            G = Graph(n)
            for v, w in edges:
                G.add_edge(v, w)
            yield G

def read_all_graphs(n):
    with open("graphs/graph{}.g6".format(n), "rb") as f:
        for line in f:
            g = line.strip()
            yield (from_graph6_bytes(g), g)

    
def random_graph(n, nP):
    # This function is not used
    G = Graph(n)
    for v in range(n):
        for w in range(v):
            if random.random() < .1:
                G.add_edge(v, w)
    return G

    
def initial_graph(n, nP):
    G = Graph(n)
    for v in range(n):
        for w in range(v):
            if v < nP and w < nP:
                if w == 0:
                    G.add_edge(v, w)
            elif random.random() < .1:
                G.add_edge(v, w)
    return G

    
def iso(P, T):
    counter[0] += 1
    return induced_subgraph_isomorphism(P, T)


def start():
    if len(sys.argv) < 6:
        print("Usage: python3 {} NP NT iters_per_T seed step".format(sys.argv[0]))
        exit(1)

    nP = int(sys.argv[1])
    nT = int(sys.argv[2])
    iters_per_T = int(sys.argv[3])
    random.seed(int(sys.argv[4]))
    step_num = int(sys.argv[5])

    patterns = [G for G in read_all_trees(nP)]

#    for P in patterns:
#        print(len(induced_subgraph_isomorphism(P, P, True)))
    patterns.sort(key=lambda G: -len(induced_subgraph_isomorphism(G, G, True)))

#    print("{} patterns".format(len(patterns)))
    overall_best = -1
    while True:
        score_cache = {}
        T = initial_graph(nT, nP)
        best = -1
        for _ in range(iters_per_T):
            v, w = choose_edge_to_change(T, nP)
            change_an_edge(T, v, w)
            flat_adj_mat = tuple(item for row in T._adj_mat for item in row)
            if flat_adj_mat in score_cache:
                score = score_cache[flat_adj_mat]
            else:
                score = calc_score(T, patterns, best)
                score_cache[flat_adj_mat] = score
            if score < best:
                # The change lowered the score, so revert it.
                change_an_edge(T, v, w)
            elif score > best:
                best = score
                if best > overall_best:
                    overall_best = best
                    sys.stderr.write("* {} {}\n".format(overall_best, len(patterns)))
            if score == len(patterns):
#                print()
#                for i in range(nT):
#                    for j in range(i):
#                        if T._adj_mat[i][j]:
#                            change_an_edge(T, i, j)
#                            if calc_score(T, patterns, len(patterns)) != len(patterns):
#                                change_an_edge(T, i, j)
#                            else:
#                                print('GOOD')
#                for row in T._adj_mat:
#                    print(" ".join(str(int(x)) for x in row))
                #### print('success', nP, nT)
                if step_num == 1:
                    with open('tmp/tree.dot', 'w') as f:
                        f.write('graph {\n')
                        for i in range(nT):
                            f.write('  v{};\n'.format(i))
                        for i in range(nT):
                            for j in range(i):
                                if T._adj_mat[i][j]:
                                    f.write('  v{} -- v{};\n'.format(i, j))
                        f.write('}\n')
                else:
                    with open('tmp/tree.txt', 'r') as f:
                        coords = [[float(c) / 150 for c in line.strip().split(",")] for line in f]
                    for P in patterns:
                        tree_vertices = set(induced_subgraph_isomorphism(P, T)[0].values())
                        nodes = []
                        for i, (x, y) in enumerate(coords):
                            colour = "gray!80"
                            if i in tree_vertices:
                                colour = "fill={}".format(highlight_colour, highlight_colour)
                            nodes.append(tikz_node_template.format(colour, x, y, i))
                        edges = []
                        for i in range(nT):
                            for j in range(i):
                                if T._adj_mat[i][j]:
                                    if i in tree_vertices and j in tree_vertices:
                                        colour = "{},thick".format(highlight_colour)
                                    else:
                                        colour = "gray!72"
                                    edges.append(tikz_edge_template.format(colour, i, j))
                        print(tikz_template.format("".join(nodes), "".join(edges)))
                        print("\\qquad")
                exit(0)


def calc_score(T, patterns, best):
    score = len(patterns)
    for P in patterns:
        if not iso(P, T):
            score -= 1
            if score < best:
                return -1
    return score


def change_an_edge(G, v, w):
    G._adj_mat[v][w] = not G._adj_mat[v][w]
    G._adj_mat[w][v] = not G._adj_mat[w][v]


def choose_edge_to_change(G, nP):
    while True:
        v = random.randrange(G.number_of_nodes())
        w = random.randrange(G.number_of_nodes())
        if v == w:
            continue
        if v < nP and w < nP:
            continue
        return v, w


if __name__ == "__main__":
    start()
