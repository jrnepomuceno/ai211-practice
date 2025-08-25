import numpy as np  # for formatting and splicing
from utils import *
import functools

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


def back_substitution(A, b, row, values = [None] * len(b)):

    if(is_empty(A)):
        return 0
    
    if(values[row] != None):
        return values

    ref_A_row = A[0]
    ref_b = b[0][0]
    # print(ref_A_row)
    # print(ref_b)

    values[row] = (ref_b - sum([(back_substitution(A[1:,1:], b[1:,:], row+ith+1, values)[row+ith+1]) * np.array(c) for ith, c in enumerate(ref_A_row[1:])])) / ref_A_row[0]

    return np.array(values)

def solve_mult_E(collection_E, A, b):

    matrix_E = np.array(collection_E)
    # print(np.array(matrix_E))

    product_Em = b

    for E in matrix_E:
        product_Em = E @ product_Em
        # print(np.array(product_EA))

    print(np.array(product_Em))

    # matrix_Eb = product_EA @ b
    # print(matrix_Eb)

    # result = product_E @ matrix_Ab

    # print(np.array(result))

def print_values(values):
    for index, value in enumerate(np.array(values)):
        print(f"x{index+1} = {value}")

if __name__ == "__main__":
    values = back_substitution(A, b, 0)
    for index, value in enumerate(np.array(values)):
        print(f"x{index+1} = {value}")