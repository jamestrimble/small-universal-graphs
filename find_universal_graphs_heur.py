import sys
import random

from universalgraphs import Graph, induced_subgraph_isomorphism, from_graph6_bytes

counter = [0]

def read_all_graphs(n):
    with open("graphs/graph{}.g6".format(n), "rb") as f:
        for line in f:
            g = line.strip()
            yield (from_graph6_bytes(g), g)

    
def random_graph(n, nP, independent_set_start):
    G = Graph(n)
    for v in range(n):
        for w in range(v):
            if v < nP and w < nP:
                G.add_edge(v, w)
            elif (v >= independent_set_start and
                  w >= independent_set_start and
                  v < independent_set_start + nP and
                  w < independent_set_start + nP):
                pass
            elif random.random() < .5:
                G.add_edge(v, w)
    return G

    
def iso(P, T):
    counter[0] += 1
    return induced_subgraph_isomorphism(P, T)


def start():
    if len(sys.argv) < 5:
        print("Usage: python3 {} NP NT iters_per_T seed [independent-set-start]".format(sys.argv[0]))
        exit(1)

    nP = int(sys.argv[1])
    nT = int(sys.argv[2])
    iters_per_T = int(sys.argv[3])
    random.seed(int(sys.argv[4]))
    if len(sys.argv) == 6:
        independent_set_start = int(sys.argv[5])
    else:
        independent_set_start = nP - 1

    patterns = [G for G, _ in read_all_graphs(nP)]
    if not isinstance(patterns, list):
        patterns = [patterns]

    patterns.sort(key=lambda G: -len(induced_subgraph_isomorphism(G, G, True)))

#    print("{} patterns".format(len(patterns)))
    overall_best = -1
    while True:
        score_cache = {}
        T = random_graph(nT, nP, independent_set_start)
        best = -1
        for j in range(iters_per_T): #range(i * 10):
            v, w = choose_edge_to_change(T, nP, independent_set_start)
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
            sys.stderr.write("{} {} {}  {}\n".format(score, best, overall_best, len(patterns)))
            if score == len(patterns):
                for row in T._adj_mat:
                    print(" ".join(str(int(x)) for x in row))
                #print('success', nP, nT)
                exit(0)
#        print()


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


def choose_edge_to_change(G, nP, independent_set_start):
    while True:
        v = random.randrange(G.number_of_nodes())
        w = random.randrange(G.number_of_nodes())
        if v == w:
            continue
        if v < nP and w < nP:
            continue
        if (v >= independent_set_start and
              w >= independent_set_start and
              v < independent_set_start + nP and
              w < independent_set_start + nP):
            continue
        return v, w


if __name__ == "__main__":
    start()
