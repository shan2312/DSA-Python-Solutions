import random

class RandomizedSet:

    def __init__(self) -> None:
        self.random_list = []
        self.value_to_idx = {}

    def insert(self, val):
        if val in self.value_to_idx:
            return False

        self.random_list.append(val)
        last_idx = len(self.random_list) - 1
        self.value_to_idx[val] = last_idx
        return True

    def swapValues(self, i, j):
        i_val = self.random_list[i]
        j_val = self.random_list[j]

        self.random_list[i], self.random_list[j] = j_val, i_val
        self.value_to_idx[i_val] = j
        self.value_to_idx[j_val] = i


    def remove(self, val):
        if val not in self.value_to_idx:
            return False
        
        last_idx = len(self.random_list) - 1
        remove_idx = self.value_to_idx[val]
        self.swapValues(remove_idx, last_idx)

        del self.value_to_idx[val]

        self.random_list.pop()
        
        return True

    def getRandom(self):
        random_num = random.choice(self.random_list)
        return random_num