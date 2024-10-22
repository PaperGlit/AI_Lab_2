def gamma(array_ar, letter_ar1, letter_ar2, u_ar1, u_ar2, threshold):
    n = len(array_ar)
    na1 = sum(letter_ar1)
    na2 = sum(letter_ar2)
    sum_active = +u_ar1
    sum_passive = +u_ar2

    if na1 == 0 or na2 == 0:
        print("There are no active connections to finish this function.")
        return

    cycle = 1
    iterations = 0
    while sum_active > threshold or sum_passive < threshold:
        if cycle % 2 != 0:
            correction_active = 0.1 - (na1 * 0.1) / n
            correction_passive = (-1 * na1 * 0.1) / n
            for i in range(n):
                if letter_ar1[i] == 1:
                    if array_ar[i] + correction_active >= 1:
                        correction_active = 0.1 - ((na1 - 1) * 0.1) / (n - 1)
                    array_ar[i] -= correction_active
                    if array_ar[i] > 1:
                        array_ar[i] = 1
                    if array_ar[i] < 0:
                        array_ar[i] = 0
                    sum_active -= correction_active
                else:
                    if array_ar[i] + correction_passive < 0:
                        correction_passive = (-1 * ((na1 - 1) * 0.1)) / (n - 1)
                    array_ar[i] -= correction_passive
                    if array_ar[i] > 1:
                        array_ar[i] = 1
                    if array_ar[i] < 0:
                        array_ar[i] = 0
                    sum_passive -= correction_passive
        else:
            correction_active2 = 0.1 - (na2 * 0.1) / n
            correction_passive2 = (-1 * na2 * 0.1) / n
            for i in range(n):
                if letter_ar2[i] == 1:
                    if array_ar[i] + correction_active2 > 1:
                        correction_active2 = 0.1 - ((na2 - 1) * 0.1) / (n - 1)
                    array_ar[i] += correction_active2
                    if array_ar[i] > 1:
                        array_ar[i] = 1
                    if array_ar[i] < 0:
                        array_ar[i] = 0
                    sum_passive += correction_active2
                else:
                    if array_ar[i] + correction_passive2 < 0:
                        correction_passive2 = (-1 * ((na2 - 1) * 0.1)) / (n - 1)
                    array_ar[i] += correction_passive2
                    if array_ar[i] > 1:
                        array_ar[i] = 1
                    if array_ar[i] < 0:
                        array_ar[i] = 0
                    sum_active += correction_passive2
        cycle += 1
        iterations += 1

    sum_active1 = na1 * 0.1 + (na1 - (2 * na1 ** 2) / n) * 0.1
    sum_active2 = na2 * 0.1 + (na2 - (2 * na2 ** 2) / n) * 0.1

    print(f"Delta sum of weights for the first letter: {sum_active1}\n"
          f"Delta sum of weights for the second letter: {sum_active2}\n"
          f"Final sum for the first letter: {sum_active}\n"
          f"Final sum for the second letter: {sum_passive}\n"
          f"Final array: {array_ar}\n")
