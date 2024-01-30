import heapq

def min_refuel_stops(target, start_fuel, stations): 
    stations.append([target, 0])
    max_fuel = []
    heapq.heapify(max_fuel)
    count = 0

    for distance, fuel in stations:

        start_fuel -= distance
        while start_fuel < 0:
            if max_fuel:
                start_fuel += -1 * heapq.heappop(max_fuel)
                count += 1
            else:
                return -1 

        heapq.heappush(max_fuel, -1 * fuel)

        print(start_fuel)
    return count if start_fuel >=0 else -1


print(min_refuel_stops(120 , 10 , [[10, 60], [20, 25], [30, 30], [60, 40]]))