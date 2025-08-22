import sys
from eros import *
from utils import augment_matrix
import numpy as np  # for printing only

def main(args):
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

    print("Reference:")
    print(np.array(augmented_matrix))
    print()
    for col in range(cols-1):
        index, max_coeff = get_index_max_coeff(augmented_matrix, col)
        print(f"Column {col}: Max coefficient {max_coeff} at row {index}")
        if index != col:
            # perform swap
            augmented_matrix = erosI(augmented_matrix, col, index)
            print(f"Swapped rows {col} and {index}:")
            print(np.array(augmented_matrix))
        if(augmented_matrix[col][col] != 1 or augmented_matrix[col][col] != 0):
            # perform reduction
            augmented_matrix = erosII(augmented_matrix, col)
            print(f"Scaled row {col} to make leading coefficient 1:")
            print(np.array(augmented_matrix))
        # perform elimination
        if col < (cols-2):  # Avoid last column of A
            for row in range(col+1, rows):
                if row != col:
                    factor = augmented_matrix[row][col] / augmented_matrix[col][col]
                    augmented_matrix = erosIII(augmented_matrix, col, row, factor)
                    print(f"Eliminated column {col} in row {row}:")
                    print(np.array(augmented_matrix))

if __name__ == "__main__":
    main(sys.argv)