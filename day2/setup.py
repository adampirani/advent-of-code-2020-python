EXPENSES = open('input.txt', 'r')
expenses_array = EXPENSES.read().splitlines()
ledger = set()


def findProduct(total, expenses, start=0):
    """Get the product of the two numbers that add to the total"""
    for idx, expense in enumerate(expenses, start):
        expense_int = int(expense)
        if ((total-expense_int) in ledger):
            return (expense_int*(total-expense_int))
        else:
            ledger.add(expense_int)


def findTripleProduct(total, expenses):
    """Get the product of the three numbers that add to the total"""
    for idx, expense in enumerate(expenses):

        expense_int = int(expense)
        remainder = total-expense_int
        remainderProduct = findProduct(remainder, expenses, idx+1)

        if (remainderProduct):
            return remainderProduct*expense_int


print(findTripleProduct(2020, expenses_array))
