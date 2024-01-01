 
# O(N!*N^2)
def get_permutations(nums):
    if len(nums) == 1:
        return [nums]

    all_permutations_list = []
    for num in nums:
        all_permutations_list.extend([[num] + x for x in get_permutations([n for n in nums if n != num])])

    return all_permutations_list



def get_permutations_opt(nums):
    ans = []
    def backtrack(current_list):
        if len(current_list) == len(nums):
            ans.append(current_list)

        for num in nums:
            if num in current_list:
                continue
            current_list.append(num)
            backtrack(current_list)
            current_list.pop()
    backtrack([])
    return ans

print(get_permutations_opt([1, 2, 3]))


        