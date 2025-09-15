from utils import *
from eros import *
import time

def gaussian_elimination_with_pivot(ref_matrix):
    start_time = time.perf_counter()

    # augmented_matrix = augment_matrix(ref_matrix.copy(), b.copy())
    A = ref_matrix.copy()

    rows, cols = get_matrix_shape(A)
    if rows == 0 or cols == 0:
        print("The matrix is empty.")

    zero_cols = []
    det_factors = []

    for row in range(rows):

        if get_first_nonzero_elem(A, row) == -1:
            if(row == rows):
                break

        for col in range(cols):

            if(row <= col):               
                index_wmax, max_coeff = get_index_max_coeff(A, col, row)
                """
                If max_coeff is zero, (means no leading non-zero element in column), goto next column
                """
                if(max_coeff == 0.):                 
                    zero_cols.append((row, col))
                    continue

                if index_wmax != row:
                    # perform swap
                    A, e = erosI(A, row, index_wmax)
                    det_factors.append(e)

                # perform reduction
                leading_coefficient = A[row][col]
                if(leading_coefficient != 1 or leading_coefficient != 1.0):
                    A, m = erosII(A, row, col, leading_coefficient)
                    det_factors.append(m)

                # perform elimination
                for elim_row in range(row+1, rows):
                    factor = A[elim_row][col] #/ augmented_matrix[row][col]
                    A = erosIII(A, row, elim_row, col, factor)

                break

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    return np.array(A), det_factors

if __name__ == "__main__":
   
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

    print(np.array(values))