import random
import sys
import json
import math

from universalgraphs import Graph, induced_subgraph_isomorphism, from_graph6_bytes

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

    
def print_usage_and_exit():
    print("Usage: python3 {} tree|graph NP".format(sys.argv[0]))
    exit(1)


def graph_summary(G, auto_count):
    n = G.number_of_nodes()
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if G._adj_mat[i][j]:
                edges.append((i, j))
    return n, edges, auto_count


table_template = r"""
\begin{{table}}[h!]
\centering
\begin{{tabular}}{{c l}}
 \toprule
 Automorphisms & Graphs \\ [0.5ex]
 \midrule
{}
 \bottomrule
\end{{tabular}}
\caption{{The 34 graphs of order 5, classified by automorphism group size}}
\label{{tab:graphs-by-autom-count}}
\end{{table}}
"""

graph_template = r"""\begin{{tikzpicture}}[>=latex',line join=bevel,scale=.3]
    {{
         \tikzstyle{{every node}}=[draw, circle, inner sep=1pt, minimum size=.1cm]
         {}
         {}
    }};
  \end{{tikzpicture}}"""

def vertex_x(i, n):
    return math.cos(math.radians(i / n * 360 + 90))


def vertex_y(i, n):
    return math.sin(math.radians(i / n * 360 + 90))


def vertex_tikz(n):
    retval = ""
    for i in range(n):
        retval += "\\node ({}) at ({},{}) {{}};".format(i, vertex_x(i, n), vertex_y(i, n))
    return retval


def edge_tikz(edges):
    return " ".join("\draw ({}) -- ({});".format(v, w) for v, w in edges)


def show_by_autom_count(grouped):
    table_body = ""
    for autom_count, graphs in grouped:
        table_body += "{} & ".format(autom_count)
        sep = ""
        for n, edges in graphs:
            graph_tikz = graph_template.format(vertex_tikz(n), edge_tikz(edges))
            table_body += sep + graph_tikz
            sep = "\\quad"
        table_body += "\\\\\n"
    print(table_template.format(table_body))



def start():
    arg_count = 0
    for arg in sys.argv[1:]:
        if arg_count == 0:
            graph_type = sys.argv[1]
        elif arg_count == 1:
            nP = int(sys.argv[2])
        else:
            print_usage_and_exit()
        arg_count += 1
    if arg_count != 2:
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

    random.shuffle(patterns)
    PP = [(G, len(induced_subgraph_isomorphism(G, G, True))) for G in patterns]
    summaries = []
    for G, auto_count in PP:
        n, edges, auto_count = graph_summary(G, auto_count)
        summaries.append((n, edges, auto_count))
    grouped = []
    for auto_count in sorted(set(s[2] for s in summaries), reverse=True):
        grouped.append((auto_count, [(n, edges) for n, edges, ac in summaries if ac == auto_count]))
    show_by_autom_count(grouped)


if __name__ == "__main__":
    start()
