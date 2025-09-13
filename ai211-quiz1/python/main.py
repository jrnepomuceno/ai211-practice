import sys
from eros import *
from algorithms import naive_gaussian_elimination_with_pivoting, gaussian_elimination_two
from equations import print_values, print_values_T
import equations
import numpy as np
import csv
import argparse

def generate_matrix(min, max, row, col):
    return np.random.randint(min, max, size=(row, col))

def generate_invertible_matrix_by_rank(low, high, size):
    while True:
        A = np.random.randint(low, high, (size, size))
        if np.linalg.matrix_rank(A) == size:
            return A

def run_sample(args, size):

    matrix_size = size
    low_A, high_A = args.loA, args.hiA
    low_b, high_b = args.lob, args.hib

    results = []
    """
    At least 10 runs for each sample
    """
    for c in range(0, 1):
        ref_A = generate_invertible_matrix_by_rank(low_A, high_A, matrix_size)
        # print(np.array(ref_A))

        ref_b = generate_matrix(0, high_b, matrix_size, 1)
        # print(np.array(ref_b))

        ref_A = [
            [1,3,-5,1,5],
            [1,4,-7,3,-2],
            [1,5,-9,5,-9],
            [0,3,-6,2,-1]
        ]
        ref_b = [
            [0],
            [0],
            [0],
            [0]
        ]

        print(f"Performing Naive GE ({c})...")
        result_1, elapsed_t1 = naive_gaussian_elimination_with_pivoting(ref_A, ref_b)
        print(f"Performing GE with Elementary matrices ({c})...")
        result_2, elapsed_t2 = gaussian_elimination_two(ref_A, ref_b)
        # print(np.array(result))

        A1, b1 = np.array(result_1[:,:-1].copy()), np.array(result_1[:,-1:].copy())
        A2, b2 = np.array(result_2[:,:-1].copy()), np.array(result_2[:,-1:].copy())
        """
        Get values using Back Substitution
        """
        values_1 = equations.back_substitution(A1, b1)
        # print_values(values_1)
        values_2 = equations.back_substitution(A2, b2)
        # print_values(values_2)

        # print(f"Naive Gaussian Elimination time elapsed: {elapsed_t1:.9f} s")
        # print(f"Gaussian Elimination w/ Elem Matrices time elapsed: {elapsed_t2:.9f} s")
        results.append((f"{elapsed_t1:.9f}", f"{elapsed_t2:.9f}"))

    # print(results)

    """
    Checking Consistency of answers
    """
    for index, (v1, v2) in enumerate(zip(values_1, values_2, strict=True)):
        if np.allclose(v1, v2, rtol=1e-05, atol=1e-08):
            pass
        else:
            print(f"x{index} is not equal: {v1} {v2}")

    return results

def main(args):

    matrix_size = args.size
    low_A, high_A = args.loA, args.hiA
    low_b, high_b = args.lob, args.hib

    results_map = {}
    # matrices_size_list = [2 ** c for c in range(3, 10)]
    matrices_size_list = [2]

    # print(matrices_size_list)
    # return 0

    """
    Run with different sizes
    """
    for size in matrices_size_list:
        print(f"Running Gaussian Elimination experiment for size: {size}")
        results = run_sample(args, size)
        results_map[size] = results

    # for key, val in results_map.items():
    #     print(f'{key} {val}')

    with open(f'../results/nge-vs-gewem_range_{low_A}_to_{high_A}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        header_row = [' ']
        ne_data = [None] * 10
        gewem_data = [None] * 10
        for key, val in results_map.items():
            header_row.append(key)
            ne_data, gewem_data = process_key_val(key, val, ne_data, gewem_data)

        # print(f'ne_data: {index} {ne_data}\n')
        # print(f'gewem_data: {index} {gewem_data}\n')
        writer.writerow(header_row)
        writer.writerows(ne_data)
        writer.writerow([' '])
        writer.writerows(gewem_data)

    # print(results)

def process_key_val(key, val, ne_data, gewem_data):
    # print(f'{key}\n')
    # print(f'{val}\n')

    for index, (r1, r2) in enumerate(val):
        # print(f'{index} {r1}')
        if ne_data[index] == None:
            ne_data[index] = [index+1]

        ne_data[index].append(r1)

        if gewem_data[index] == None:
            gewem_data[index] = [index+1]

        gewem_data[index].append(r2)

    return ne_data, gewem_data

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A simple example script.")

    # Add arguments
    parser.add_argument("-loA", type=int, default=-1, help="lower bound for A", required=False)
    parser.add_argument("-hiA", type=int, default=1, help="upper bound for A", required=False)

    parser.add_argument("-lob", type=int, default=-1, help="lower bound for b", required=False)
    parser.add_argument("-hib", type=int, default=1, help="upper bound for b", required=False)

    parser.add_argument("-size", type=int, default=3, help="size x size matrix", required=False)

    # Parse the arguments
    args = parser.parse_args()

    main(args)