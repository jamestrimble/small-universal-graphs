import sys
import random

from universalgraphs import Graph, induced_subgraph_isomorphism, from_graph6_bytes

counter = [0]

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
    G = Graph(n)
    for v in range(n):
        for w in range(v):
            if random.random() < .1:
                G.add_edge(v, w)
    return G

    
def iso(P, T):
    counter[0] += 1
    return induced_subgraph_isomorphism(P, T)


def start():
    if len(sys.argv) < 5:
        print("Usage: python3 {} NP NT iters_per_T seed".format(sys.argv[0]))
        exit(1)

    nP = int(sys.argv[1])
    nT = int(sys.argv[2])
    iters_per_T = int(sys.argv[3])
    random.seed(int(sys.argv[4]))

    patterns = [G for G in read_all_trees(nP)]

#    for P in patterns:
#        print(len(induced_subgraph_isomorphism(P, P, True)))
    patterns.sort(key=lambda G: -len(induced_subgraph_isomorphism(G, G, True)))

#    print("{} patterns".format(len(patterns)))
    overall_best = -1
    while True:
        score_cache = {}
        T = random_graph(nT, nP)
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
                    print("*", overall_best, len(patterns))
                    overall_best = best
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
                for row in T._adj_mat:
                    print(" ".join(str(int(x)) for x in row))
                print('success', nP, nT)
                print('graph {')
                for i in range(nT):
                    print('  v{};'.format(i))
                for i in range(nT):
                    for j in range(i):
                        if T._adj_mat[i][j]:
                            print('  v{} -- v{};'.format(i, j))
                print('}')
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
        if v != w:
            return v, w


if __name__ == "__main__":
    start()
