def calculate_volume(spaceship_part: list[int]) -> int:
    block_sum, sum = 0, 0
    max_val, max_val_ind = 0, 0

    for ind, elem in enumerate(spaceship_part):
        if elem < max_val:
            block_sum += elem
            continue

        sum += (ind - max_val_ind - 1) * max_val - block_sum
        max_val, max_val_ind = elem, ind
        block_sum = 0

    return sum


def material(spaceship: list[int]) -> int:
    max_val, ind_of_max = 0, 0

    for ind, elem in enumerate(spaceship):
        if elem < max_val: continue
        ind_of_max = ind
        max_val = elem

    return calculate_volume(spaceship[:ind_of_max + 1]) + calculate_volume((spaceship[ind_of_max:])[::-1])