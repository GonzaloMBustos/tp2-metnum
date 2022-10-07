#pragma once

#include <eigen3/Eigen/Sparse>
#include <eigen3/Eigen/Dense>

using namespace std;
using Eigen::MatrixXd;

typedef Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor> Matrix;
typedef Eigen::SparseMatrix<double> SparseMatrix;

typedef Eigen::VectorXd Vector;

typedef Eigen::Triplet<double> T; //to build sparce matrix 