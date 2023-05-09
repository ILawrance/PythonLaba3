n = 3
m = 3
a = [[2.3, 3, 7], [11.7, 2.1, 1], [-3, -10.1, 2]]
b = [[-1, -1.5, 2], [2.9, 3.4, 5], [4.5, -4.4, 6]]


def Slojenie_Vichitanie(n, m, a, b):
    c = [[0]*m for i in range(n)]
    v = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = a[i][j]+b[i][j]
            v[i][j] = a[i][j]-b[i][j]
    print(c)
    print(v)


Slojenie_Vichitanie(n, m, a, b)
