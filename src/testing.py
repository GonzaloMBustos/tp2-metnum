import metnum as mt
import numpy as np


def test_deflation(M):
    num = M.shape[0]
    epsilon = 0.00000001


    (rvals, rvecs) = mt.deflation(M, num, 10000, 0.000000001)
    (evals, evecs) = np.linalg.eigh(M)

    rorden = np.argsort(rvals)
    eorden = np.argsort(evals)

    rvals = rvals[rorden]
    rvecs = rvecs[::, rorden]
    evals = evals[eorden]
    evecs = evecs[::, eorden]

    print(np.allclose(rvals, evals, epsilon))
    prodinter = np.zeros(num)
    for i in range(num):
        prodinter[i] = abs(np.dot(evecs[::,i], rvecs[::,i]))
    todosunos = np.ones(num)
    print(np.allclose(prodinter, todosunos, epsilon))

def test_power(M):
    num = M.shape[0]
    epsilon = 1e-8

    (rval , rvec) = mt.power_iteration(O, 1000, 1e-10)
    eval = np.linalg.eigvals(M)[0]
    evec = np.linalg.eig(M)[1][:,0]
    
    print(np.allclose(rval, eval, epsilon))
    print(np.allclose(abs(np.dot(evec, rvec)), 1, epsilon))


if __name__ == '__main__':
    M = np.random.rand(5,5)
    #M = np.array([1,2,3,7,8,9,4,5,6]).reshape(3, 3)
    N = np.transpose(M)
    O = M + N
    print(1)
    test_power(O)
    #test_deflation(O)

