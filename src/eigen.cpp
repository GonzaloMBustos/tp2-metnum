#include <algorithm>
#include <chrono>
#include <iostream>
#include "eigen.h"

using namespace std;

namespace py=pybind11;

// Matriz, dinámica, de tamaño arbitrario (X), con elementos del tipo Double(D)
using Eigen::MatrixXd;

// Matriz de numero de filas arbitrario (X) , de 1 columna y con elementos del 
//tipo Double(D)
using Eigen::VectorXd;

pair<double, Vector> power_iteration(const Matrix &X, unsigned niter, double eps)
{
	Eigen::VectorXd b = Vector::Random(X.cols());
	bool break_crit = false;

	for (int i = 0; i < niter && !break_crit; i++)
	{
		Eigen::VectorXd new_b = X * b;
		new_b = new_b / new_b.norm();
		double cos_angle = new_b.transpose() * b;
		break_crit = (1 - eps) < cos_angle && cos_angle <= 1;
		b = new_b;
	}

	double eigval = b.transpose() * X * b;
	return make_pair(eigval, b);
}

pair<Vector, Matrix> deflation(const Matrix &X, unsigned num, unsigned num_iter, double epsilon)
{
	Matrix A;
	A = X;
	Eigen::VectorXd eigvalues(num);
	Eigen::MatrixXd eigvectors(A.rows(), num);

	double a = 0;
	Eigen::VectorXd v = Vector::Zero(A.rows());
	for (int i = 0; i < num; i++)
	{
		A = A - (a * v * v.transpose());
		tie(a, v) = power_iteration(A, num_iter, epsilon);
		eigvalues[i] = a;
		eigvectors.col(i) = v;
	}
	return make_pair(eigvalues, eigvectors);
}

void print_hey(){
	cout << "HEY" <<endl; 
}

void print_bye(){
	cout << "BYE" <<endl; 
}

PYBIND11_MODULE(lib_tp2, m) {
    m.def(
        "power_iteration", &power_iteration,
        "doingthings"
    );
	m.def(
		"deflation", &deflation,
		"deflation"
	);
	m.def(
		"print_hey",  &print_hey,
		"print hey"
	);
	
}