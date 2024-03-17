from functools import reduce


def process_numbers(numbers):
    positive_numb = filter(lambda x: x > 0 and x % 2 == 0, numbers)
    squared_numb = map(lambda x: x ** 2, positive_numb)
    sum_of_squared_numbers = reduce(lambda x, y: x + y, squared_numb, 0)
    return sum_of_squared_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, -2, -4]
result = process_numbers(numbers)
print(result)
