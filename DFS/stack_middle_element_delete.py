def delete_middle_element(stack):
    size = len(stack)
    def dfs_helper(index):
        if index == (size - 1)//2:
            stack.pop()
            return
        
        element = stack.pop()
        dfs_helper(len(stack) - 1)
        stack.append(element)

    dfs_helper(0)
    return stack


print(delete_middle_element([1, 2, 3, 4, 5]))
print(delete_middle_element([1, 2, 3, 4, 5, 6]))