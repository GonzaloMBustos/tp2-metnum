import metnum as mt

import numpy as np

import pytest


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

    epsilon = 1e-8

    (rval , rvec) = mt.power_iteration(M, 1000, 1e-10)

    eval = np.linalg.eigvals(M)[0]

    evec = np.linalg.eig(M)[1][:,0]

    return np.allclose(rval, eval, epsilon), np.allclose(abs(np.dot(evec, rvec)), 1, epsilon)


def test_karate():

    K = leer_karateclub()

    res_autoval, res_autovect = test_power(K)
    assert(res_autoval)
    assert(res_autovect)
    res_autoval, res_autovect = test_deflation(K)
    assert(res_autoval)
    assert(res_autovect)


def test_aleatorio():
    M = np.random.rand(100,100)

    #N = np.transpose(M)
    m_autoval, m_autovect = test_power(M)

    assert(m_autoval)
    assert(m_autovect)

    m_autoval, m_autovect = test_deflation(M)

    assert(m_autoval)
    assert(m_autovect)

def test_3x3_base():
    M = np.array([7, 2, 3, 0, 2, 0, -6, -2, -2]).reshape(3,3)

    #N = np.transpose(M)
    m_autoval, m_autovect = test_power(M)

    assert(m_autoval)
    assert(m_autovect)

    m_autoval, m_autovect = test_deflation(M)

    assert(m_autoval)
    assert(m_autovect)

def test_3x3_nobase():
    M = np.array([1, 0, 1, 0, 1, 1, 0, 0, 2]).reshape(3,3)

    #N = np.transpose(M)
    m_autoval, m_autovect = test_power(M)

    assert(m_autoval)
    assert(m_autovect)

    m_autoval, m_autovect = test_deflation(M)

    assert(m_autoval)
    assert(m_autovect)
##MAIN 

test_3x3_base()
test_3x3_nobase()

print("test aleatorio")
test_aleatorio()

print("test_karate")
test_karate()

