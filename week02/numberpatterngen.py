# Number Pattern Generator from FreeCodeCamp.org
def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if not n > 0:
        return 'Argument must be an integer greater than 0.'
    result = ""
    for i in range(1, n + 1):
        result += str(i)
        if i < n:
            result += " "
    return result

print(number_pattern(4))