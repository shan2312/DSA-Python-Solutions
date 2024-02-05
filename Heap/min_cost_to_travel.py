
# A car has to travel from point A to point B.
# The fuel capacity of the tank of the car is V units.
# Initially, the tank is completely filled.

# There are m Gas Stations at points D1, D2, .... Dm on the way between A and B and the cost of fuel at each Gas Station is given by a price array P, where Pi = price of fuel per unit at Gas Station i. Each Gas Station is having unlimited quantity of fuel and you may fill as much as you want (obviously <=V).

# Return the minimum cost to travel from point A to point B.

import heapq

def get_minimum_cost(tank_capacity, distance, gas_stations):

    gas_stations.sort(key = lambda x: x[0])
    gas_stations.append((distance, float('inf')))

    available_gas = []
    heapq.heapify(available_gas)
    current_fuel = tank_capacity
    total_price = 0
    prev_distance = 0

    for current_distance, current_price in gas_stations:
        delta_distance = current_distance - prev_distance

        print(available_gas, current_fuel, delta_distance)

        if (len(available_gas) == 0 and current_fuel < delta_distance) or (delta_distance - current_fuel) > tank_capacity:
            return -1
        
        if current_fuel >= delta_distance:
            current_fuel -= delta_distance

        else:
            prev_price = available_gas[0]
            total_price += prev_price*(delta_distance - current_fuel)
            current_fuel = 0
        heapq.heappush(available_gas, current_price)
        prev_distance = current_distance
            

    return total_price


# print(get_minimum_cost(20, 100, [(50, 10), (70, 10)]))
print(get_minimum_cost(50, 100, [(20, 5), (70, 1)]))


