import sys
import numpy as np
from algorithms import *
from utils import *
import test_data

def main(args):

    # matrix_size = size
    # low_A, high_A = args.loA, args.hiA
    # low_b, high_b = args.lob, args.hib

    results = []
    """
    At least 10 runs for each sample
    """

    # ref_A, ref_b = test_data.get_test_data_1()
    ref_A, ref_b = test_data.get_test_data_5()

    result, elapsed_t = gauss_jordan_elimination(ref_A, ref_b)

    A, b = np.array(result[:,:-1].copy()), np.array(result[:,-1:].copy())

    print("A:")
    print(np.array(A))
    print("b:")
    print(np.array(b))
    # """
    # Get values using Back Substitution
    # """
    # values = back_substitution(A, b)
    # results.append((f"{elapsed_t:.9f}"))

    print("Solution: ")
    for equation in evaluate_equation(A, b):
        print(equation)

    # return results

if __name__ == "__main__":
    main(sys.argv)
