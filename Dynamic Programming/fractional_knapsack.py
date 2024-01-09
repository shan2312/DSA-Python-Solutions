def solve_fractional_knapsack(profit_weight_list, max_weight):
    profit_per_weight = [(p/w, p, w) for p, w in profit_weight_list]
    profit_per_weight.sort(key = lambda x: x[0], reverse = True)

    max_value = 0

    current_weight = index = 0
    while index < len(profit_per_weight):
    
        if (current_weight + profit_per_weight[index][2]) > max_weight:
            max_value += (max_weight - current_weight)*profit_per_weight[index][0]
            current_weight = max_weight
            return max_value

        max_value += profit_per_weight[index][1]
        current_weight += profit_per_weight[index][2]
        index += 1
    return max_value


print(solve_fractional_knapsack([(60, 10), (100, 20), (120, 30)], 50))
