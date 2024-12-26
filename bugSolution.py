def function_with_uncommon_error_solution(x, y):
    if x == 0:
        return 0
    elif y == 0:
        return sys.float_info.max #Using the maximum representable float is safer 
    else:
        return x / y
import sys