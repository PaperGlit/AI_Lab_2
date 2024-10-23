from gamma_subfunction import gamma_subfunction
from check_na import check_na
from find_u import find_u


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
            if increment:
                wp = (na1 * 0.1 + w) / n
                wa = -1 * (0.1 * wp)
            else:
                wp = -1 * (na1 * 0.1 + w) / n
                wa = 0.1 - (-1 * wp)
            n, w = gamma_subfunction(array_ar, letter_ar1, n, wp, wa)
        else:
            print(f"Iteration number: {counter}. Second cycle")
            na2 = check_na(array_ar, letter_ar2)
            if increment:
                wp = -1 * (na2 * 0.1 + w) / n
                wa = 0.1 - (-1 * wp)
            else:
                wp = (na2 * 0.1 + w) / n
                wa = -1 * (0.1 - wp)
            n, w = gamma_subfunction(array_ar, letter_ar2, n, wp, wa)
        u_ar1 = find_u(letter_ar1, array_ar)
        u_ar2 = find_u(letter_ar2, array_ar)
        u_sum = round(u_ar1 + u_ar2, 1)
        counter += 1
        if counter == 100:
            print("Gamma function can not be found for this instance")
            return

    print(f"Final weight values: {u_ar1}, {u_ar2}\n"
          f"Total sum: {u_sum}\n"
          f"Iterations spent: {counter - 1}\n"
          f"Final array: {array_ar}\n")
