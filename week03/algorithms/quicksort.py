# Quick Sort Algorithm from FreeCodeCamp.org
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers[:]

    pivot = numbers[0]
    less = [n for n in numbers if n < pivot]
    equal = [n for n in numbers if n == pivot]
    greater = [n for n in numbers if n > pivot]

    return quick_sort(less) + equal + quick_sort(greater)