
from day2 import passwords

PASSWORDS = open('day2/input.txt', 'r')
passwords_array = PASSWORDS.read().splitlines()

print(passwords.num_valid(passwords_array))
