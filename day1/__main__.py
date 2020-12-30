
from day1.src.products import findTripleProduct
EXPENSES = open('day1/input.txt', 'r')
expenses_array = EXPENSES.read().splitlines()


print(findTripleProduct(2020, expenses_array))
