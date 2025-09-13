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

    return [np.concatenate((row1,row2), axis=None) for row1, row2 in zip(A,B)]

def get_matrix_shape(matrix):
    """Returns (num_rows, num_cols) for a 2D list (matrix)."""
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    return num_rows, num_cols

def generate_matrix(min, max, row, col):
    return np.random.randint(min, max, size=(row, col))

def generate_invertible_matrix_by_rank(low, high, size):
    while True:
        A = np.random.randint(low, high, (size, size))
        if np.linalg.matrix_rank(A) == size:
            return A

def get_first_nonzero_elem(augmented_matrix, target_row):
    non_zero_indices = np.nonzero(augmented_matrix[target_row])
    if non_zero_indices[0].size > 0:
        return non_zero_indices[0][0]
    return -1

"""
    Pivoting
"""
def get_index_max_coeff(matrix, target_col, row):
    """Finds the coefficient with the largest magnitude in each row in target column."""
    if is_empty(matrix):
        return -1, None

    elem = [e[target_col] for e in matrix[row::]]
    max_elem = max(elem, key=abs)
    if abs(max_elem) < 1.0e-5:
        max_elem = 0
    return elem.index(max_elem) + row, max_elem
    # return elem.index(max(elem, key=abs)) + col, max(elem, key=abs)

def matrix_transpose(matrix):
    """Transposes the given matrix."""
    if is_empty(matrix):
        return []
    return [list(row) for row in zip(*matrix)]

def main():
    # ref_matrix = [
    #     [4,-2,2],
    #     [-2,2,-4],
    #     [2,-4,11]
    # ]
    # b = [
    #     [4],
    #     [0],
    #     [-5]
    # ]

    ref_matrix = [
        [1,3,-5,1,5],
        [1,4,-7,3,-2],
        [1,5,-9,5,-9],
        [0,3,-6,2,-1]
    ]
    b = [
        [0],
        [0],
        [0],
        [0]
    ]

    print(get_index_max_coeff(ref_matrix, b))

if __name__ == "__main__":
    main()
