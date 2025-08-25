from utils import *
from eros import *
import equations
from decorators import timing_decorator

"""
Naive Gaussian Elimination

"""
@timing_decorator
def naive_gaussian_elimination(ref_matrix, b):

    augmented_matrix = augment_matrix(ref_matrix, b)
    rows, cols = get_matrix_shape(augmented_matrix)
    if rows == 0 or cols == 0:
        print("The matrix is empty.")

    # print("Reference:")
    # print(np.array(augmented_matrix))
    print()
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

    result = np.array(augmented_matrix)

    new_A = result[:,:-1]
    new_b = result[:,-1:]

    """
    Get values using Back Substitution
    """
    values = equations.back_substitution(new_A, new_b, 0)

    return values

"""
Get values using Elementary Matrix Multiplication
"""
@timing_decorator
def gaussian_elimination_two(ref_matrix, b):

    augmented_matrix = augment_matrix(ref_matrix, b)
    saved_aug_matrix = augmented_matrix.copy()
    rows, cols = get_matrix_shape(augmented_matrix)
    if rows == 0 or cols == 0:
        print("The matrix is empty.")

    # print("Reference:")
    # print(np.array(augmented_matrix))
    print()

    I = np.identity(rows)
    # print(I)
    E_collection = []

    for col in range(cols-1):
        index, max_coeff = get_index_max_coeff(augmented_matrix, col)
        # print(f"Column {col}: Max coefficient {max_coeff} at row {index}")
        if index != col:
            # perform swap
            E = erosI(I.copy(), col, index)
            # print(np.array(E))
            augmented_matrix = E @ augmented_matrix
            # print(f"Swapped rows {col} and {index}:")
            # print(np.array(augmented_matrix))
            # print(np.array(E_collection))

        # perform reduction
        leading_coefficient = augmented_matrix[col][col]
        if(leading_coefficient != 1 or leading_coefficient != 1.0 or leading_coefficient != 0):
            E = erosII(I.copy(), col, leading_coefficient)
            augmented_matrix = E @ augmented_matrix
            # print(f"Scaled row {col} to make leading coefficient 1:")
            # print(np.array(augmented_matrix))
            # print(np.array(E_collection))

        # perform elimination
        if col < (cols-2):  # Avoid last column of A
            for row in range(col+1, rows):
                if row != col:
                    factor = augmented_matrix[row][col] / augmented_matrix[col][col]
                    E = erosIII(I.copy(), col, row, factor)
                    # print(np.array(E))
                    augmented_matrix = E @ augmented_matrix
                    # print(f"Eliminated column {col} in row {row}:")
                    # print(np.array(augmented_matrix))
                    # print(np.array(E_collection))


    result = np.array(augmented_matrix)

    new_A = result[:,:-1]
    new_b = result[:,-1:]

    """
    Get values using Back Substitution
    """
    values = equations.back_substitution(new_A, new_b, 0)
    return values

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

    values = gaussian_elimination_two(A, b)
    print(np.array(values))