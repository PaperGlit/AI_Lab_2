from gamma_subfunction import gamma_subfunction
from find_u import find_u


def gamma(array_ar, letter_ar1, letter_ar2, u_ar1, u_ar2, threshold):
    n = len(array_ar)
    na1 = sum(letter_ar1)
    na2 = sum(letter_ar2)

    print(f"Starting weights: {u_ar1}, {u_ar2}\n"
          f"Starting sum: {u_ar1 + u_ar2}\n"
          f"Threshold: {threshold}")

    if na1 == 0 or na2 == 0:
        print("There are no active links in letters")
        return

    increment = False if u_ar1 >= threshold else True

    w = 0
    iteration = 1
    while (((u_ar1 <= threshold and increment) or (u_ar1 >= threshold and not increment)) or
           ((u_ar2 <= threshold and not increment) or (u_ar2 >= threshold and increment))):
        if iteration % 2 == 1:
            if increment:
                wp = -1 * ((na1 * 0.1 + w) / n)
                wa = 0.1 + wp
            else:
                wp = (na1 * 0.1 + w) / n
                wa = -1 * (0.1 - wp)
            n, na1, w = gamma_subfunction(array_ar, letter_ar1, n, na1, wp, wa)
            u_ar1 = find_u(letter_ar1, array_ar)
        else:
            if not increment:
                wp = -1 * ((na2 * 0.1 + w) / n)
                wa = 0.1 + wp
            else:
                wp = (na2 * 0.1 + w) / n
                wa = -1 * (0.1 - wp)
            n, na2, w = gamma_subfunction(array_ar, letter_ar2, n, na2, wp, wa)
            u_ar2 = find_u(letter_ar2, array_ar)
        iteration += 1

    print(f"Final weight values: {u_ar1}, {u_ar2}\n"
          f"Total sum: {u_ar1 + u_ar2}\n"
          f"Cycles spent: {iteration}")