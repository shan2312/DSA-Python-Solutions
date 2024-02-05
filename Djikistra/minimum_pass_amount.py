# s1 -> s3 = 5
# s3 -> s4 = 7
# s3 -> s2 = 6
# s2 -> s4 = 4

# s1 ->5 s3 ->6 s2 ->4 s4

# s1 -> s4

# I/P - source, destination, [(edge, pass_value)]

# O/P - minimum ticket value(int)

# max = 7, min_tkt_value = 7
# s1 -> s3 -> s4
# s1 -> s3 -> s2 -> s4

# {s3 : 7, s1: 7} 



# s1 ------ s2 ---------- s3
#  |                      |
#  |                      |
# s4--------s5------------s6

from collections import defaultdict, deque

CANNOT_REACH_DESTINATION = -1


def build_graph(station_passes):
    graph = defaultdict(list)

    for s1, s2, pass_amount in station_passes:
        graph[s1].append((s2, pass_amount))
        
    for s1, s2, pass_amount in station_passes:
        if s1 not in graph:
            graph[s1] = []
        if s2 not in graph:
            graph[s2] = []

    return graph

def get_minimum_pass_amount(station_passes, source, destination):
    station_passes.sort(key = lambda x: x[2])
    graph = build_graph(station_passes)
    min_pass_amount = float('inf')
    visited_set = set()

    queue = deque([(source, visited_set, 0)])

    while queue:
        current_station, visited_stations, current_pass_amount = queue.popleft()
        if current_station == destination:
            min_pass_amount = min(min_pass_amount, current_pass_amount)
            continue

        for neighbor_station, pass_amount in graph[current_station]:
            if neighbor_station in visited_set: continue
            queue.append((neighbor_station, max(current_pass_amount, pass_amount)))
            if neighbor_station != destination:
                visited_set.add(neighbor_station)

    return min_pass_amount if min_pass_amount != float('inf') else CANNOT_REACH_DESTINATION


def get_minimum_pass_amount(station_passes, source, destination):
    station_passes.sort(key = lambda x: x[2])
    graph = build_graph(station_passes)
    cycle_set = set()

    def get_minimum_pass_amount_from(station_passes, source, destination, cycle_set, graph):
        
        if source == destination:
            return 0
        
        if source in cycle_set:
            return -1
        
        cycle_set.add(source)
        for neighbor_station, pass_amount in graph[source]:
            future_pass_amount = get_minimum_pass_amount_from(station_passes, neighbor_station, destination, cycle_set, graph)

            if future_pass_amount != -1:
                return max(future_pass_amount, pass_amount)

        cycle_set.remove(source)
        return -1

    return get_minimum_pass_amount_from(station_passes, source, destination, cycle_set, graph)


def is_destination_reachable(source, destination, amount, graph):
    queue = deque([source])
    visited_set = set([source])

    while queue:
        current_station = queue.popleft()

        if current_station == destination:
            return True

        for neighbor_station, ticket_amount in graph[current_station]:
            if neighbor_station in visited_set or amount < ticket_amount:
                continue
            queue.append((neighbor_station))
            visited_set.add(neighbor_station)

    return False

def get_minimum_pass_amount_binary(station_passes, source, destination):

    graph = build_graph(station_passes)
    # O(E)
    min_ticket_amount = 0
    max_ticket_amount = max([pass_amount for s1, s2, pass_amount in station_passes])
    # O(E)
    
    # O((V + E)*log(max))
    while min_ticket_amount <= max_ticket_amount:
        middle = (min_ticket_amount + max_ticket_amount)//2

        if is_destination_reachable(source, destination, middle, graph):
            max_ticket_amount = middle - 1
            answer = middle

        else:
            min_ticket_amount = middle + 1

    return answer


import heapq
def get_minimum_pass_amount_djikstra(station_passes, source, destination):
    graph = build_graph(station_passes)

    distance_dict = {node: [float('inf'), None] for node in graph}
    distance_dict[source][0] = 0
    min_heap = [(0, source)]

    while min_heap:
        min_pass_amount, curr_node = heapq.heappop(min_heap)

        
        for neighbor, pass_amount in graph[curr_node]:
            current_max = max(distance_dict[curr_node][0], pass_amount)
            if current_max < distance_dict[neighbor][0]:
                distance_dict[neighbor][0] = current_max
                distance_dict[neighbor][1] = curr_node
                heapq.heappush(min_heap, (current_max, neighbor))

    path = get_path(distance_dict, destination)
    path.reverse()
    return distance_dict[destination][0], path

def get_path(distance_dict, destination):
    path = []
    while destination is not None:
        path.append(destination)
        destination = distance_dict[destination][1]

    return path
            


print(get_minimum_pass_amount_djikstra([('s1', 's2', 4), ('s2', 's3', 10), ('s3', 's4', 2), ('s2', 's5', 3), ('s5', 's6', 1), ('s6', 's2', 22), ('s6', 's3', 1)], 's1', 's4'))
print(get_minimum_pass_amount_djikstra([('s1', 's3', 5), ('s3', 's4', 7), ('s3', 's2', 6), ('s2', 's4', 4)], 's1', 's4'))

print(get_minimum_pass_amount_djikstra([('s1', 's2', 5), ('s2', 's3', 10), ('s1', 's4', 6), ('s4', 's3', 6)], 's1', 's3'))



print(get_minimum_pass_amount_binary([('s1', 's2', 4), ('s2', 's3', 10), ('s3', 's4', 2), ('s2', 's5', 3), ('s5', 's6', 1), ('s6', 's2', 22), ('s6', 's3', 1)], 's1', 's4'))
print(get_minimum_pass_amount_binary([('s1', 's3', 5), ('s3', 's4', 7), ('s3', 's2', 6), ('s2', 's4', 4)], 's1', 's4'))

print(get_minimum_pass_amount_binary([('s1', 's2', 5), ('s2', 's3', 10), ('s1', 's4', 6), ('s4', 's3', 6)], 's1', 's3'))