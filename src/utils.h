#pragma once


#include <fstream> //Para leer el archivo
#include <iomanip> //Para setear la precision de la salida
#include<chrono> //Por el tiempo
#include <cassert> //Para los assert
#include <filesystem> // Para obtener los nombres de los archivos
#include <math.h>
#include <iostream>

#include "types.h"


SparseMatrix read_matrix_karate(); 
void print_sparce_matrix(SparseMatrix &m);  
SparseMatrix read_ego_facebook();

