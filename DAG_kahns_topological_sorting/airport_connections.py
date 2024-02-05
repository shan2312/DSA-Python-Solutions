from collections import defaultdict

class AirportNode:
    def __init__(self, airport):
        self.airport = airport
        self.connections = []
        self.is_reachable = True
        self.unreachable_connections = []

# O(a + r) time and space 
def build_airport_graph(airports, routes):
    airport_graph = {}

    for airport in airports:
        airport_graph[airport] = AirportNode(airport)

    for airport1, airport2 in routes:
        airport_graph[airport1].connections.append(airport2)

    return airport_graph

def depth_first_traversal(airport_graph, airport, visited_airports):
    if airport in visited_airports:
        return
    
    visited_airports.add(airport)
    for neighbor_airport in airport_graph[airport]:
        depth_first_traversal(airport_graph, neighbor_airport, visited_airports)

# O(a + r), O(a) space
def get_unreachable_airports(airport_graph, airports, startingAirport):
    visited_airports = {}

    depth_first_traversal(airport_graph, startingAirport, visited_airports)

    unreachable_airport_nodes = []

    for airport in airports:
        if airport in visited_airports:
            continue
        airport_node = airport_graph[airport]
        airport_node.is_reachable = False
        unreachable_airport_nodes.append(airport_node)
    return unreachable_airport_nodes

def mark_unreachable_connections_of(airport_graph, airport_node, visited_airports, unreachable_airports):
    if airport_node.is_reachable:
        return 
    
    if airport_node in visited_airports:
        return
    
    visited_airports.add(airport_node)
    airport_node.unreachable_connections.append(neighbor_airport)

    for neighbor_airport in airport_graph[airport_node]:  
        mark_unreachable_connections_of(airport_graph, neighbor_airport, visited_airports, unreachable_airports)

def mark_unreachable_connections(airport_graph, unreachable_airport_nodes):
    for airport_node in unreachable_airport_nodes:
        visited_airports = {}
        mark_unreachable_connections_of(airport_graph, airport_node, visited_airports, unreachable_airports)


def get_min_number_of_new_connections(airport_graph, unreachable_airport_nodes):
    unreachable_airport_nodes.sort(key = lambda airport: len(airport.unreachable_connections), reverse = True)
    
    count= 0
    for airport in unreachable_airport_nodes:
        if airport.is_reachable:
            continue
        
        count += 1
        for unreachable_airport in airport.unreachable_airport_node:
            airport_graph[unreachable_airport].is_reachable = True

    return count

   
def get_minimum_flights_to_connect(airports, routes, startingAirport):
    airport_graph = build_airport_graph(airports, routes)

    unreachable_airport_nodes = get_unreachable_airports(airport_graph, airports, startingAirport)

    mark_unreachable_connections(airport_graph, unreachable_airport_nodes)

    return get_min_number_of_new_connections(graph, unreachable_airport_nodes)



