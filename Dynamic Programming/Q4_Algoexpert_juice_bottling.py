
# TC: O(N^3),  SC: O(N^2)
def get_juice_bottling_1(prices):
    size = len(prices)
    max_revenue = [0] *size
    solutions = [[]] * size

    for units in range(size):
        for dividing_point in range(units + 1):
            current_revenue = max_revenue[units - dividing_point] + prices[dividing_point]
            if current_revenue > max_revenue[units]:
                max_revenue[units] = current_revenue
                solutions[units] = [dividing_point] + solutions[units - dividing_point]

    return solutions[-1]


# TC: O(N^2), SC: O(N)
def get_jucie_bottling_2(prices):
    size = len(prices)
    max_revenue = [0] * size
    dividing_points = [0] * size

    for units in range(size):
        for dividing_point in range(units + 1):
            current_revenue = max_revenue[units - dividing_point] + prices[dividing_point]
            if current_revenue > max_revenue[units]:
                max_revenue[units] = current_revenue
                dividing_points[units] = dividing_point

    # build solution
    current_dividing_point = size - 1
    solution = []
    while current_dividing_point != 0:
        solution.append(dividing_points[current_dividing_point])
        current_dividing_point -= dividing_points[current_dividing_point]

    return solution


if __name__ == '__main__':
    print(get_juice_bottling_1([0, 1, 3, 2]))
    print(get_jucie_bottling_2([0, 1, 3, 2]))
