def find_letter_ar(array_u, threshold):
    letter_ar = []
    for i in array_u:
        if i >= threshold:
            letter_ar.append(1)
        else:
            letter_ar.append(0)
    return letter_ar