def find_w(n, na, w, increment):
    if increment:
        wp = (na * 0.1 + w) / n
        wa = -1 * (0.1 - wp)
    else:
        wp = -1 * (na * 0.1 + w) / n
        wa = 0.1 - (-1 * wp)
    return wp, wa