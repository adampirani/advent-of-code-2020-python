
TREE_CHAR = '#'
OPEN_CHAR = '.'


def is_hit(path, idx):
    path_len = len(path)
    return path[idx % path_len] == TREE_CHAR


def num_trees(map, start_down=0, start_right=0, num_down=1, num_right=3):
    count = 0
    down = start_down + num_down
    right = start_right + num_right
    while down < len(map):
        path = map[down]
        if is_hit(path, right):
            count += 1
        down += num_down
        right += num_right

    return count
