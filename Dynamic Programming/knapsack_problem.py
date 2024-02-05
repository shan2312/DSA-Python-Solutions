def knapsackProblem(items, capacity):
    knapsack_values = [[0]*(capacity + 1) for _ in range(len(items) + 1)]
    
    for i in range(1, len(items) + 1):
        for c in range(1, capacity + 1):
            item_value, item_weight = items[i - 1]
            left_weight = (c - item_weight)

            if left_weight < 0:
                knapsack_values[i][c] = knapsack_values[i - 1][c]
                continue

            knapsack_values[i][c] = max(knapsack_values[i - 1][c], item_value + knapsack_values[i - 1][left_weight])
    return knapsack_values[-1][-1], get_knapsack_items(knapsack_values, items)


def get_knapsack_items(knapsack_values, items):
   
    sequence = []
    i = len(knapsack_values) - 1
    c = len(knapsack_values[0]) -1

    while i > 0:
        if knapsack_values[i][c] == knapsack_values[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1

        if c==0:
            break
    return list(reversed(sequence))