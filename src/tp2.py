import lib_tp2
import numpy as np
if __name__ == '__main__':
    M = np.array([1, 2, 3, 0, 2, 3, 0, 0, 3]).reshape(3, 3)
    #M = mylib.add_one(M)
    lib_tp2.print_hey()
    print(lib_tp2.power_iteration(M, 1000, 0.0001))

    print("WORKING :)")
