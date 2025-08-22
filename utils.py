import numpy as np

def is_empty(matrix):
    """Check if the matrix is empty."""
    return len(matrix) == 0 or len(matrix[0]) == 0

def augment_matrix(A, B):
    """Augments matrix A with matrix B (horizontally)."""
    check_empty_matrix(A)
    check_empty_matrix(B)
    if len(A) != len(B):
        raise ValueError("Matrices must have the same number of rows to be augmented.")
    return [row_a + row_b for row_a, row_b in zip(A, B)]

def get_index_max_coeff(matrix, col):
    """Finds the coefficient with the largest magnitude in each row."""
    check_empty_matrix(matrix)
    # first row by default
    elem = [e[col] for e in matrix[col:len(matrix)]]
    max_elem = max(elem, key=abs)
    return elem.index(max_elem) + col, max_elem
    # return elem.index(max(elem, key=abs)) + col, max(elem, key=abs)

def matrix_transpose(matrix):
    """Transposes the given matrix."""
    check_empty_matrix(matrix)
    return [list(row) for row in zip(*matrix)]

if __name__ == "__main__":

    ref_matrix = [
        [4,-2,2],
        [-2,2,-4],
        [2,-4,11]
    ]

    print(get_index_max_coeff(ref_matrix, 0))