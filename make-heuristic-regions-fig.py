n = 14
k = 6

adjmat = [[0] * n for _ in range(n)]

for i in range(k):
    for j in range(i):
        adjmat[i][j] = "\\textbf{1}"
        adjmat[j][i] = "\\textbf{1}"

for i in range(k - 1, k * 2 - 1):
    for j in range(k - 1, i):
        adjmat[i][j] = "\\textbf{0}"
        adjmat[j][i] = "\\textbf{0}"

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if i < k and j < k:
            continue
        if i >= k - 1 and i < 2 * k - 1 and j >= k - 1 and j < 2 * k - 1:
            continue
        adjmat[i][j] = "$\\boldsymbol{\\cdot}$"

print("\draw[uofgcobalt,fill=uofgcobalt,fill opacity=0.15, thick] (-.5,-5.5) rectangle (5.5,.5);")
print("\draw[uofgpumpkin,fill=uofgpumpkin,fill opacity=0.15, thick] (4.5,-10.5) rectangle (10.5,-4.5);")

for i in range(n):
    for j in range(n):
        print("\\node ({}_{}) at ({},{}) {{{}}};".format(i, j, i, -j, adjmat[i][j]))

