import numpy as np  # for formatting and splicing
from utils import *
import functools
import time

ref_matrix = np.array([
    [1.,0.5,-0.5,1.],
    [-0.,1.,-3.33333333,2.33333333],
    [0.,0.,1.,-1.]
    ])

A, b = ref_matrix[:,:-1], ref_matrix[:,-1:]

def print_matrix(A, b):
    """Prints the matrix using numpy for better formatting."""
    print("A:")
    print(np.array(A))
    print("b:")
    print(np.array(b))

def print_equation(A, b):
    """Prints the equation Ax = b."""
    A = A[::-1]
    b = b[::-1]
    print_matrix = []
    for i in range(len(b)):
        exp = len(b)-i
        eq = " + ".join(f"{A[i,j]}x{exp+(j-exp)+1}" for j in range(len(A[i])) if A[i,j] != 0)
        print_matrix.append(f"{eq} = {b[i,0]}")

    for line in print_matrix:
        print(line)

def back_substitution(A, b):

    values = [None] * len(b)

    if(is_empty(A)):
        return values

    for row in range(len(A)-1, -1, -1):
        # print(f"row{row}: {A[row][row]}")
        if A[row][row] == 0:
            b[row][0] = 0
            continue

        # print(f"target_coeff: {A[row][row]}")
        coeff_b = np.round(b[row][0] / A[row][row], 5)
        # print(coeff_b)
        if abs(coeff_b) < 1.0e-5:
            coeff_b = 0
        b[row][0] = coeff_b
        if row < len(A)-1:
            temp = [A[row][e] * b[row+1][0] for e in range(len(A)-1,row,-1)]
            print(temp)
            b[row][0] = b[row][0] - sum(temp)

    return np.array(b)

def print_values(values):
    for index, value in enumerate(np.array(values)):
        print(f"x{index+1} = {value[0]:.5e}")

def print_values_T(values):
    for index, value in enumerate(np.array(values)):
        value = np.array(value)
        print(f"x{index+1} = {value:.5e}")

if __name__ == "__main__":

    ref_matrix = [
        [1.,0.5,-0.5,1.],
        [-0.,1.,-3.33333333,2.33333333],
        [0.,0.,1.,-1.]
        ]

    A = [c[:-1] for c in ref_matrix]
    b = [[]] * len(A)
    for index, row in enumerate(ref_matrix):
        b[index] = [row[-1]]

    values = back_substitution(A, b)
    print_values(values)