EXPENSES = open('input.txt', 'r')
TOTAL = 2020
ledger = set()

for expense in EXPENSES:
    expense_int = int(expense)
    if ((TOTAL-expense_int) in ledger):
        print(expense_int*(TOTAL-expense_int))
        break
    else:
        ledger.add(expense_int)
