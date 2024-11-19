from alpha import alpha
from gamma import gamma
from find_u import find_u
from GlobalVariables import *
from create_array import create_array
from create_matrix import create_matrix
from create_array_u import create_array_u
from find_letter_ar import find_letter_ar
from find_threshold_value import find_threshold_value
from sa_from_file import sa_from_file
from sa_to_file import sa_to_file
from array_to_file import array_to_file
from array_from_file import array_from_file

def main():
    s_count = len(letter1)
    a_count = len(letter1) * 2 // 3
    prompt = input("1 - Save, 2 - Test: ")
    match prompt:
        case "1":
            while True:
                if len(letter1) != len(letter2):
                    raise ValueError("Letters must have same length")
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

                print("Alpha function:")
                alpha_f = alpha(array_ar.copy(), letter_ar1.copy(), letter_ar2.copy(), u_ar1, u_ar2, threshold_ar)

                print("Gamma function:")
                gamma_f = gamma(array_ar.copy(), letter_ar1, letter_ar2, u_ar1, u_ar2, threshold_ar)

                if alpha_f and gamma_f:
                    sa_to_file(matrix_sa)
                    array_to_file(array_ar, "ar")
                    array_to_file(alpha_f, "alpha")
                    array_to_file(gamma_f, "gamma")
                    print("Data saved successfully")
                    break
        case "2":
            matrix_sa = sa_from_file()
            array_ar = array_from_file("ar")
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

            print("Alpha function:")
            alpha_f = alpha(array_ar.copy(), letter_ar1.copy(), letter_ar2.copy(), u_ar1, u_ar2, threshold_ar)

            for i in range(len(alpha_f)):
                alpha_f[i] = round(alpha_f[i], 1)


            print("Gamma function:")
            gamma_f = gamma(array_ar, letter_ar1, letter_ar2, u_ar1, u_ar2, threshold_ar)

            alpha_g = array_from_file("alpha")
            gamma_g = array_from_file("gamma")

            if (all(f == g for f, g in zip(alpha_f, alpha_g))):
                print("The data was recognized successfully")
            else:
                print("The data is different")