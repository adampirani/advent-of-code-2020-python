
def process_person(person, yes_set):
    for char in person:
        if char in yes_set:
            yes_set[char] += 1
        else:
            yes_set[char] = 1


def all_yes_in_group(yes_set, num_in_group):
    count = 0

    for num_yes_in_set in yes_set.values():
        if num_yes_in_set == num_in_group:
            count += 1

    return count


def num_yes(groups_of_groups):
    """
        Could save space complexity by using array of 26 ints
        Then count over the array after, for O(26) = 0 time complexity
    """

    count = 0
    num_in_group = 0
    yes_set = {}
    total_lines = len(groups_of_groups)

    for idx, person in enumerate(groups_of_groups):
        if person:
            process_person(person, yes_set)
            num_in_group += 1
            if idx == (total_lines-1):
                count += all_yes_in_group(yes_set, num_in_group)
                num_in_group = 0
                yes_set.clear()
        else:
            count += all_yes_in_group(yes_set, num_in_group)
            num_in_group = 0
            yes_set.clear()

    return count
