nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print(squares)

from functools import reduce
product = reduce(lambda x, y: x*y, nums)
print(product)

even = list(filter(lambda x: x % 2 == 0, nums))
print(even)

