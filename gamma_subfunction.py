def gamma_subfunction(array_ar, letter, increment, n, na, wp, wa):
    iterations_left = len(array_ar)
    for i in range(len(array_ar)):
        if letter[i] == 1:
            if not increment:
                if array_ar[i] != 0:
                    if array_ar[i] - wa <= 0:
                        w = abs(array_ar[i] - wa)

                        wa = wa - (w / iterations_left)
                        wp = wp + (w / iterations_left)
                        array_ar[i] = 0
                        n -= 1
                        na -= 1
                    else:
                        array_ar[i] -= wa
            else:
                if array_ar[i] != 1:
                    if array_ar[i] + wa >= 1:
                        w = wa - abs(1 - array_ar[i])
                        wa += w
                        wp += w
                        array_ar[i] = 1
                        n -= 1
                        na -= 1
                    else:
                        array_ar[i] += wa
        else:
            if not increment:
                if array_ar[i] != 1:
                    if array_ar[i] + wp >= 1:
                        w = wa - abs(1 - array_ar[i])
                        wa += w
                        wp += w
                        array_ar[i] = 1
                        n -= 1
                    else:
                        array_ar[i] += wp
            else:
                if array_ar[i] != 0:
                    if array_ar[i] - wp <= 0:
                        w = abs(array_ar[i] - wa)
                        wa += w
                        wp += w
                        array_ar[i] = 0
                        n -= 1
                    else:
                        array_ar[i] -= wp
        iterations_left -= 1
    return n, na