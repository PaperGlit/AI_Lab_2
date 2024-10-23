from find_u import find_u
from alpha_subfunction import alpha_subfunction


def alpha(array_ar, letter_ar1, letter_ar2, u_ar1, u_ar2, threshold):
    increment = True if u_ar1 < threshold else False
    u_sum = round(u_ar1 + u_ar2, 1)
    counter = 1
    while (((u_ar1 <= threshold and increment) or (u_ar1 >= threshold and not increment)) or
           ((u_ar2 <= threshold and not increment) or (u_ar2 >= threshold and increment))):
        if counter % 2 == 1:
            print(f"Iteration number: {counter}. First cycle")
            if increment:
                alpha_subfunction(array_ar, letter_ar1, 0.1)
            else:
                alpha_subfunction(array_ar, letter_ar1, -0.1)
        else:
            if increment:
                alpha_subfunction(array_ar, letter_ar2, -0.1)
            else:
                alpha_subfunction(array_ar, letter_ar2, 0.1)
        u_ar1 = find_u(letter_ar1, array_ar)
        u_ar2 = find_u(letter_ar2, array_ar)
        u_sum = round(u_ar1 + u_ar2, 1)
        counter += 1
        if counter == 100:
            print("Alpha function can not be found for this instance\n")
            return

    print(f"Final weight values: {u_ar1}, {u_ar2}\n"
          f"Total sum: {u_sum}\n"
          f"Iterations spent: {counter - 1}\n"
          f"Final array: {array_ar}\n")