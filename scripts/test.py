import numpy as np


def test():
    a = np.zeros(10)
    a[0] = 1
    print(a[a != np.zeros(1)])


if __name__ == "__main__":
    test()
