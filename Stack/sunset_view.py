def sunsetViews(buildings, direction):
    buildings_with_sunset_view = []

    if direction == 'WEST':
        buildings.reverse()

    print(buildings)

    for index, height in enumerate(buildings):
        print(buildings_with_sunset_view)
        while len(buildings_with_sunset_view) != 0 and buildings[buildings_with_sunset_view[-1]] <= height:
            buildings_with_sunset_view.pop()

        buildings_with_sunset_view.append(index)

    print(buildings_with_sunset_view)
    if direction == 'WEST':
        buildings_with_sunset_view = [(len(buildings) - index - 1) for index in buildings_with_sunset_view]

    return buildings_with_sunset_view
        

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], 'EAST'))