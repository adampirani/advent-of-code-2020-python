LEN_FIRST_HALF = 7


def get_row_text(token):
    return token[:LEN_FIRST_HALF]


def get_col_text(token):
    return token[LEN_FIRST_HALF:]


def get_binary_value(token, high_char, low_char):
    min_val = 0
    max_val = 2**len(token) - 1

    for char in token:
        if char == high_char:
            min_val = ((min_val + max_val) + 1)/2
        else:
            max_val = ((min_val + max_val) + 1)/2 - 1

    return min_val


def get_id(row, column):
    return row*8 + column
