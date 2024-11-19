from gamma_subfunction import gamma_subfunction
from check_na import check_na
from find_u import find_u
from find_w import find_w


def gamma(array_ar, letter_ar1, letter_ar2, u_ar1, u_ar2, threshold):
    n = len(array_ar)
    na1 = sum(letter_ar1)
    na2 = sum(letter_ar2)

    if na1 == 0 or na2 == 0:
        print("There are no active connections to finish this function.")
        return

    increment = True if u_ar1 < threshold else False
    u_sum = u_ar1 + u_ar2
    counter = 1
    w = 0
    while (((u_ar1 <= threshold and increment) or (u_ar1 >= threshold and not increment)) or
           ((u_ar2 <= threshold and not increment) or (u_ar2 >= threshold and increment))):
        if counter % 2 == 1:
            print(f"Iteration number: {counter}. First cycle")
            na1 = check_na(array_ar, letter_ar1)
            wp, wa = find_w(n, na1, w, increment)
            n, w = gamma_subfunction(array_ar, letter_ar1, n, wa, wp)
        else:
            print(f"Iteration number: {counter}. Second cycle")
            na2 = check_na(array_ar, letter_ar2)
            wp, wa = find_w(n, na2, w, not increment)
            n, w = gamma_subfunction(array_ar, letter_ar2, n, wa, wp)
        u_ar1 = find_u(letter_ar1, array_ar)
        u_ar2 = find_u(letter_ar2, array_ar)
        u_sum = round(u_ar1 + u_ar2, 1)
        counter += 1
        if counter == 100:
            print("Gamma function can not be found for this instance")
            return []

    for i in range(len(array_ar)):
       array_ar[i] = round(array_ar[i], 3)

    print(f"Final weight values: {u_ar1}, {u_ar2}\n"
          f"Total sum: {u_sum}\n"
          f"Iterations spent: {counter - 1}\n"
          f"Final array: {array_ar}\n")

    return array_ar