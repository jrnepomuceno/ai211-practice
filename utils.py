import numpy as np

def is_empty(matrix):
    """Check if the matrix is empty."""
    return len(matrix) == 0

def augment_matrix(A, B):
    """Augments matrix A with matrix B (horizontally)."""
    if is_empty(A) or is_empty(B):
        return []

    if len(A) != len(B):
        raise ValueError("Matrices must have the same number of rows to be augmented.")

    return [row1 + row2 for row1, row2 in zip(A,B)]


def get_index_max_coeff(matrix, col):
    """Finds the coefficient with the largest magnitude in each row."""
    if is_empty(matrix):
        return []
    # first row by default
    elem = [e[col] for e in matrix[col:len(matrix)]]
    max_elem = max(elem, key=abs)
    return elem.index(max_elem) + col, max_elem
    # return elem.index(max(elem, key=abs)) + col, max(elem, key=abs)

def matrix_transpose(matrix):
    """Transposes the given matrix."""
    if is_empty(matrix):
        return []
    return [list(row) for row in zip(*matrix)]

if __name__ == "__main__":

    ref_matrix = [
        [4,-2,2],
        [-2,2,-4],
        [2,-4,11]
    ]
    b = [
        [4],
        [0],
        [-5]
    ]
    print(get_index_max_coeff(ref_matrix, b))