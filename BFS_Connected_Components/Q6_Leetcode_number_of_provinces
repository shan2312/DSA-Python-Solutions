def build_graph(is_connected_matrix):
    count_cities = len(is_connected_matrix)
    adj_list = [[] for i in range(count_cities)]
    
    for city1_id in range(count_cities):
        for city2_id in range(count_cities):

            if city1_id == city2_id or is_connected_matrix[city1_id][city2_id] != 1:continue
            
            adj_list[city1_id].append(city2_id)
            adj_list[city2_id].append(city1_id)
    return adj_list


def traverse_province(start_city, seen, adj_list):
        stack = [start_city]
        seen.add(start_city)
        
        while stack:
            current_city = stack.pop()

            for next_city in adj_list[current_city]:
                if next_city in seen:continue
                stack.append(next_city)
                seen.add(next_city)

def count_provinces(isConnected):
    count_cities = len(isConnected)
    adj_list = build_graph(isConnected)
    seen = set()
    
    count_provinces = 0
    for city in range(count_cities):
        if city not in seen:
            traverse_province(city, seen, adj_list)
            count_provinces += 1
            
    return count_provinces


if __name__ == '__main__':
    is_connected = [[1,1,0],[1,1,0],[0,0,1]]
    print(count_provinces(is_connected))
                    
               
#         par = [i for i in range(len(isConnected))]
#         rank = [1]*(len(isConnected))
        
#         def find(n):
#             p = par[n]
#             while(p!=par[p]):
#                 p = par[p]
#             return p
        
#         def union(n1, n2):
#             p1, p2 = find(n1), find(n2)
#             if(p1!=p2):
#                 if(rank[p1]<rank[p2]):
#                     par[p1] = p2
#                     rank[p2]+=rank[p1]
#                 else:
#                     par[p2] = p1
#                     rank[p1]+=rank[p2]
#             print(par)
#         for n1 in range(len(isConnected)):
#             for n2 in range(len(isConnected[0])):
#                 if(isConnected[n1][n2]==1 and n1!=n2):
#                     union(n1, n2)
            
    
#         v = set()
#         for n in range(len(isConnected)):
#             v.add(find(n))
        
#         return len(v)