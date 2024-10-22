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

    increment1 = False if u_ar1 >= threshold else True
    increment2 = False if u_ar2 > threshold else True

    iteration = 1
    while (((u_ar1 <= threshold and increment1) or (u_ar1 >= threshold and not increment1)) or
           ((u_ar2 <= threshold and increment2) or (u_ar2 >= threshold and not increment2))):
        if iteration % 2 == 1:
            wp = (na1 * 0.1) / n
            wa = 0.1 - wp
            n, na1 = gamma_subfunction(array_ar, letter_ar1, increment1, n, na1, wp, wa)
            u_ar1 = find_u(letter_ar1, array_ar)
        else:
            wp = (na2 * 0.1) / n
            wa = 0.1 - wp
            n, na2 = gamma_subfunction(array_ar, letter_ar2, increment2, n, na2, wp, wa)
            u_ar2 = find_u(letter_ar2, array_ar)
        iteration += 1

    print(f"Final weight values: {u_ar1}, {u_ar2}\n"
          f"Total sum: {u_ar1 + u_ar2}\n"
          f"Cycles spent: {iteration}")