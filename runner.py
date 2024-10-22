from alpha import alpha
from find_u import find_u
from GlobalVariables import *
from create_array import create_array
from create_matrix import create_matrix
from create_array_u import create_array_u
from find_letter_ar import find_letter_ar
from find_threshold_value import find_threshold_value
from gamma import gamma


def main():
    if len(letter1) != len(letter2):
        raise ValueError("Letters must have same length")
    s_count = len(letter1)
    a_count = len(letter1) * 2 // 3

    matrix_sa = create_matrix(a_count, s_count)
    array_ar = create_array(a_count)
    array_u_sa1 = create_array_u(letter1, matrix_sa)
    array_u_sa2 = create_array_u(letter2, matrix_sa)
    threshold_sa = find_threshold_value(array_u_sa1 + array_u_sa2)
    letter_ar1 = find_letter_ar(array_u_sa1, threshold_sa)
    letter_ar2 = find_letter_ar(array_u_sa2, threshold_sa)
    u_ar1 = find_u(letter_ar1, array_ar)
    u_ar2 = find_u(letter_ar2, array_ar)
    threshold_ar = round((u_ar1 + u_ar2) / 2, 1)

    print(f"SA matrix: {matrix_sa}\n"
          f"AR array: {array_ar}\n"
          f"SA array weighted for the first letter: {array_u_sa1}\n"
          f"SA array weighted for the second letter: {array_u_sa2}\n"
          f"Threshold for SA matrix: {threshold_sa}\n"
          f"AR array first letter: {letter_ar1}\n"
          f"AR array second letter: {letter_ar2}\n"
          f"AR array weighted for the first letter: {u_ar1}\n"
          f"AR array weighted for the second letter: {u_ar2}\n"
          f"Threshold for AR array: {threshold_ar}\n")

    print("Alpha function:\n"
          "First letter:")
    alpha(array_ar, letter_ar1, u_ar1, threshold_ar)
    print("Second letter:")
    alpha(array_ar, letter_ar2, u_ar2, threshold_ar)


    test_array1 = [0.2, 0.8, 0.6, 0.9, 0.8, 0.1]
    test_array2 = [1, 1, 1, 1, 0, 0]
    test_array3 = [0, 0, 0, 0, 1, 1]
    test_u1 = 2.5
    test_u2 = 0.9
    test_threshold = 1.7
    print("Gamma function:")
    gamma(test_array1, test_array2, test_array3, test_u1, test_u2, test_threshold)
    #gamma(array_ar, letter_ar1, letter_ar2, u_ar1, u_ar2, threshold_ar)