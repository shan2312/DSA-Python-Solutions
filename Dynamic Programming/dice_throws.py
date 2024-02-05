from collections import defaultdict

def diceThrows(numDice, numSides, target):
    cache = defaultdict(int)

    def get_ways_to_get_target(num_dice, target):
        if (num_dice, target) in cache:
            return cache[(num_dice, target)]
   
        if num_dice == 0 and target == 0:
            return 1
            
        elif num_dice == 0 or target == 0:
            return 0
        
        ways = 0
        for throw in range(1, numSides + 1):
            ways += get_ways_to_get_target(num_dice - 1, target - throw)
        cache[(num_dice, target)] = ways
        return cache[(num_dice, target)]

    return get_ways_to_get_target(numDice, target)

def dice_throw_iterative(numDice, numSides, target):
    cache = [[0] * (target + 1) for i in range(2)]
    cache[0][0] = 1

    for curr_num_dice in range(1, numDice + 1):
        for current_target in range(target, 0, -1):
            for throw in range(numSides, 0, -1):
                if throw > current_target:
                    continue    
                cache[curr_num_dice%2][current_target] += cache[(curr_num_dice - 1)%2][current_target - throw]
    return cache[numDice%2][-1]


        
# print(diceThrows(3, 10, 12))
print(dice_throw_iterative(3, 10, 12))