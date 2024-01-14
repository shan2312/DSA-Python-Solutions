def get_best_block(blocks, requirements):
    block_distance_list = [{requirement: float('inf') for requirement in requirements} for _ in range(len(blocks))]


    for index in range(len(block_distance_list)):
        for requirement in requirements:
            if blocks[index][requirement]:
                block_distance_list[index][requirement] = 0
                continue

            if (index - 1) < 0:
                continue

            block_distance_list[index][requirement] = block_distance_list[index - 1][requirement] + 1


    for index in range(len(block_distance_list) - 1, -1, -1):
        for requirement in requirements:
            if (index + 1) >= len(blocks):
                continue
            block_distance_list[index][requirement] = min(block_distance_list[index][requirement], block_distance_list[index + 1][requirement] + 1)
    
    farthest_distances = [0] * len(block_distance_list)
    for index in range(len(block_distance_list)):
        farthest_distances[index] = max([v for k,v in block_distance_list[index].items()])

    return farthest_distances.index(min(farthest_distances))


print(get_best_block([
    {'gym': False, 'school': True, 'store': False}, 
    {'gym': True, 'school': False, 'store': False},
    {'gym': True, 'school': True, 'store': False},
    {'gym': False, 'school': True, 'store': False},
    {'gym': False, 'school': True, 'store': True}], ['gym', 'school', 'store']))



    
