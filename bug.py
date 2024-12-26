def function_with_uncommon_error(x, y):
    if x == 0:
        return 0
    elif y == 0:
        return float('inf')  # Using float('inf') can cause unexpected behaviour
    else:
        return x / y