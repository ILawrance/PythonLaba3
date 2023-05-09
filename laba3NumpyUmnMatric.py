import numpy as np

a = np.array([[2, 4, 12],
              [-10, 2, 6]])

b = np.array([[1, 2, 5,  3],
              [9, 4, 2,  5],
              [2, 15, 4, 9]])


def UmnojenMatrc(a, b):
    c = np.matmul(a, b)
    return c


print(str(UmnojenMatrc(a, b)))
