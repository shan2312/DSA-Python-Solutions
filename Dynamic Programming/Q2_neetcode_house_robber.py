def get_max_rob(houses_wealth):
    rob1 = rob2 = 0
    for wealth in houses_wealth:
        rob1, rob2 = rob2, max(rob1 + wealth, rob2)

    return rob2


if __name__ == '__main__':
    print(get_max_rob([]))
