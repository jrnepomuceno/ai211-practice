from utils import *

# switch_rows
def erosI(A, row1, row2):
    assert not is_empty(A)
    A_copy = A.copy()
    A_copy[row1], A_copy[row2] = A[row2], A[row1]
    return A_copy

# scalar multiplication / row reduction
def erosII(A, target_row, leading_coefficient):
    assert not is_empty(A)
    A[target_row] = [(element / float(leading_coefficient)) for element in A[target_row]]
    return A

# elimination
def erosIII(A, ref_row, target_row, scalar):
    assert not is_empty(A)
    A[target_row] = [a + (b * (-1*scalar)) for a, b in zip(A[target_row], A[ref_row])]
    return A


def generate_EI(row1, row2, n):
    E = np.eye(n)
    E[row2][row1] = 1
    E[row1][row2] = 1
    E[row1][row1] = 0
    E[row2][row2] = 0
    return E

# scalar multiplication / row reduction
def generate_EII(target_row, m, n):
    E = np.eye(n)
    E[target_row][target_row] = m
    return E

# elimination
def generate_EIII(ref_row, target_row, m, n):
    E = np.eye(n)
    E[target_row][ref_row] = -1*(m)
    # print(np.array(E))
    return E

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

    print(np.array(generate_EI(0,2,len(augmented_matrix))))

    print(augmented_matrix)

def get_matrix_shape(matrix):
    """Returns (num_rows, num_cols) for a 2D list (matrix)."""
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    return num_rows, num_cols

if __name__ == "__main__":
    main()