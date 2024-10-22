def gamma_subfunction(array_ar, letter, n, na, wp, wa):
    w = 0
    for i in range(len(array_ar)):
        if array_ar[i] not in [0, 1]:
            if letter[i] == 1:
                if array_ar[i] + wa == 1:
                    w = (array_ar[i] + wa) - 1
                    array_ar[i] = 1
                    na -= 1
                    n -= 1
                elif array_ar[i] + wa == 0:
                    w = abs(array_ar[i] + wa)
                    array_ar[i] = 0
                    na -= 1
                    n -= 1
                else:
                    array_ar[i] += wa
            else:
                if array_ar[i] + wp == 1:
                    w = (array_ar[i] + wp) - 1
                    array_ar[i] = 1
                    n -= 1
                elif array_ar[i] + wp == 0:
                    w = abs(array_ar[i] + wp)
                    array_ar[i] = 0
                    n -= 1
                else:
                    array_ar[i] += wp
    return n, na, w