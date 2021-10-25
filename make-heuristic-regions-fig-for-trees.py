n = 9
k = 6

adjmat = [[0] * n for _ in range(n)]

for i in range(1, k):
    adjmat[i][0] = "\\textbf{1}"
    adjmat[0][i] = "\\textbf{1}"

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if i < k and j < k:
            continue
        adjmat[i][j] = "$\\boldsymbol{\\cdot}$"

print("\draw[uofgcobalt,fill=uofgcobalt,fill opacity=0.15, thick] (-.5,-5.5) rectangle (5.5,.5);")
#print("\draw[uofgpumpkin,fill=uofgpumpkin,fill opacity=0.15, thick] (4.5,-10.5) rectangle (10.5,-4.5);")

for i in range(n):
    for j in range(n):
        print("\\node ({}_{}) at ({},{}) {{{}}};".format(i, j, i, -j, adjmat[i][j]))

