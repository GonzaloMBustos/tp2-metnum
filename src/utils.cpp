#include "utils.h"

SparseMatrix read_matrix_karate(){
    double epsilon = pow(10, -5);

    ifstream input("../datasets/karateclub_matriz.txt");  
     
    std::vector<T> tripletList;
    tripletList.reserve(156);

    for(int i = 0; i < 34; i++){
        for(int j = 0; j < 34; j++){
            double e;
            input >> e; 
            if(abs(e-1) < epsilon ){
                tripletList.push_back(T(i,j,e));                  
            }
        }
    }

    SparseMatrix mat_karate(34, 34);
    mat_karate.setFromTriplets(tripletList.begin(), tripletList.end());
    return mat_karate; 
}

void print_sparce_matrix(SparseMatrix &m){
    cout<< MatrixXd(m) <<endl;
}


SparseMatrix read_ego_facebook(){
    double epsilon = pow(10, -5);

    ifstream input("../datasets/ego-facebook.edges");  
     
    std::vector<T> tripletList;
    tripletList.reserve(3000);

    for(int i = 0; i < 34; i++){
        for(int j = 0; j < 34; j++){
            double a, b;
            input >> a >> b; 
            tripletList.push_back(T(a,b,1));
        }
    }

    SparseMatrix mat_ego_face(3500, 3500);
    mat_ego_face.setFromTriplets(tripletList.begin(), tripletList.end());
    return mat_ego_face; 
}

void out_eigvalues(Vector eigvals, string path){
    ofstream output(path); 
    for(Vector::iterator it = eigvals.begin(); it != eigvals.end();  it++){
        output << *it; 
    }
}

