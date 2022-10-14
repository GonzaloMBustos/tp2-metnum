import metnum as mt
import numpy as np

def leer_karateclub(path = "../karateclub_matriz.txt"):
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

if __name__ == '__main__':
    A = leer_karateclub("../datasets/karateclub_matriz.txt")
    a, e = mt.power_iteration(A.astype(float), 1000, 0.001)
    print(e)

