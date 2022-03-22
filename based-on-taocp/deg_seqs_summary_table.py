import sys

d = {}

p = int(sys.argv[1])
t = int(sys.argv[2])

for line in sys.stdin:
    line = line.strip().split()
    key = tuple(line[:-1])
    if key not in d:
        d[key] = {"count": 0, "example_graph": line[-1]}
    d[key]["count"] += 1

table_template_start = r"""\begin{tabular}{m{0.15\linewidth} m{0.35\linewidth} m{0.15\linewidth} m{0.25\linewidth}}
 \toprule
    Edges & Degrees & Count & Example\\ [0.5ex]
 \midrule"""

table_template_end = r"""\bottomrule
\end{tabular}"""

print(table_template_start)

for i, key in enumerate(sorted(d.keys())):
    print(key[0], "&", " ".join(key[1:]), "&", d[key]["count"], "&",
            "\\includegraphics[height=1cm]{{15-universal-graphs/img/degree-sequences-example-graphs/graph-{}-{}-{}}}".format(p, t, i) + r"\\")

print(table_template_end)
