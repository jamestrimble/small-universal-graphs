import sys

d = {}

for line in sys.stdin:
    line = line.strip().split()
    key = tuple(line[:-1])
    if key not in d:
        d[key] = {"count": 0, "example_graph": line[-1]}
    d[key]["count"] += 1

for key in sorted(d.keys()):
    print(d[key]["example_graph"], " ".join(key), d[key]["count"])
