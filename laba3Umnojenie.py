a = [[2, 4.1, 2], [4, -1, 6.5]]
n = 2
m = 3
z = float(input("z= "))


def Umnojenie(a, n, m, z):
    for i in range(n):
        for j in range(m):
            a[i][j] = a[i][j]*z
    print(a)


Umnojenie(a, n, m, z)
