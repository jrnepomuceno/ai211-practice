from utils import *

# switch_rows
def erosI(A, row1, row2):
    check_empty_matrix(A)
    A[row1], A[row2] = A[row2], A[row1]

# scalar multiplication
def erosII(A, target_row, scalar):
    check_empty_matrix(A)
    A[target_row] = [element * scalar for element in A[target_row]]

# elimination
def erosIII(A, ref_row, target_row, scalar):
    check_empty_matrix(A)
    A[target_row] = [a - b * scalar for a, b in zip(A[target_row], A[ref_row])]
    # Note: This is a simplified version and may not cover all edge cases.

def main():

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
    augmented_matrix = augment_matrix(ref_matrix, b)
    rows, cols = get_matrix_shape(augmented_matrix)
    if rows == 0 or cols == 0:
        print("The matrix is empty.")

    print(augmented_matrix)

def get_matrix_shape(matrix):
    """Returns (num_rows, num_cols) for a 2D list (matrix)."""
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    return num_rows, num_cols

if __name__ == "__main__":
    main()