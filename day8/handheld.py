def process_instruction(instruction, index, acc, visited):

    instruction_type, instruction_value = instruction.split(' ')
    visited.add(index)

    if instruction_type == 'nop':
        index += 1
    elif instruction_type == 'acc':
        index += 1
        acc += int(instruction_value)
    elif instruction_type == 'jmp':
        index += int(instruction_value)

    return index, acc, visited


def find_loop(instruction_array):

    index = 0
    acc = 0
    visited = set()

    while index < len(instruction_array):
        if index in visited:
            return index, acc, visited
        instruction = instruction_array[index]

        index, acc, visited = process_instruction(
            instruction,
            index,
            acc,
            visited
        )

    return index, acc, visited


def has_loop(index, array_len):
    return index < array_len


def modify_instruction(instruction):
    if instruction.find('nop') > -1:
        return instruction.replace('nop', 'jmp')
    elif instruction.find('jmp') > -1:
        return instruction.replace('jmp', 'nop')
    else:
        return instruction


def modify_loop(instructions_array):
    """
        Assumes there's already a loop
        Skips trying to fix a loop if it's an 'acc' instruction
    """
    instruction_idx_to_change = 0
    looping = True
    array_len = len(instructions_array)

    while (looping):
        instruction_to_change = instructions_array[instruction_idx_to_change]
        changed_instruction = modify_instruction(instruction_to_change)

        if changed_instruction != instruction_to_change:
            instructions_array[instruction_idx_to_change] = changed_instruction
            index, acc, visited = find_loop(instructions_array)
            looping = has_loop(index, array_len)
            instructions_array[instruction_idx_to_change] = instruction_to_change

        instruction_idx_to_change += 1

    return index, acc, visited
