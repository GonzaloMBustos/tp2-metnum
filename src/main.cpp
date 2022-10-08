#include <iostream>

#include "types.h"
#include "utils.h"

//#include "eigen.cpp"
//#include "utils.cpp"

using namespace std;

int main(){
    SparseMatrix mat_karate = read_matrix_karate(); 
    print_sparce_matrix(mat_karate);  
    SparseMatrix ego_facebook = read_ego_facebook(); 
    return 0; 
}


