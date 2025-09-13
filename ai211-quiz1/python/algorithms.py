from utils import *
from eros import *
import equations as equations
from decorators import timing_decorator
import time

"""
Naive Gaussian Elimination

"""
@timing_decorator
def naive_gaussian_elimination_with_pivoting(ref_matrix, b):

    start_time = time.perf_counter()

    augmented_matrix = augment_matrix(ref_matrix.copy(), b.copy())
    # print(f"matrix A|b: \n{np.array(augmented_matrix)}")
    rows, cols = get_matrix_shape(augmented_matrix)
    if rows == 0 or cols == 0:
        print("The matrix is empty.")

    # print("Reference:")
    # print(np.array(augmented_matrix))
    for col in range(cols-1):
        index, max_coeff = get_index_max_coeff(augmented_matrix, col)
        # print(f"Column {col}: Max coefficient {max_coeff} at row {index}")
        if index != col:
            # perform swap
            augmented_matrix = erosI(augmented_matrix, col, index)
            # print(f"Swapped rows {col} and {index}:")
            # print(np.array(augmented_matrix))

        # perform reduction
        leading_coefficient = augmented_matrix[col][col]
        if(leading_coefficient != 1 or leading_coefficient != 1.0):
            augmented_matrix = erosII(augmented_matrix, col, leading_coefficient)
            # print(f"Scaled row {col} to make leading coefficient 1:")
            # print(np.array(augmented_matrix))

        # perform elimination
        if col < (cols-2):  # Avoid last column of A
            for row in range(col+1, rows):
                if row != col:
                    factor = augmented_matrix[row][col] / augmented_matrix[col][col]
                    augmented_matrix = erosIII(augmented_matrix, col, row, factor)
                    # print(f"Eliminated column {col} in row {row}:")
                    # print(np.array(augmented_matrix))

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    return np.array(augmented_matrix), elapsed_time

"""
Get values using Elementary Matrix Multiplication
"""
# TODO: Optimize Matrix multiplication
# @timing_decorator
def gaussian_elimination_two(ref_matrix, b):
    start_time = time.perf_counter()

    augmented_matrix = augment_matrix(ref_matrix.copy(), b.copy())
    rows, cols = get_matrix_shape(augmented_matrix)
    if rows == 0 or cols == 0:
        print("The matrix is empty.")

    # print("Reference:")
    # print(np.array(augmented_matrix))

    for col in range(cols-1):
        index, max_coeff = get_index_max_coeff(augmented_matrix, col)
        # print(f"Column {col}: Max coefficient {max_coeff} at row {index}")
        if index != col:
            # perform swap
            E = generate_EI(col, index, len(augmented_matrix))
            # print(np.array(E))
            augmented_matrix = E @ augmented_matrix
            # print(f"Swapped rows {col} and {index}:")
            # print(np.array(augmented_matrix))

        # perform reduction
        leading_coefficient = augmented_matrix[col][col]
        if(leading_coefficient != 1 or leading_coefficient != 1.0 or leading_coefficient != 0):
            m = 1. / leading_coefficient
            # print(m)
            E = generate_EII(col, m, len(augmented_matrix))
            augmented_matrix = E @ augmented_matrix
            # print(f"Scaled row {col} to make leading coefficient 1:")
            # print(np.array(augmented_matrix))

        # perform elimination
        if col < (cols-2):  # Avoid last column of A and augmented_matrix: b
            for row in range(col+1, rows):
                if row != col:
                    factor = augmented_matrix[row][col] / augmented_matrix[col][col]
                    E = generate_EIII(col, row, factor, len(augmented_matrix))
                    # print(np.array(E))
                    augmented_matrix = E @ augmented_matrix
                    # print(f"Eliminated column {col} in row {row}:")
                    # print(np.array(augmented_matrix))

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    return np.array(augmented_matrix), elapsed_time

if __name__ == "__main__":

    # ref_matrix = [
    #     [1.,0.5,-0.5,1.],
    #     [-0.,1.,-3.33333333,2.33333333],
    #     [0.,0.,1.,-1.]
    #     ]
    
    ref_matrix = [
        [4,-2,2,4],
        [-2,2,-4,0],
        [2,-4,11,-5]
    ]

    ref_b = [
        [4],
        [0],
        [-5]
    ]

    A = [c[:-1] for c in ref_matrix]
    b = [[]] * len(A)
    for index, row in enumerate(ref_matrix):
        b[index] = [row[-1]]

    values = gaussian_elimination_two(A, b)
    print(np.array(values))