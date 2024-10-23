def alpha_subfunction(array_ar, letter_ar, w):
    for i in range(len(array_ar)):
        if letter_ar[i] == 1 and (array_ar[i] != 0 and array_ar[i] != 1):
            if array_ar[i] + w <= 0:
                array_ar[i] = 0
            elif array_ar[i] + w >= 1:
                array_ar[i] = 1
            else:
                array_ar[i] += w
                array_ar[i] = round(array_ar[i], 1)