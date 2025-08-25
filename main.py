import sys
from eros import *
from algorithms import naive_gaussian_elimination, improved_gaussian_elimination
from equations import print_values
import numpy as np  # for formatting only


def main(args):

    ref_A = [
        [4,-2,2],
        [-2,2,-4],
        [2,-4,11]
    ]

    ref_b = [
        [4],
        [0],
        [-5]
    ]

    values_1 = naive_gaussian_elimination(ref_A, ref_b)
    print_values(values_1)

    values_2 = improved_gaussian_elimination(ref_A, ref_b)
    print_values(values_2)

if __name__ == "__main__":
    main(sys.argv)