def check_na(array_ar, letter_ar):
    na = 0
    for i in range(len(array_ar)):
        if letter_ar[i] == 1 and (array_ar[i] != 0 and array_ar[i] != 1):
            na += 1
    return na