def get_number_of_days(weights, capacity):
        present_sum = 0
        i = 0
        count_days = 1
        
        while i < len(weights):
            present_sum += weights[i]

            if present_sum > capacity:
                i -= 1
                count_days += 1
                present_sum = 0
                
            i += 1
        return count_days


def shipWithinDays(weights, days):
    min_cap = max(weights)
    max_cap = sum(weights)

    while min_cap < max_cap:
        mid_cap = (min_cap + max_cap)//2
        
        mid_cap_days = get_number_of_days(weights, mid_cap)
        
        if mid_cap_days > days:
            min_cap = mid_cap + 1

        elif mid_cap_days <= days:
            max_cap = mid_cap
    
    return min_cap


if __name__ == '__main__':
    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5
    print(shipWithinDays(weights, days))
