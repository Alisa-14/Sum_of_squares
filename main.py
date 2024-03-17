from functools import reduce


def process_numbers(numbers):
    positive = filter(lambda x: x > 0 and x % 2 == 0, numbers)
    squared = map(lambda x: x ** 2, positive)
    summa = reduce(lambda x, y: x + y, squared, 0)
    return summa


numbers = [1, 2, 3, 4, 5, 6, 7, -2, -4]
result = process_numbers(numbers)
print(result)
