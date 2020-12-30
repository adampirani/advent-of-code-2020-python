
MIN_MAX_DELIM = "-"
LETTER_DELIM = " "
PWORD_DELIM = ": "


def is_valid(password, letter, min, max):
    letter_count = 0
    for char in password:
        if letter == char:
            letter_count += 1
    return letter_count >= min and letter_count <= max


def split(line):
    min_str = ''
    max_str = ''
    letter = ''
    password = ''
    idx = 0

    while idx < len(line):
        char = line[idx]
        if not min_str:
            min_str += char
            idx += 1
            continue

        if min_str and not max_str:
            if char == MIN_MAX_DELIM:
                max_str = line[idx+1]  # start max_str
                idx += 2
                continue
            else:
                min_str += char
                idx += 1
                continue

        if not letter:
            if char == LETTER_DELIM:
                letter = line[idx+1]
                password = line[idx+2+len(PWORD_DELIM):]
                break
            else:
                max_str += char
                idx += 1
                continue

    return {
        'min': int(min_str),
        'max': int(max_str),
        'letter': letter,
        'password': password
    }


def num_valid(password_array):
    count = 0
    for password in password_array:
        splits = split(password)
        if is_valid(splits['password'], splits['letter'], splits['min'], splits['max']):
            count += 1

    return count
