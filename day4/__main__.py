
from day4 import passport

PASSPORTS = open('day4/input.txt', 'r')
passports_array = PASSPORTS.read().splitlines()

print(
    passport.num_valid(passports_array)
)
