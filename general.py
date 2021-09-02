def calculate_factorial(x):
    if x == 1:
        return 1
    return x * calculate_factorial(x - 1)


def iterative_factorial(x):
    final_result = 1
    while x != 1:
        final_result = final_result * x
        x = x -1

    return final_result


result = calculate_factorial(10)
print(str(result))

final_value = iterative_factorial(10)
print(str(final_value))
