from gamma_process import gamma_process


def gamma_subfunction(array_ar, letter_ar, n, wa, wp):
    w = 0
    for i in range(len(array_ar)):
        if array_ar[i] not in [0, 1]:
            if letter_ar[i] == 1:
                n, w, array_ar[i] = gamma_process(array_ar[i], n, wa)
            else:
                n, w, array_ar[i] = gamma_process(array_ar[i], n, wp)
    return n, w