import numpy as np
import metnum as mt

def leer_karateclub(path = "../datasets/karateclub_matriz.txt"):
  M = np.zeros(34*34).reshape(34, 34)
  with open(path,'r') as file:
    # reading each line 
    i = 0
    for line in file:
      line = line.split()
      for j in range(0, len(line)):

        M[i][j] = line[j]
      i+=1
  return M

def test_deflation(M):

    num = M.shape[0]

    epsilon = 1e-8

    (rvals, rvecs) = mt.deflation(M, num, 10000, 1e-10)

    (evals, evecs) = np.linalg.eigh(M)

    rorden = np.argsort(rvals)

    eorden = np.argsort(evals)

    rvals = rvals[rorden]

    rvecs = rvecs[::, rorden]

    evals = evals[eorden]

    evecs = evecs[::, eorden]

    prodinter = np.zeros(num)

    for i in range(num):

        prodinter[i] = abs(np.dot(evecs[::,i], rvecs[::,i]))

    todosunos = np.ones(num)

    return np.allclose(rvals, evals, epsilon),  np.allclose(prodinter, todosunos, epsilon)

def test_power(M):

    num = M.shape[0]

    epsilon = 1e-3

    (rval , rvec) = mt.power_iteration(M, 1000, 1e-10)

    evals = np.linalg.eigvals(M)
    
    evecs = np.linalg.eig(M)[1]

    eorden = np.argsort(evals)[::-1]

    evals = evals[eorden]

    evecs = evecs[::,eorden]

    eval = evals[0]
    evec = evecs[:, 0]

    return abs(rval-eval) < epsilon, np.allclose(abs(np.dot(evec, rvec)), 1, epsilon)
