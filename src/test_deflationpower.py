
import numpy as np
import test_utils as u
import pytest


def test_karate():

    K = u.leer_karateclub()
    test = "karate"
    res_autoval_p, res_autovect_p = u.test_power(K, test)
    assert(res_autoval_p)
    assert(res_autovect_p)

    res_autoval_d, res_autovect_d= u.test_deflation(K, test)
    assert res_autoval_d 
    assert not res_autovect_d 


def test_3x3_base():
    M = np.array([7, 2, 3, 0, 2, 0, -6, -2, -2]).reshape(3,3)
    test = "3x3_base"
    m_autoval_p, m_autovect_p = u.test_power(M@M.T, test)

    assert(m_autoval_p)
    assert(m_autovect_p)

    m_autoval_d, m_autovect_d = u.test_deflation(M@M.T, test)

    assert(m_autoval_d)
    assert(m_autovect_d)

def test_3x3_nobase():
    M = np.array([1, 0, 1, 0, 1, 1, 0, 0, 2]).reshape(3,3)

    test = "3x3_no_base"
    #N = np.transpose(M)
    m_autoval_p, m_autovect_p = u.test_power(M, test)

    assert m_autoval_p
    assert m_autovect_p

    m_autoval_d, m_autovect_d = u.test_deflation(M, test)

    assert not m_autoval_d
    assert not m_autovect_d

def test_3x3_autovals_distintos():
    M = np.array([1, 2, 3, 
                2, 2, 4, 
                3, 4, 4]).reshape(3,3)

    test = "3x3_autovals_distintos"
    m_autoval_p, m_autovect_p = u.test_power(M, test)

    assert(m_autoval_p)
    assert(m_autovect_p)

    m_autoval_d, m_autovect_d = u.test_deflation(M,  test)

    assert(m_autoval_d)
    assert(m_autovect_d)

def test_3x3_autovals_repetidos():
    M = np.array([3, 2, 4, 
                  2, 0, 2, 
                  4, 2, 3]).reshape(3,3)

    test = "3x3_autovals_rep"
    m_autoval_p, m_autovect_p = u.test_power(M,test)
    
    assert(m_autoval_p)
    assert(m_autovect_p)

    m_autoval_d, m_autovect_d = u.test_deflation(M, test)

    assert m_autoval_d
    assert not m_autovect_d

""" 
Este test tiene el problema de que si los autovalores son muy cercanos a 0 o entre si 
luego no los distinguimos bien por comparar con el epsilon y entramos en el caso donde el 
metodo no funciona. 
def test_aleatorio():
    M = np.random.rand(100,100)

    m_autoval_p, m_autovect_p = u.test_power(M@M.T)

    assert(m_autoval_p)
    assert(m_autovect_p)

    m_autoval_d, m_autovect_d = u.test_deflation(M@M.T)

    assert(m_autoval_d)
    assert(m_autovect_d) 

"""