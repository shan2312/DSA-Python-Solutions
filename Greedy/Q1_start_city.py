def validStartingCity(distances, fuel, mpg):
    extra_fuel_list = []

    for i in range(len(distances)):
        extra_fuel = (fuel[i] - distances[i]/mpg)
        extra_fuel_list.append(extra_fuel)

    print(extra_fuel_list)

    for i in range(len(distances)):
        if extra_fuel_list[i] < 0:
            continue
        if extra_fuel_list[i - 1] > 0:
            continue
        return i


if __name__ == '__main__':
    
    d = {
        "distances": [15, 20, 25, 30, 35, 5],
        "fuel": [0, 3, 0, 0, 1, 1],
        "mpg": 26
    }
    print(validStartingCity(d['distances'], d['fuel'], d['mpg']))