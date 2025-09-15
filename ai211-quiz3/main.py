import sys
import numpy as np
import scipy.linalg
from algorithms import *
from utils import *

def main(args):

    ref_A = generate_random_invertible_matrix(200)
    # print(f"A =\n {np.array(ref_A)}")

    # ref_A, _ = test_data.get_test_data_1()
    # print(f"A =\n {np.array(ref_A)}")

    result, det_factors = gaussian_elimination_with_pivot(ref_A)
    A = np.array(result.copy())

    # print(np.array(A))

    # print(np.array(det_factors))
    determinant = 1.

    for d in det_factors:
        determinant *= d

    print(f"Determinant using EROs: {round(determinant, 5)}")

    det_scipy = round(scipy.linalg.det(ref_A), 5)
    print(f"Determinant from scipy: {det_scipy}")

if __name__ == "__main__":
    main(sys.argv)
