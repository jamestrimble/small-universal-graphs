n = 11
k = 7

adjmat = [[0] * n for _ in range(n)]

for i in range(1, k):
    adjmat[i][0] = "\\textbf{1}"
    adjmat[0][i] = "\\textbf{1}"

for i in range(n):
    for j in range(i):
        if i == j:
            continue
        if i < k and j < k:
            continue
        if i >= k and j >= k:
            continue
        a = j + 1
        b = i - k + 1
        adjmat[i][j] = "$x_{{{}{}}}$".format(a, b)
        adjmat[j][i] = "$x_{{{}{}}}$".format(a, b)

for i in range(n):
    for j in range(i):
        if i == j:
            continue
        if i >= k and j >= k:
            adjmat[i][j] = "$\\boldsymbol{\\cdot}$"
            adjmat[j][i] = "$\\boldsymbol{\\cdot}$"

print("\draw[uofgcobalt,fill=uofgcobalt,fill opacity=0.15, thick] (-.45,-6.45) rectangle (6.45,.45);")
print("\draw[uofgpumpkin,fill=uofgpumpkin,fill opacity=0.15, thick] (6.55,-6.45) rectangle (10.45,-.45);")
#print("\draw[uofgpumpkin,fill=uofgpumpkin,fill opacity=0.15, thick] (.45,-10.45) rectangle (6.45,-6.55);")
print("\draw[uofgslate,fill=uofgslate,fill opacity=0.15, thick] (6.55,-10.45) rectangle (10.45,-6.55);")

for i in range(n):
    for j in range(n):
        print("\\node ({}_{}) at ({},{}) {{{}}};".format(i, j, i, -j, adjmat[i][j]))

