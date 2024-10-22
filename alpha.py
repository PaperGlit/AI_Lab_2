def alpha(array_ar, picture_ar, u_ar, threshold):
    if u_ar > threshold:
        increment = False
    else:
        increment = True

    array_normalized = []
    for i in range(len(array_ar)):
        if picture_ar[i] == 1:
            array_normalized.append(array_ar[i])
        else:
            array_normalized.append(0)

    counter = 1
    while u_ar <= threshold and increment or u_ar >= threshold and not increment:
        if counter > 100:
            print("Alpha function can not be found for this instance\n")
            return
        for i in range(len(array_normalized)):
            if increment:
                if array_normalized[i]!= 1 and array_normalized[i] != 0:
                    array_normalized[i] += 0.1
            else:
                if array_normalized[i] != 0:
                    array_normalized[i] -= 0.1
            array_normalized[i] = round(array_normalized[i], 1)
        u_ar = sum(array_normalized)
        counter += 1

    print(f"Final weight value: {round(u_ar, 1)}\n"
          f"Cycles spent: {counter}\n"
          f"Final array: {array_normalized}\n")
