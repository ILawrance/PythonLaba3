A = [[2, 4, 12],
     [-10, 2, 6]]

B = [[1, 2, 5,  3],
     [9, 4, 2,  5],
     [2, 15, 4, 9]]


def UmnojMatric(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return (C)


print(UmnojMatric(A, B))
