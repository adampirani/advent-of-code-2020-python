
DEFAULT_FIELDS = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid"
}

BETWEEN_FIELD_DELIM = " "
WITHIN_FIELD_DELIM = ":"


def is_field_valid(field, value):
    if field == 'byr':
        return value >= '1920' and value <= '2002'
    elif field == 'iyr':
        return value >= '2010' and value <= '2020'
    elif field == 'eyr':
        return value >= '2020' and value <= '2030'
    elif field == 'hgt':
        field_inches = value.split('in')
        if len(field_inches) > 1:
            value_inches = field_inches[0]
            return value_inches >= '59' and value_inches <= '76'
        field_cms = value.split('cm')
        if len(field_cms) > 1:
            value_cms = field_cms[0]
            return value_cms >= '150' and value_cms <= '193'
        return False
    elif field == 'hcl':
        field_color = value.split('#')
        if len(field_color) != 2:
            return False
        value_hex = field_color[1]

        if len(value_hex) != 6:
            return False
        for char in value_hex:
            if not ((char >= 'a' and char <= 'f') or (char >= '0' and char <= '9')):
                return False
        return True
    elif field == 'ecl':
        valid_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        return value in valid_colors
    elif field == 'pid':
        if len(value) != 9:
            return False
        for char in value:
            if not (char >= '0' and char <= '9'):
                return False
        return True
    return False


def is_valid(passport_set, req_fields=DEFAULT_FIELDS):
    if len(passport_set) != len(req_fields):
        return False

    for field, value in passport_set.items():
        if not is_field_valid(field, value):
            return False

    return True


def process_line(passport_line, passport_set=set(), req_fields=DEFAULT_FIELDS):
    """Modifies passport_set param"""

    passport_line_array = passport_line.split(BETWEEN_FIELD_DELIM)

    for field in passport_line_array:
        field_array = field.split(WITHIN_FIELD_DELIM)

        field_name = field_array[0]
        field_value = field_array[1]
        if field_name in DEFAULT_FIELDS:
            passport_set[field_name] = field_value

    return passport_set


def num_valid(passports, req_fields=DEFAULT_FIELDS):
    count = 0
    passport_set = {}
    passports_len = len(passports)

    for idx, passport_line in enumerate(passports):
        if passport_line:
            process_line(passport_line, passport_set, req_fields)
            if idx == (passports_len - 1):
                if is_valid(passport_set, req_fields):
                    count += 1
        else:
            if is_valid(passport_set, req_fields):
                count += 1
            passport_set.clear()

    return count
