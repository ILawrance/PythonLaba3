import numpy as np

k = np.array([[2, 4.1, 2], [4, -1, 6.5]])
z = float(input("z= "))


def Umnoj_Na_Skalyar(k, z):
    c = k*z
    print("K *%4d = " % (z) + str(c))


Umnoj_Na_Skalyar(k, z)