def gamma_process(value_ar, n, wa):
    w = 0
    if value_ar - wa >= 1:
        w = (value_ar - wa) - 1
        value_ar = 1
        n -= 1
    elif value_ar - wa <= 0:
        w = abs(value_ar - wa)
        value_ar = 0
        n -= 1
    else:
        value_ar -= wa
    if value_ar <= 0.0001 and value_ar != 0:
        value_ar = 0
        n -= 1
    elif value_ar >= 0.9999 and value_ar != 1:
        value_ar = 1
        n -= 1
    return n, w, value_ar