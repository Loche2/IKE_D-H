import numpy as np


def verify_primitive_root(p, g):
    a = np.zeros(g)
    for i in range(1, g):
        print(f"{p}^{i} mod {g} = {(p ** i) % g}")
        k = (p ** i) % g
        if a[k] != 0:
            print("Not Primitive Root Group!")
            return
        else:
            a[k] = a[k] + 1
    print("Primitive Root Group")
    return


verify_primitive_root(6, 251)
