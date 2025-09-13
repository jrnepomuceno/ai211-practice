from eros import *
from decorators import timing_decorator
import time

#@timing_decorator
def ge_with_pivoting_general_sle(ref_matrix, b):

    augmented_matrix = augment_matrix(ref_matrix.copy(), b.copy())

    rows, cols = get_matrix_shape(augmented_matrix)
    if rows == 0 or cols == 0:
        print("The matrix is empty.")

    zero_cols = []

    for row in range(rows):

        if get_first_nonzero_elem(augmented_matrix, row) == -1:
            # if last row, finish
            if(row == rows-1):
                break

        for col in range(cols-1):

            if(row <= col):               
                index_wmax, max_coeff = get_index_max_coeff(augmented_matrix, col, row)
                """
                If max_coeff is zero, (means no leading non-zero element in column), goto next column
                """
                if(max_coeff == 0.):                 
                    zero_cols.append((row, col))
                    continue

                if index_wmax != row:
                    # perform swap
                    augmented_matrix = erosI(augmented_matrix, row, index_wmax)

                # perform reduction
                leading_coefficient = augmented_matrix[row][col]
                if(leading_coefficient != 1 or leading_coefficient != 1.0):
                    augmented_matrix = erosII(augmented_matrix, row, col, leading_coefficient)

                # perform elimination
                if col < (cols-1):
                    for elim_row in range(row+1, rows):
                        factor = augmented_matrix[elim_row][col] #/ augmented_matrix[row][col]
                        augmented_matrix = erosIII(augmented_matrix, row, elim_row, col, factor)

                break

    return np.array(augmented_matrix), zero_cols

# @timing_decorator
def gauss_jordan_elimination(ref_A, ref_b):

    start_time = time.perf_counter()

    # Gaussian Elimination with Pivoting
    result, zero_rows = ge_with_pivoting_general_sle(ref_A, ref_b)

    A, b = np.array(result[:,:-1].copy()), np.array(result[:,-1:].copy())

    augmented_matrix = augment_matrix(A, b)
    rows, cols = get_matrix_shape(augmented_matrix)
    if rows == 0 or cols == 0:
        print("The matrix is empty.")

    # Reduction Phase
    for row in range(rows-1, 0, -1):
        for col in range(cols-1,0,-1):
            coeff = augmented_matrix[row][col]
            if coeff != 1.:
                continue

            # perform elimination
            if col < (cols-1): 
                for elim_row in range(0, row):
                    factor = round(augmented_matrix[elim_row][col], 5) # / augmented_matrix[row][col]
                    augmented_matrix = erosIII(augmented_matrix, row, elim_row, col, factor)

            break

    augmented_matrix = [[round(elem, 2) for elem in row] for row in augmented_matrix]

    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time)

    return np.array(augmented_matrix), elapsed_time
    

def evaluate_equation(A, b):

    equations = []

    for row in range(len(A)):
        equation = ""

        """
        For RREF, rows with only zeroes as elements mean end of rows has been reached
        """
        offset = get_first_nonzero_elem(A, row)
        if offset == -1:
            break

        num_terms = 0
        for col in range(offset, len(A[row])):

            coeff = round(A[row][col], 5)

            if col == offset:
                equation += f"x{col+1} ="
                equation += f" {b[row]}"
                num_terms += 1
                continue
            else:
                if coeff != 0.:
                    if num_terms > 0:
                        equation += " -"
                    if coeff == 1.:
                        equation += f" x{col+1}"
                        num_terms += 1
                    else:
                        equation += f" ({coeff})x{col+1}"
                        num_terms += 1
                else:
                    continue

        equations.append(equation)


    return equations