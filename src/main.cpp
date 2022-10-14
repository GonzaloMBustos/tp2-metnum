#include <iostream>

#include "types.h"
#include "utils.h"
#include "eigen.h"

using namespace std;


int main(){
    
    SparseMatrix mat_karate = read_matrix_karate(); 
    SparseMatrix ego_facebook = read_ego_facebook(); //chequear que esta bien 

    Matrix m {{1, 2, 3}, {0,4, 6}, {0,0, 6}};

    pair<double, Vector> eig = power_iteration(m, 1000, pow(10, -10));
    cout << eig.first << endl;  
    return 0; 
}


