

def check_empty_matrix(matrix):
    """Check if the matrix is empty."""
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise ValueError("Matrix cannot be empty.")
    

def augment_matrix(A, B):
    """Augments matrix A with matrix B (horizontally)."""
    check_empty_matrix(A)
    check_empty_matrix(B)
    if len(A) != len(B):
        raise ValueError("Matrices must have the same number of rows to be augmented.")
    return [row_a + row_b for row_a, row_b in zip(A, B)]