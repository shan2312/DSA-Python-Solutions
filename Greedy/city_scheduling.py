  
def get_min_cost(costs):
  diff = [(i, (a - b)) for i, (a, b) in enumerate(costs)]
  diff.sort(key = lambda x: x[1])

  count_for_each = len(costs)//2
  print(count_for_each, diff)
 
  return sum([costs[index][0] if i < count_for_each else costs[index][1] for i, (index, _) in enumerate(diff)])

def two_city_scheduling(costs):
    total_cost = 0
    costs.sort(key = lambda x : x[0] - x[1])
    cost_length = len(costs)
   
    for i in range(cost_length//2):
        total_cost = total_cost + costs[i][0] + costs[cost_length-i-1][1];
  
    return total_cost

print(two_city_scheduling([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]))

print(get_min_cost([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]))