from utils import *

# switch_rows
def erosI(A, row1, row2):
    assert not is_empty(A)
    A_copy = A.copy()
    A_copy[row1], A_copy[row2] = A[row2], A[row1]
    return A_copy

# scalar multiplication / row reduction
def erosII(A, target_row, target_column, leading_coefficient):
    assert not is_empty(A)
    # efficiency: only process elements in col >= target_col, concatenate to elements in col < target_col after
    new_row = []
    for element in A[target_row][target_column::]:
        temp = round((element / leading_coefficient), 5)
        if abs(temp) <= 1.0e-5:
            temp = 0
        new_row.append(temp)

    A[target_row] = [*A[target_row][0:target_column],*new_row]
    return A

# elimination
def erosIII(A, ref_row, target_row, target_column, scalar):
    assert not is_empty(A)
    # efficiency: only process elements in col >= target_col, concatenate to elements in col < target_col after
    scalar = round(scalar, 5)
    new_row = []

    for a, b in zip(A[target_row][target_column::], A[ref_row][target_column::]):
        temp = round(a + (b * (-1*scalar)), 5)
        if abs(temp) <= 1.0e-5:
            temp = 0
        new_row.append(temp)

    # A[target_row] = [*A[target_row][0:target_column],
    #                  *[round(a + (b * (-1*scalar)), 5) for a, b in zip(A[target_row][target_column::], A[ref_row][target_column::])]]
    A[target_row] = [*A[target_row][0:target_column],*new_row]
    return A

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

if __name__ == "__main__":
    main()