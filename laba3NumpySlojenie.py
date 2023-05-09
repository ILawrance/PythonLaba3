import numpy as np

a = np.array([[2.3, 3, 7], [11.7, 2.1, 1], [-3, -10.1, 2]])
b = np.array([[-1, -1.5, 2], [2.9, 3.4, 5], [4.5, -4.4, 6]])


def Slojenie_And_Vichitanie(a, b):
    c = a + b
    v = a - b
    print("A + B = " + str(c), end="\n \n")
    print("A - B = " + str(v))


Slojenie_And_Vichitanie(a, b)

