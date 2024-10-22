def find_threshold_value(array):
    min_value = min(array)
    max_value = max(array)
    mid_value = (max_value + min_value) / 2
    return round(mid_value, 1)