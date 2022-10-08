#include <iostream>

#include "types.h"
#include "utils.h"

//#include "eigen.cpp"
//#include "utils.cpp"

using namespace std;

int main(){
    //SparseMatrix mat_karate = read_matrix_karate(); 
    //SparseMatrix ego_facebook = read_ego_facebook(); //chequear que esta bien 

    Matrix v {{1, 2, 3}, {5,4, 6}};
    out_eigvectors(v, ".out/autovect.out"); 
    return 0; 
}


